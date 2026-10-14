#!/usr/bin/env python3
"""fpa_roots — where the tools read and write. Two places, kept apart on purpose.

A **catalog** is what a publisher signs: prompts/, index.json, its signature, the
key it publishes, and frompt-catalog.json. A **workspace** is what a client trusts:
its own allowed_signers, fpa.registered, fpa.lock and .fpa/ state. In this
repository the two are the same directory, which is why nobody noticed they were
two things until somebody wanted to host a catalog of their own.

    catalog    FPA_CATALOG, else the nearest directory upward from the current
               one that holds frompt-catalog.json, else this tool checkout
    workspace  FPA_WORKSPACE, else this tool checkout

The workspace never defaults to a catalog found on disk. A catalog directory is
usually a clone of somebody's repository, and a trust root read out of it would
be a key taken from the host it is used to check (FPA.md M7).

    python3 bin/fpa_roots.py catalog      # print the catalog root
    python3 bin/fpa_roots.py workspace    # print the workspace
"""
import json
import os
import pathlib
import sys

TOOLS = pathlib.Path(__file__).resolve().parent.parent
CONFIG = "frompt-catalog.json"


def catalog():
    env = os.environ.get("FPA_CATALOG")
    if env:
        return pathlib.Path(env).expanduser().resolve()
    here = pathlib.Path.cwd().resolve()
    for d in (here, *here.parents):
        if (d / CONFIG).is_file():
            return d
    return TOOLS


def workspace():
    env = os.environ.get("FPA_WORKSPACE")
    return pathlib.Path(env).expanduser().resolve() if env else TOOLS


def config(root=None):
    """The catalog's frompt-catalog.json, or {} when it has none."""
    path = (root or catalog()) / CONFIG
    if not path.is_file():
        return {}
    return json.loads(path.read_text())


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else ""
    if which == "catalog":
        print(catalog())
    elif which == "workspace":
        print(workspace())
    else:
        print(__doc__)
        sys.exit(2)
