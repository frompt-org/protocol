# gentar report — floor-catalog-e2e: PASS

| field | value |
|---|---|
| run_id | `gentar-20261007-091637-5d3d79` |
| verdict | `pass (exit 0)` |
| subject | `protocol` |
| bench agent | `shell` |
| credentials | `-` |
| sandbox | `gentar-20261007-091637-5d3d79` |
| started | `2026-10-07 09:16:37 +0000` |
| written | `2026-10-07 09:17:03 +0000` |

Reproduce: `gentar/run.sh floor-catalog-e2e`

## Steps

### 0. pass

```sh
"$WORKSPACE_DIR/examples/06-catalog-end-to-end/run.sh" > /tmp/e2e.log 2>&1; rc=$?; cat /tmp/e2e.log; exit $rc
```

```
…s
registered /tmp/frompt-e2e-FqlciL/catalog
  key SHA256:af5d1b0s6XdzPlXDpBsxNTySeFiUr2Iuu9IgQnEvk3w
  pin latest, by example

== 5. Resolve by id, no digest typed: verified against the signed manifest first
resolved=hello@latest version=1.0.0 digest=d52bd5cc63b1 source=/tmp/frompt-e2e-FqlciL/catalog/prompts/hello/1.0.0.frompt.md verified=registered

== 6. The managed path: signature, expiry, freshness, digest
manifest verified: index.json signed by example-publisher SHA256:af5d1b0s6XdzPlXDpBsxNTySeFiUr2Iuu9IgQnEvk3w
authorized: hello v1.0.0 digest d52bd5cc63b1 contexts [interactive, registered, managed] serial 1 expires 2026-11-06T09:16:56Z source /tmp/frompt-e2e-FqlciL/catalog/prompts/hello/1.0.0.frompt.md

== 7. Tamper with the published bytes -- the resolver refuses
fp-verify: DIGEST MISMATCH for hello
  manifest d52bd5cc63b16e939509009e7599bd31bbd4a8c02049f0ca37a03421731280bf
  fetched  d782130d613ac731155a7920c8f466cea5bc65b8956b561196ebba8d5e279bc7
  source   /tmp/frompt-e2e-FqlciL/catalog/prompts/hello/1.0.0.frompt.md
Refusing.
fp-resolve: refusing -- /tmp/frompt-e2e-FqlciL/catalog did not pass verification for the registered context (reason above).
refused, as it should be
```

## Assertions (2/2 passed)

| check | result | detail |
|---|---|---|
| `cmd grep -c "verified=registered" /tmp/e2e.log` | ✅ pass |  |
| `cmd tail -1 /tmp/e2e.log` | ✅ pass |  |

## Summary

oracle ok: 2/2 assertions passed
