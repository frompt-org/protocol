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
import json
import os
import pathlib
import re
import sys

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
