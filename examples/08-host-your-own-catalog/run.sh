#!/usr/bin/env bash
# Host a catalog on your own domain, and be trusted for it -- the trust story,
# played out between a publisher, a client, and a second publisher the client
# also trusts.
#
#   acme     publishes https://catalog.acme.example and hands out a fingerprint
#   client   registers it by that fingerprint, pins a version, resolves by id
#   globex   another publisher the client trusts, signing a manifest that names
#            acme's catalog -- which must change nothing about acme
#
# A directory stands in for each domain: the client's --from is that directory
# where in production it would be the https URL. Everything is checked the same
# way. Temp directories only, removed at the end. Needs bash, python3, ssh-keygen.
set -euo pipefail
tools=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/bin
tmp=${TMPDIR:-/tmp}
work=$(mktemp -d "${tmp%/}/frompt-host-XXXXXX")
trap 'rm -rf "$work"' EXIT
unset FPA_CATALOG FPA_SIGNING_IDENTITY FPA_SIGNING_KEY
# One trust record per user: this is what ~/.config/frompt would hold.
export FPA_WORKSPACE="$work/client"
acme="$work/catalog.acme.example"
globex="$work/catalog.globex.example"

step() { printf '\n== %s\n' "$*"; }
expect_refusal() { # expect_refusal <what> <command...>
  local what=$1; shift
  if "$@" >"$work/out" 2>&1; then echo "UNEXPECTED: $what was accepted"; cat "$work/out"; exit 1; fi
  sed -n '1,2p' "$work/out"; echo "  -> refused, as it should be"
}
frompt() { # frompt <catalog> <id> <version> <sentence>
  local dir="$1/prompts/$2"
  "$tools/fp-new" "$2" -c "$4" -f linear --version "$3" -o "$1/prompts" --author "$(basename "$1")" >/dev/null 2>&1
  sed -i.bak 's/^flow:/contexts: interactive, registered, managed\
flow:/' "$dir/$3.frompt.md" && rm -f "$dir/$3.frompt.md.bak"
}

step "1. acme starts a catalog for its domain"
"$tools/fp-init-catalog" "$acme" --url https://catalog.acme.example | sed -n '1,3p'
acme_key=$(ssh-keygen -lf "$acme/.fpa/signing_key.pub" | awk '{print $2}')
echo "acme puts this on its website, its README, its security page -- anywhere but the catalog:"
echo "  $acme_key"

step "2. acme publishes a frompt"
frompt "$acme" standup 1.0.0 i-have-read-this-prompt-and-want-a-standup-note-written-from-my-git-log
(cd "$acme" && "$tools/fp-index" | tail -1 && "$tools/fp-sign" | sed -n '1p')

step "3. The client registers acme by a fingerprint it got somewhere else"
expect_refusal "a fingerprint that is not acme's" \
  "$tools/fp-register" "$acme" --key SHA256:0000000000000000000000000000000000000000000
"$tools/fp-register" "$acme" --key "$acme_key" --pin version --as client

step "4. Pin a version from a catalog the client does not hold, then resolve by id"
"$tools/fp-lock" --update standup --from "$acme"
"$tools/fp-resolve" standup --from "$acme" --record

step "5. acme ships 1.1.0 -- a pinned client does not drift onto it"
frompt "$acme" standup 1.1.0 i-have-read-this-prompt-and-want-a-standup-note-with-blockers-from-my-git-log
(cd "$acme" && "$tools/fp-index" >/dev/null && "$tools/fp-sign" >/dev/null)
expect_refusal "an unpinned version" "$tools/fp-resolve" standup --from "$acme" --record
echo "re-pinning is a deliberate act, and a diff somebody reviews:"
"$tools/fp-lock" --update standup --from "$acme"
"$tools/fp-resolve" standup --from "$acme" --record

step "6. globex, also trusted, signs a manifest naming acme's catalog at serial 999999"
"$tools/fp-init-catalog" "$globex" --url https://catalog.globex.example >/dev/null
globex_key=$(ssh-keygen -lf "$globex/.fpa/signing_key.pub" | awk '{print $2}')
"$tools/fp-register" "$globex" --key "$globex_key" --as client >/dev/null
python3 - "$acme/index.json" "$globex/index.json" <<'PY'
import json, sys
m = json.load(open(sys.argv[1]))
m["serial"] = 999999
open(sys.argv[2], "w").write(json.dumps(m, indent=2, sort_keys=True) + "\n")
PY
rm -f "$globex/index.json.sig"
ssh-keygen -Y sign -f "$globex/.fpa/signing_key" -n foreign-prompts "$globex/index.json" 2>/dev/null
"$tools/fp-verify" --from "$globex" | tail -1
echo "acme's catalog is untouched -- a freshness floor is raised only by the key that set it:"
"$tools/fp-verify" standup --from "$acme" | tail -1 | cut -c1-90

step "7. Someone swaps acme's key at the host -- manifest, signature and published key"
ssh-keygen -q -t ed25519 -N "" -C catalog.acme.example -f "$work/swapped" >/dev/null
printf 'catalog.acme.example %s\n' "$(cat "$work/swapped.pub")" > "$acme/allowed_signers"
rm -f "$acme/index.json.sig"
ssh-keygen -Y sign -f "$work/swapped" -n foreign-prompts "$acme/index.json" 2>/dev/null
expect_refusal "a catalog signed by a key nobody registered" \
  "$tools/fp-resolve" standup --from "$acme" --record

step "To serve a catalog for real"
cat <<'EOF'
The catalog directory is the website. Commit it and serve it byte for byte:
  GitHub Pages     push to a repo, Pages from the branch root; .nojekyll and CNAME are already there
  Cloudflare Pages point it at the repo, no build command, output directory /
  anything static  nginx, S3, R2 -- whatever already serves your files
Then give clients the fingerprint, and keep the manifest fresh (it expires in 30 days):
  fp-index --renew && fp-sign, or .github/workflows/renew.yml with the key as a secret.
EOF
