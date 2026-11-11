#!/usr/bin/env python3
"""fpa_roots — where the tools read and write. Two places, kept apart on purpose.

A **catalog** is what a publisher signs: prompts/, index.json, its signature, the
key it publishes, and frompt-catalog.json. A **workspace** is what a client trusts:
its own allowed_signers, fpa.registered, fpa.lock and .fpa/ state. In this
repository the two are the same directory, which is why nobody noticed they were
two things until somebody wanted to host a catalog of their own.

    catalog    for the tools that BUILD a catalog (fp-index, fp-sign, fp-publish):
               FPA_CATALOG, else the nearest directory upward from the current
               one that holds frompt-catalog.json, else this tool checkout
               for the tools that READ one (fp-resolve, fp-lock, fp-verify):
               FPA_CATALOG, else this tool checkout -- never a directory found
               on disk
    workspace  FPA_WORKSPACE, else this tool checkout

Building and reading differ on purpose. A publisher standing in their own catalog
means to index and sign it, so finding it saves typing. A client reads a catalog
only because someone chose it: FPA_CATALOG, a registration (--from), or this
checkout. A directory it happens to be standing in is a choice nobody made.

The workspace never defaults to a catalog found on disk. A catalog directory is
usually a clone of somebody's repository, and a trust root read out of it would
be a key taken from the host it is used to check (FPA.md M7).

    python3 bin/fpa_roots.py catalog      # print the catalog root a builder uses
    python3 bin/fpa_roots.py catalog --no-discover   # ...and the one a reader uses
    python3 bin/fpa_roots.py workspace    # print the workspace
"""
import base64
import binascii
import contextlib
import datetime
import hashlib
import fcntl
import json
import os
import pathlib
import re
import stat
import struct
import sys
import tempfile
from urllib.parse import urlsplit, urlunsplit

TOOLS = pathlib.Path(__file__).resolve().parent.parent
CONFIG = "frompt-catalog.json"


def catalog(discover=True):
    env = os.environ.get("FPA_CATALOG")
    if env:
        return pathlib.Path(env).expanduser().resolve()
    if not discover:
        return TOOLS
    here = pathlib.Path.cwd().resolve()
    for d in (here, *here.parents):
        if (d / CONFIG).is_file():
            return d
    return TOOLS


def workspace():
    env = os.environ.get("FPA_WORKSPACE")
    return pathlib.Path(env).expanduser().resolve() if env else TOOLS


# A manifest's `file` is a path under its catalog's prompts/: plain segments that
# each start with a letter or digit. That rules out an absolute path, a URL, `..`,
# a hidden file and anything a command line could read as an option.
_SEGMENT = r"[A-Za-z0-9][A-Za-z0-9._-]*"
_FILE = re.compile(rf"{_SEGMENT}(?:/{_SEGMENT})*")


def safe_file(name):
    """True if a manifest `file` value is a plain relative path under prompts/."""
    return isinstance(name, str) and bool(_FILE.fullmatch(name))


# --- values a manifest or a lock line may carry --------------------------------
# A lock line and a registration line are whitespace-delimited, so every value that
# reaches one is checked against a strict pattern first: no space, no control
# character, nothing a reader could split differently from the writer.
_ID = re.compile(r"[a-z0-9][a-z0-9-]*")
# [0-9], never \d: in Python \d also matches digits of other scripts.
_SEMVER = re.compile(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
)
_DIGEST = re.compile(r"[0-9a-f]{64}")
_PRINTABLE = re.compile(r"[!-~]+")
_STAMP = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z")


def _is(pattern, value):
    return isinstance(value, str) and bool(pattern.fullmatch(value))


def valid_id(value):
    return _is(_ID, value)


def valid_version(value):
    return _is(_SEMVER, value)


def valid_digest(value):
    return _is(_DIGEST, value)


