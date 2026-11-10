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
import contextlib
import fcntl
import json
import os
import pathlib
import re
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
_SEMVER = re.compile(
    r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
)
_DIGEST = re.compile(r"[0-9a-f]{64}")
_PRINTABLE = re.compile(r"[!-~]+")
_STAMP = re.compile(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ")


def _is(pattern, value):
    return isinstance(value, str) and bool(pattern.fullmatch(value))


def valid_id(value):
    return _is(_ID, value)


def valid_version(value):
    return _is(_SEMVER, value)


def valid_digest(value):
    return _is(_DIGEST, value)


def valid_stamp(value):
    """A UTC timestamp as manifests carry it: 2026-12-01T08:57:00Z."""
    return _is(_STAMP, value)


def valid_base(value):
    """A manifest's base: an http(s) address with a host and no credentials, query
    or fragment, or an absolute path for a catalog on disk -- either way in
    printable characters without spaces."""
    if not _is(_PRINTABLE, value):
        return False
    if value.startswith("/"):
        return True
    try:
        p = urlsplit(value)
        p.port
    except ValueError:
        return False
    return (p.scheme.lower() in ("http", "https") and bool(p.hostname)
            and "@" not in p.netloc and not p.query and not p.fragment)


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
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
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
    if not os.path.lexists(path):
        return {}
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError) as exc:
        raise StateError(f"{path} cannot be read ({type(exc).__name__})") from None
    want = int if kind == "floors" else str
    if not isinstance(data, dict) or not all(
            isinstance(k, str) and isinstance(v, want) and not isinstance(v, bool)
            for k, v in data.items()):
        raise StateError(f"{path} is not in the form this tool writes")
    return data


def read_trust_state(ws):
    """(floors, signers, addresses). The signer bindings are also implied by the
    floors, which are keyed by catalog and signer: when the bindings file is missing
    and floors exist, the bindings are read back out of them."""
    floors = read_state(ws, "floors")
    path = state_path(ws, "signers")
    if os.path.lexists(path):
        signers = read_state(ws, "signers")
    else:
        signers = {}
        for key in floors:
            base, sep, signer = key.partition(" ")
            if not sep or signer.startswith("SHA256:"):
                continue
            if signers.setdefault(base, signer) != signer:
                raise StateError(f"{path} is missing, and the floors name two signers for {base}")
    return floors, signers, read_state(ws, "addresses")


def write_state(ws, kind, data):
    write_text_atomic(state_path(ws, kind), json.dumps(data, indent=2, sort_keys=True) + "\n")


@contextlib.contextmanager
def state_lock(ws):
    """One writer at a time: hold this, read the state again, check, then write."""
    lock = pathlib.Path(ws) / ".fpa" / "state.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "a") as f:
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


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which == "catalog":
        print(catalog(discover="--no-discover" not in sys.argv[2:]))
    elif which == "workspace":
        print(workspace())
    else:
        print(__doc__)
        sys.exit(2)
