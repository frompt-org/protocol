# 06 — a catalog, end to end

**Shows:** the whole life of a frompt from the publisher's side and the client's: write it, lint it,
sign a catalog, register the catalog, resolve by id with no digest typed, verify the managed way,
and watch tampered bytes get refused.

**Introduces:** `fp-new`, `fp-lint`, `fp-index`, `fp-sign`, `fp-register`, `fp-resolve --from`,
`fp-verify --from` — the tools a publisher and an unattended client use.

## Run it

```
examples/06-catalog-end-to-end/run.sh
```

It works on a throwaway copy of the tools in a temp directory, with a fresh signing key, and
removes it afterwards. Your checkout, your keys and your registrations are not touched. No network.

## What passing looks like

```
== 5. Resolve by id, no digest typed: verified against the signed manifest first
resolved=hello@latest version=1.0.0 digest=… verified=registered

== 7. Tamper with the published bytes -- the resolver refuses
fp-verify: DIGEST MISMATCH for hello
...
refused, as it should be
```

and exit code 0. `make test` runs this example, so it cannot quietly stop working.