def parse_stamp(value):
    """The moment a manifest timestamp names (2026-12-01T08:57:00Z), as an aware UTC
    datetime, or None when it is not one: the right shape is not enough, the date
    has to exist, and it is compared as a time, never as a string."""
    if not _is(_STAMP, value):
        return None
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def valid_stamp(value):
    """A UTC timestamp as manifests carry it: 2026-12-01T08:57:00Z."""
    return parse_stamp(value) is not None


def valid_base(value):
    """A manifest's base: an http(s) address with a host and no credentials, query
    or fragment, or an absolute path for a catalog on disk -- either way in
    printable characters without spaces, and already in its one plain spelling.

    A spelling that only some readers would take for the same place -- a `.` or
    `..` segment, an empty segment, a percent escape, a `;`, a host ending in a
    dot -- is refused, not normalised: normalising every such form is a promise
    no single function keeps, and a catalog has no reason to be written that way.
    Trailing slashes, the case of scheme and host and a default port are the
    only variations allowed; normalize_base() folds them."""
    if not _is(_PRINTABLE, value):
        return False
    s = value
    while len(s) > 1 and s.endswith("/"):
        s = s[:-1]
    # A path is one plain spelling when normpath leaves it as it is; the characters
    # that only mean something in a URL are ordinary in a file name.
    if s.startswith("/"):
        return not s.startswith("//") and os.path.normpath(s) == s
    if any(c in s for c in "%;?#\\"):
        return False
    try:
        p = urlsplit(s)
        p.port
    except ValueError:
        return False
    if not (p.scheme.lower() in ("http", "https") and p.hostname
            and "@" not in p.netloc and not p.hostname.endswith(".")):
        return False
    if p.path and not p.path.startswith("/"):
        return False
    return all(seg not in ("", ".", "..") for seg in p.path.split("/")[1:])


def scheme_twin(catalog):
    """The same catalog under the other of http and https, or None. One spelling
    per catalog means a base bound under one scheme is not free under the other."""
    for a, b in (("https://", "http://"), ("http://", "https://")):
        if catalog.startswith(a):
            return b + catalog[len(a):]
    return None


def binding_conflict(signers, catalog, signer):
    """(base, bound signer) when this workspace binds the catalog -- under either
    scheme -- to a signer other than this one; None otherwise (M6b)."""
    for k in (catalog, scheme_twin(catalog)):
        bound = signers.get(k) if k else None
        if bound is not None and bound != signer:
            return k, bound
    return None


def normalize_base(value):
    """One spelling per catalog address, used by every tool that compares two of
    them: no trailing slash, and for http(s) the scheme and host in lower case and
    no default port."""
    s = value
    while len(s) > 1 and s.endswith("/"):
        s = s[:-1]
    if s.lower().startswith(("http://", "https://")):
        try:
            p = urlsplit(s)
            scheme, host, port = p.scheme.lower(), (p.hostname or "").lower(), p.port
        except ValueError:
            return s
        if ":" in host:
            host = f"[{host}]"
        netloc = host if port in (None, {"http": 80, "https": 443}[scheme]) else f"{host}:{port}"
        s = urlunsplit((scheme, netloc, p.path, p.query, p.fragment))
        while len(s) > 1 and s.endswith("/"):
            s = s[:-1]
    return s


def write_text_atomic(path, text):
    """Replace a file whole: write a temporary file beside it, then rename it over
    the old one, so a reader sees the old file or the new one and never half of one."""
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # mkstemp makes the file 0600; the file it replaces keeps the mode it had, and a
    # new one gets what the umask gives any new file, so a workspace shared by several
    # accounts stays readable to them.
    try:
        mode = stat.S_IMODE(os.stat(path).st_mode)
    except FileNotFoundError:
        mask = os.umask(0)
        os.umask(mask)
        mode = 0o666 & ~mask
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        os.fchmod(fd, mode)
        with os.fdopen(fd, "w") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except BaseException:
        with contextlib.suppress(OSError):
            os.unlink(tmp)
        raise


