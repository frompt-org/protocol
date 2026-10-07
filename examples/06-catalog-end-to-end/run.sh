#!/usr/bin/env bash
# The whole life of a frompt, end to end, on a throwaway copy of this repository:
# write it, lint it, publish it into a signed catalog, register the catalog,
# resolve it with no digest typed, verify it the managed way -- then watch the
# catalog refuse a tampered copy and a frompt that never offered itself for
# unattended use.
#
# Nothing here touches your checkout: the tools are copied into a temp
# directory, a fresh signing key is made there, and the directory is removed at
# the end. Needs bash, python3, ssh-keygen. No network.
set -euo pipefail
src=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
work=$(mktemp -d "${TMPDIR:-/tmp}/frompt-e2e-XXXXXX")
trap 'rm -rf "$work"' EXIT

step() { printf '\n== %s\n' "$*"; }
# A catalog is a shape: index.json, its signature, prompts/<id>/<version>.frompt.md.
# Copy the tools and the template, and start with no prompts and no state.
mkdir -p "$work/catalog/prompts"
cp -R "$src/bin" "$src/TEMPLATE.frompt.md" "$work/catalog/"
cd "$work/catalog"

step "1. Write a frompt"
bin/fp-new hello -c i-have-read-this-prompt-and-want-my-agent-to-say-hello-once -f linear -o prompts --author example 2>/dev/null
# Offer it to all three adoption contexts, so a registration and a signature can authorize it.
sed -i.bak 's/^contexts: .*/contexts: interactive, registered, managed/' prompts/hello/1.0.0.frompt.md && rm prompts/hello/1.0.0.frompt.md.bak
grep -q '^contexts:' prompts/hello/1.0.0.frompt.md || sed -i.bak 's/^flow:/contexts: interactive, registered, managed\nflow:/' prompts/hello/1.0.0.frompt.md
rm -f prompts/hello/1.0.0.frompt.md.bak
ls prompts/hello/

step "2. Lint it -- structure only, never intent"
bin/fp-lint prompts/hello/1.0.0.frompt.md

step "3. Index it and sign the catalog with a fresh key"
bin/fp-index | tail -1
FPA_SIGNING_IDENTITY=example-publisher bin/fp-sign --keygen >/dev/null 2>&1 || true
FPA_SIGNING_IDENTITY=example-publisher bin/fp-sign | tail -1

step "4. Register it once -- the one consent this workspace keeps"
bin/fp-register "$work/catalog" --pin latest --as example

step "5. Resolve by id, no digest typed: verified against the signed manifest first"
bin/fp-resolve hello --from "$work/catalog" --record

step "6. The managed path: signature, expiry, freshness, digest"
bin/fp-verify hello --from "$work/catalog"

step "7. Tamper with the published bytes -- the resolver refuses"
printf '\n<!-- changed after publication -->\n' >> prompts/hello/1.0.0.frompt.md
if bin/fp-resolve hello --from "$work/catalog" --record 2>&1; then
  echo "UNEXPECTED: tampered bytes were accepted"; exit 1
else
  echo "refused, as it should be"
fi
