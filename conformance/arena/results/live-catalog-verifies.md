# gentar report — live-catalog-verifies: PASS

| field | value |
|---|---|
| run_id | `gentar-20261007-091741-c290b0` |
| verdict | `pass (exit 0)` |
| subject | `protocol` |
| bench agent | `shell` |
| credentials | `-` |
| sandbox | `gentar-20261007-091741-c290b0` |
| started | `2026-10-07 09:17:41 +0000` |
| written | `2026-10-07 09:17:56 +0000` |

Reproduce: `gentar/run.sh live-catalog-verifies`

## Steps

### 0. pass

```sh
cd "$WORKSPACE_DIR" && bin/fp-register https://raw.githubusercontent.com/frompt-org/catalog/main --pin latest --as arena
```

```
registered https://raw.githubusercontent.com/frompt-org/catalog/main
  key SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
  pin latest, by arena
```

### 1. pass

```sh
cd "$WORKSPACE_DIR" && bin/fp-verify repo-recon --from https://raw.githubusercontent.com/frompt-org/catalog/main > /tmp/live.log 2>&1; rc=$?; cat /tmp/live.log; exit $rc
```

```
manifest verified: index.json signed by frompt-catalog SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
authorized: repo-recon v1.1.0 digest 31c1785acb46 contexts [interactive, registered, managed] serial 7 expires 2026-11-06T08:27:05Z source https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/repo-recon/1.1.0.frompt.md
```

## Assertions (1/1 passed)

| check | result | detail |
|---|---|---|
| `cmd cat /tmp/live.log` | ✅ pass |  |

## Summary

oracle ok: 1/1 assertions passed