# --- the lock: pins, one per id --------------------------------------------------
class LockError(Exception):
    """fpa.lock holds a line this tool would not have written. It is refused, not
    repaired: a pin is a reviewed decision, and a guess about one is not."""


def lock_line_ok(pid, version, digest, url):
    return valid_id(pid) and valid_version(version) and valid_digest(digest) and _is(_PRINTABLE, url)


def parse_lock(path):
    """id -> (version, digest, url) from an fpa.lock; {} when there is none."""
    path = pathlib.Path(path)
    if not path.exists():
        return {}
    out = {}
    for n, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("#") or not line.strip():
            continue
        fields = line.split(" ")
        if (len(fields) != 4 or not fields[2].startswith("sha256:")
                or not lock_line_ok(fields[0], fields[1], fields[2][len("sha256:"):], fields[3])):
            raise LockError(f"{path} line {n} is not '<id> <version> sha256:<digest> <url>'")
        if fields[0] in out:
            raise LockError(f"{path} pins {fields[0]} twice (line {n})")
        out[fields[0]] = (fields[1], fields[2][len("sha256:"):], fields[3])
    return out


# --- trust state: floors and bindings ---------------------------------------------
# What a workspace has accepted: the freshness floors (M6), the signer each catalog
# is bound to and the catalog each address is bound to (M6b). A file that is missing
# is a workspace that has not accepted anything of that kind yet. A file that exists
# and cannot be read is never taken for an empty one: that would be a workspace that
# forgot what it had accepted, so every reader refuses, naming the file.
STATE = {"floors": "manifest-serials.json", "signers": "catalog-signers.json",
         "addresses": "catalog-addresses.json"}


class StateError(Exception):
    """A trust-state file exists but cannot be used."""


def state_path(ws, kind):
    return pathlib.Path(ws) / ".fpa" / STATE[kind]


def read_state(ws, kind):
    path = state_path(ws, kind)
    # .fpa itself must be a directory this tool can read: a file, a dangling link or
    # a directory it may not enter would make every state file look absent.
    d = path.parent
    if os.path.lexists(d) and not (d.is_dir() and os.access(d, os.R_OK | os.X_OK)):
        raise StateError(f"{d} is not a directory this tool can read")
    if not os.path.lexists(path):
        return {}
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError, RecursionError) as exc:
        raise StateError(f"{path} cannot be read ({type(exc).__name__})") from None
    want = int if kind == "floors" else str
    if not isinstance(data, dict) or not all(
            isinstance(k, str) and isinstance(v, want) and not isinstance(v, bool)
            for k, v in data.items()):
        raise StateError(f"{path} is not in the form this tool writes")
    return data


def read_trust_state(ws):
    """(floors, signers, addresses). A floor is keyed by catalog and signer, so it
    is a binding too: a catalog the bindings file does not name is bound to the
    signer its floors name. The floors are written first, so a run stopped between
    the two writes still leaves the binding behind. Rebinding a catalog therefore
    means deleting its binding and the old signer's floor."""
    floors = read_state(ws, "floors")
    signers = read_state(ws, "signers")
    implied = {}
    for key in floors:
        base, sep, signer = key.partition(" ")
        if not sep or signer.startswith("SHA256:"):
            continue
        if implied.setdefault(base, signer) != signer and base not in signers:
            raise StateError(f"{state_path(ws, 'floors')} names two signers for {base}, and "
                             f"{state_path(ws, 'signers')} binds it to neither")
    for base, signer in implied.items():
        signers.setdefault(base, signer)
    return floors, signers, read_state(ws, "addresses")


def write_state(ws, kind, data):
    write_text_atomic(state_path(ws, kind), json.dumps(data, indent=2, sort_keys=True) + "\n")


@contextlib.contextmanager
def state_lock(ws):
    """One writer at a time: hold this, read the state again, check, then write."""
    lock = pathlib.Path(ws) / ".fpa" / "state.lock"
    try:
        lock.parent.mkdir(parents=True, exist_ok=True)
        f = open(lock, "a")
    except OSError as exc:
        raise StateError(f"{lock.parent} is not a directory this tool can use "
                         f"({type(exc).__name__})") from None
    with f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


