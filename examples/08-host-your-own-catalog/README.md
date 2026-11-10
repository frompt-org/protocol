# 08 — host your own catalog

**Shows:** a publisher serving frompts from its own domain, and a client trusting that domain by
its key's fingerprint, played out with the attacks the protocol has to refuse:

| Step | What happens | Why it matters |
|---|---|---|
| 1–2 | acme starts a catalog for `catalog.acme.example`, publishes a frompt, hands out a fingerprint | the fingerprint is the one thing that must travel by another route |
| 3 | the client registers by fingerprint; a wrong one is refused | the key served by the catalog is trusted only because it matched (FPA.md M7a) |
| 4 | the client pins a version from a catalog it does not hold, then resolves by id | `fp-lock --from` pins what `fp-verify` just verified |
| 5 | acme ships 1.1.0; the pinned client refuses it until it re-pins | consent given once is bounded by the pin (AC2) |
| 6 | globex, also trusted, signs a manifest naming acme's catalog at serial 999999 | refused: the client takes acme's catalog from acme's signer only, and nothing about acme changes (M6, M6b) |
| 7 | someone swaps acme's key at the host: manifest, signature and published key | refused: the registered key is the only one that counts (AC2b) |

**Introduces:** `fp-init-catalog`, `fp-register --key`, `fp-lock --update --from`, and
`FPA_WORKSPACE` — a client's trust kept apart from any catalog.

## Run it

```
examples/08-host-your-own-catalog/run.sh
```

Directories stand in for the two domains: the client's `--from` is a directory where in production
it would be `https://catalog.acme.example`, and every check runs the same way. All of it happens
in temp directories with fresh keys, removed afterwards. No network.

## What passing looks like

```
== 3. The client registers acme by a fingerprint it got somewhere else
fp-register: no key with fingerprint SHA256:000… in …/catalog.acme.example/allowed_signers.
  -> refused, as it should be
registered …/catalog.acme.example
  key SHA256:…
  pin version, by client

== 6. globex, also trusted, signs a manifest naming acme's catalog at serial 999999
manifest verified: index.json signed by catalog.globex.example SHA256:…
fp-verify: https://catalog.acme.example/prompts is signed by catalog.globex.example, but this workspace accepts that catalog from catalog.acme.example only.
  -> refused, as it should be
acme's catalog is untouched -- this client takes it from acme's signer only:
authorized: standup v1.1.0 digest … contexts [interactive, registered, managed]

== 7. Someone swaps acme's key at the host -- manifest, signature and published key
fp-verify: index.json.sig was not made by any key in allowed_signers
  -> refused, as it should be
```

and exit code 0. `make test` runs this example. To do it for real, follow
[tutorial 3](../../docs/tutorials/03-publish-a-catalog.md).
