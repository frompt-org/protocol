# Tutorial 4 — run unattended

**You end with:** agents that resolve frompts by id from a catalog you registered once, with no digest
typed — and that refuse anything that does not verify.

## 1. Register the catalog, once

```
bin/fp-register gh:frompt-org/catalog@main --pin latest --trust ./frompt-catalog.allowed_signers
```

`--trust` brings the publisher's key in from a file you obtained yourself. The registration line in
`fpa.registered` records the catalog, the key's fingerprint, the pin mode, when, and who. That line
is the consent.

## 2. Resolve by id

```
bin/fp-resolve pr-review@latest --from gh:frompt-org/catalog@main
```

The manifest is verified first — signature against your key, the registered fingerprint, expiry,
the freshness floor — and only then is the document fetched and checked against the digest it
names.

## 3. Choose how much drift you accept

`--pin latest` floats to each new version. `version` and `digest` require a matching line in
`fpa.lock` (`bin/fp-lock`), so a bump arrives only as a re-pin somebody reviews.

## 4. The managed path

```
bin/fp-verify pr-review --from gh:frompt-org/catalog@main
```

No human at all: a signature authorizes, and anything that cannot be verified fails closed.

## Why each check is there

Ceremony is for a human at a keyboard. Two other contexts have no human at use time, so each replaces the phrase with something an agent can check by itself.

**`registered`** — consent given once, bounded by a pin. `fpa.lock` records id, version, digest and URL; `fp-resolve --lock` refuses bytes that are not the pinned ones:

```
$ bin/fp-resolve pr-review --lock
fp-resolve: pr-review has moved since it was pinned
  pinned  1.2.0 7f364c1f8cd4…
  fetched 6c0aaea5c2f3…
Re-pin deliberately with 'bin/fp-lock --update' if that is what you want.
```

Pinning is not safer than floating by itself. It makes the choice **a line somebody reviews** instead of an event nobody sees.

And the registration itself is recorded, in `fpa.registered` — one line per catalog, the shape `sources.list` has had for thirty years:

```
<base> <signer-fingerprint> <pin-mode> <registered-on> <who>
```

That file is the consent. A lock says what is pinned; it never says anybody agreed to it. Once the file exists, this workspace has opted into the model and `fp-verify` refuses a catalog absent from it — and refuses one whose signing key has changed since it was recorded, which catches a substitution even when the new key is in `allowed_signers`.

**`managed`** — no human at all. `index.json` is a deterministic manifest carrying a monotonic serial, signed with `ssh-keygen -Y`. `fp-verify --from <publisher>` **fetches the manifest and the document from the publisher** and checks both against a trust root held locally:

```
$ bin/fp-verify repo-recon --from https://prompts.example.org
manifest verified: index.json signed by foreign-prompts-publisher
authorized: repo-recon v1.1.0 digest 31c1785acb46 contexts [interactive, registered, managed] serial 6
```

Four things have to hold, and each one closes an attack that the others do not:

- **The manifest expires.** A serial floor is a memory, and a client that has never seen a newer manifest has none — a fresh agent, a wiped store, a clean container. All of them would accept an arbitrarily old signed bundle, and every signature on it verifies. `not_after` needs no memory: a replay dies on its own. This is apt's `Valid-Until`, and the reason WebPKI shortened certificate lifetimes instead of trusting revocation.

- **The trust root is local.** `allowed_signers` is never fetched from the host it is used to check — a signer list taken from the same place as the signature proves only that the two agree with each other.
- **The serial is monotonic.** Every signature on last month's manifest is still perfectly valid, so replaying one is a rollback that needs no key. A client refuses a serial below the highest it has accepted.
- **Digests cover bytes.** Reading a document as text first normalizes line endings, and a CRLF copy then hashes identical to its LF original while differing byte for byte.

**A digest proves the bytes are the bytes you expected; only a signature proves who expected them.** That is why the manifest is signed and the documents are not — one signature covers the set, and revocation is dropping an entry rather than reaching every agent.

The private key never enters the repository. What ships is the manifest, its signature, and the public key: enough to verify, not enough to forge. And `fp-verify` exits 2 — not 0 — when it cannot check at all, because an agent that falls back to an unsigned fetch has turned a policy boundary into a suggestion.

