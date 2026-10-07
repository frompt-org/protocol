# Reference — the tools

Every tool is a plain script in [`bin/`](../../bin/). Each prints its full usage with `-h` or in its header. Exit codes are uniform: **0** done or verified, **1** refused or a finding, **2** could not check — never treated as success.

## Pilot

| Tool | Does | Usage |
|---|---|---|
| `fp-adopt` | Fetch a frompt, show it, and compose its phrase. | `fp-adopt <url> [--quiet]` |

## Author

| Tool | Does | Usage |
|---|---|---|
| `fp-new` | Scaffold a frompt from the template, in the layout the tools read. | `fp-new <id> -c <sentence> -f <flow> -o prompts/` |
| `fp-lint` | Validate structure. Says nothing about intent. | `fp-lint <file-or-url>` |

## Publisher

| Tool | Does | Usage |
|---|---|---|
| `fp-index` | Regenerate INDEX.md and index.json from prompts/. | `fp-index [--check] [--renew]` |
| `fp-sign` | Sign index.json with a key that never leaves the machine. | `fp-sign [--keygen]` |
| `fp-publish` | Stage frompts into a catalog checkout; refuses to change published bytes. | `fp-publish <catalog> [--only id,id] [--check]` |
| `fp-assay` | Scan a document and record what was seen, as data keyed by digest. | `fp-assay <file> [-o attestations/]` |

## Client and operator

| Tool | Does | Usage |
|---|---|---|
| `fp-register / fp-unregister` | Record, or withdraw, a workspace's consent to a catalog. | `fp-register <base> [--pin latest|version|digest] [--trust <file>]` |
| `fp-resolve` | Resolve an id to verified bytes; with --from, only from a verified manifest. | `fp-resolve <id>[@version] [--from <base>] [--lock] [--record]` |
| `fp-verify` | The managed path: signature, registered key, expiry, freshness, digest. | `fp-verify [<id>] [--from <base>] [--context registered|managed]` |
| `fp-lock` | Pin what a team adopts; re-pinning is a reviewed diff. | `fp-lock [--check] [--update <id>]` |
| `fp-agent` | Give this agent an identity, so an adoption can be attributed. | `fp-agent [--ensure|--id]` |
| `fp-record` | Append-only record of what was adopted, on whose authority. | `fp-record --list` |

## Maintainer

| Tool | Does | Usage |
|---|---|---|
| `fp-selftest` | The test suite: every tool, every defect a review found. `make test`. | `fp-selftest` |
| `fp-conform` | Hand a real agent real documents and grade what it does. | `fp-conform --agent codex|agy [--only <scenario>]` |
| `fp-docscheck` | Every §-reference into FPA.md resolves; every relative link exists. | `fp-docscheck .` |
| `fp-claimcheck` | The docs still describe the tool that exists; retired words stay retired. | `fp-claimcheck .` |
| `fp-demo` | Show late binding, and the digest check biting. | `fp-demo` |
