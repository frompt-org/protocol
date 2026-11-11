#!/usr/bin/env bash
# The whole life of a frompt, end to end, in a throwaway directory: start a
# catalog, write a frompt, lint it, sign the catalog, register it by its key's
# fingerprint, resolve with no digest typed, verify it the managed way -- then
# watch tampered bytes get refused.
#
# Nothing here touches your checkout: the catalog and the client's workspace are
# temp directories with a fresh signing key, removed at the end. The tools are
# this repository's own; nothing is copied. Needs bash, python3, ssh-keygen. No network.
set -euo pipefail
tools=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/bin
tmp=${TMPDIR:-/tmp}
work=$(mktemp -d "${tmp%/}/frompt-e2e-XXXXXX")
trap 'rm -rf "$work"' EXIT
# The client's trust root, registrations and state live here, not in this checkout.
export FPA_WORKSPACE="$work/client"
unset FPA_CATALOG FPA_SIGNING_IDENTITY FPA_SIGNING_KEY

step() { printf '\n== %s\n' "$*"; }

step "1. Start a catalog: an empty one, already signed"
# In real life --url is where you will serve it. Here the client reads the directory.
"$tools/fp-init-catalog" "$work/catalog" --url "$work/catalog" --identity example-publisher | sed -n '1,3p'
cd "$work/catalog"
fingerprint=$(ssh-keygen -lf .fpa/signing_key.pub | awk '{print $2}')

step "2. Write a frompt"
"$tools/fp-new" hello -c i-have-read-this-prompt-and-want-my-agent-to-say-hello-once -f linear -o prompts --author example 2>/dev/null
# Offer it to all three adoption contexts, so a registration and a signature can authorize it.
sed -i.bak 's/^flow:/contexts: interactive, registered, managed\
flow:/' prompts/hello/1.0.0.frompt.md && rm -f prompts/hello/1.0.0.frompt.md.bak
ls prompts/hello/

step "3. Lint it -- structure only, never intent"
"$tools/fp-lint" prompts/hello/1.0.0.frompt.md

step "4. Index it and sign the catalog"
"$tools/fp-index" | tail -1
"$tools/fp-sign" | sed -n '1,3p'

step "5. Register it once, by the fingerprint the publisher gave you"
"$tools/fp-register" "$work/catalog" --key "$fingerprint" --pin latest --as example

step "6. Resolve by id, no digest typed: verified against the signed manifest first"
"$tools/fp-resolve" hello --from "$work/catalog" --record

step "7. The managed path: signature, expiry, freshness, digest"
"$tools/fp-verify" hello --from "$work/catalog"

step "8. Tamper with the published bytes -- the resolver refuses"
printf '\n<!-- changed after publication -->\n' >> prompts/hello/1.0.0.frompt.md
if "$tools/fp-resolve" hello --from "$work/catalog" --record 2>&1; then
  echo "UNEXPECTED: tampered bytes were accepted"; exit 1
else
  echo "refused, as it should be"
fi