KEY_TYPES = ("ssh-", "ecdsa-", "sk-")


def _split(text, sep):
    """Split at `sep` outside double quotes; None if a quote is left open."""
    parts, cur, quoted = [], "", False
    for c in text:
        if c == '"':
            quoted = not quoted
        if (c.isspace() if sep is None else c == sep) and not quoted:
            if cur or sep is not None:
                parts.append(cur)
            cur = ""
            continue
        cur += c
    if quoted:
        return None
    if cur or sep is not None:
        parts.append(cur)
    return parts


def signers_entry(line):
    """(principals, options, keytype, key) of an allowed_signers line, or None.

    Fields are split the way OpenSSH splits them: at whitespace outside double
    quotes, so an option value may hold spaces. `options` is a list of
    (name, value) pairs, the name lowercased because OpenSSH matches option names
    without regard to case, the value None for a bare option."""
    text = line.strip()
    if not text or text.startswith("#"):
        return None
    fields = _split(text, None)
    if not fields or len(fields) < 3:
        return None
    if fields[1].startswith(KEY_TYPES):
        principals, opts, keytype, key = fields[0], "", fields[1], fields[2]
    elif len(fields) >= 4 and fields[2].startswith(KEY_TYPES):
        principals, opts, keytype, key = fields[0], fields[1], fields[2], fields[3]
    else:
        return None
    options = []
    for item in (_split(opts, ",") if opts else []) or []:
        name, eq, value = item.partition("=")
        options.append((name.strip().lower(), value.strip().strip('"') if eq else None))
    if opts and _split(opts, ",") is None:
        return None
    return principals, options, keytype, key


def flag_value(argv, flag, tool):
    """The value after `flag`, or None when the flag is absent. A flag given with
    no value is a usage error (exit 2), not a crash."""
    if flag not in argv:
        return None
    i = argv.index(flag) + 1
    if i >= len(argv) or argv[i].startswith("--"):
        print(f"{tool}: {flag} needs a value", file=sys.stderr)
        sys.exit(2)
    return argv[i]


def config(root=None):
    """The catalog's frompt-catalog.json, or {} when it has none."""
    path = (root or catalog()) / CONFIG
    if not path.is_file():
        return {}
    return json.loads(path.read_text())


# --- OpenSSH certificates (FPA.md M7b) ---------------------------------------------
# A certificate is read from its wire format (OpenSSH PROTOCOL.certkeys), never from
# `ssh-keygen -L` text: a key id or a principal is free text an authority signs, and
# text can spell any label. Fingerprints are computed the way ssh-keygen computes them.
CERT_TYPES = {  # certificate type -> (plain key type, number of key fields)
    "ssh-rsa-cert-v01@openssh.com": ("ssh-rsa", 2),
    "ssh-dss-cert-v01@openssh.com": ("ssh-dss", 4),
    "ecdsa-sha2-nistp256-cert-v01@openssh.com": ("ecdsa-sha2-nistp256", 2),
    "ecdsa-sha2-nistp384-cert-v01@openssh.com": ("ecdsa-sha2-nistp384", 2),
    "ecdsa-sha2-nistp521-cert-v01@openssh.com": ("ecdsa-sha2-nistp521", 2),
    "ssh-ed25519-cert-v01@openssh.com": ("ssh-ed25519", 1),
    "sk-ecdsa-sha2-nistp256-cert-v01@openssh.com": ("sk-ecdsa-sha2-nistp256@openssh.com", 3),
    "sk-ssh-ed25519-cert-v01@openssh.com": ("sk-ssh-ed25519@openssh.com", 2),
}


def _string(buf, i):
    if i + 4 > len(buf):
        raise ValueError("truncated")
    (n,) = struct.unpack(">I", buf[i:i + 4])
    if i + 4 + n > len(buf):
        raise ValueError("truncated")
    return buf[i + 4:i + 4 + n], i + 4 + n


