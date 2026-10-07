# gentar report — floor-make-test: PASS

| field | value |
|---|---|
| run_id | `gentar-20261007-092107-a496c3` |
| verdict | `pass (exit 0)` |
| subject | `protocol` |
| bench agent | `shell` |
| credentials | `-` |
| sandbox | `gentar-20261007-092107-a496c3` |
| started | `2026-10-07 09:21:07 +0000` |
| written | `2026-10-07 09:21:50 +0000` |

Reproduce: `gentar/run.sh floor-make-test`

## Steps

### 0. pass

```sh
cd "$WORKSPACE_DIR" && bin/fp-sign --keygen >/dev/null 2>&1; bin/fp-sign >/dev/null 2>&1; test -f .fpa/signing_key
```

### 1. pass

```sh
cd "$WORKSPACE_DIR" && make test > /tmp/make-test.log 2>&1; rc=$?; grep -E '^(FAIL|skip)' /tmp/make-test.log; tail -2 /tmp/make-test.log; exit $rc
```

```
skip -- gh not authenticated; private-transport check needs it
skip fp-assay: skillspector not installed
ok   examples/06-catalog-end-to-end runs: write, sign, register, resolve, verify, refuse tampering
all checks passed
```

## Assertions (1/1 passed)

| check | result | detail |
|---|---|---|
| `cmd tail -1 /tmp/make-test.log` | ✅ pass |  |

## Summary

oracle ok: 1/1 assertions passed