def _pack(b):
    return struct.pack(">I", len(b)) + b


def ssh_fingerprint(blob):
    """SHA256:... of a public key blob, as ssh-keygen -l prints it."""
    return "SHA256:" + base64.b64encode(hashlib.sha256(blob).digest()).decode().rstrip("=")


def certificate(blob):
    """The parts of an OpenSSH certificate this client relies on, read from its bytes:
    the authority that signed it, the key it certifies, its key id, principals and
    validity. Raises ValueError for anything that is not a well-formed certificate."""
    ctype, i = _string(blob, 0)
    ctype = ctype.decode("ascii", "strict")
    if ctype not in CERT_TYPES:
        raise ValueError(f"not a certificate type this client reads: {ctype!r}")
    plain, nfields = CERT_TYPES[ctype]
    _nonce, i = _string(blob, i)
    fields = []
    for _ in range(nfields):
        f, i = _string(blob, i)
        fields.append(f)
    if i + 12 > len(blob):
        raise ValueError("truncated")
    i += 12  # uint64 serial, uint32 type
    key_id, i = _string(blob, i)
    packed, i = _string(blob, i)
    principals, j = [], 0
    while j < len(packed):
        p, j = _string(packed, j)
        principals.append(p.decode("utf-8", "strict"))
    if i + 16 > len(blob):
        raise ValueError("truncated")
    after, before = struct.unpack(">QQ", blob[i:i + 16])
    i += 16
    for _ in range(3):  # critical options, extensions, reserved
        _, i = _string(blob, i)
    ca_key, i = _string(blob, i)
    _sig, i = _string(blob, i)
    if i != len(blob):
        raise ValueError("trailing bytes after the certificate")
    certified = _pack(plain.encode()) + b"".join(_pack(f) for f in fields)
    return {"authority": ssh_fingerprint(ca_key), "certified": ssh_fingerprint(certified),
            "key_id": key_id.decode("utf-8", "replace"), "principals": principals,
            "valid_after": after, "valid_before": before}


def signature_key(data):
    """The public key blob inside an armored SSH signature (bytes), read strictly:
    exactly one armor and nothing around it, base64 without junk, the SSHSIG magic."""
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError:
        raise ValueError("the signature file is not plain ASCII") from None
    lines = [l.strip() for l in text.splitlines()]
    try:
        b = lines.index("-----BEGIN SSH SIGNATURE-----")
        e = lines.index("-----END SSH SIGNATURE-----", b)
    except ValueError:
        raise ValueError("no armored signature") from None
    if any(lines[:b]) or any(lines[e + 1:]):
        raise ValueError("text around the armored signature")
    try:
        blob = base64.b64decode("".join(lines[b + 1:e]), validate=True)
    except (binascii.Error, ValueError):
        raise ValueError("the signature is not valid base64") from None
    if blob[:6] != b"SSHSIG":
        raise ValueError("not an SSH signature")
    key, _ = _string(blob, 10)  # after the magic and the uint32 version
    return key


def certificate_file(text):
    """certificate() of an OpenSSH certificate file (`<type> <base64> [comment]`)."""
    parts = text.split()
    if len(parts) < 2:
        raise ValueError("not a certificate file")
    try:
        blob = base64.b64decode(parts[1], validate=True)
    except (binascii.Error, ValueError):
        raise ValueError("not a certificate file") from None
    return certificate(blob)


def cert_identity(authority, principal):
    """The signer a certificate signature counts as: its authority and its principal.
    The comma marks it: OpenSSH splits principals at commas, so no plain principal
    can spell it, and it does not begin with SHA256:, which old floors keyed by key
    used."""
    return f"ca:{authority},{principal}"


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which == "catalog":
        print(catalog(discover="--no-discover" not in sys.argv[2:]))
    elif which == "workspace":
        print(workspace())
    else:
        print(__doc__)
        sys.exit(2)
