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
| `fp-init-catalog` | Start a catalog for your own domain: empty, signed, key in `.fpa/`, renew workflow. | `fp-init-catalog <dir> --url <url> [--identity NAME]` |
| `fp-index` | Regenerate INDEX.md and index.json from prompts/, served from the catalog's `url`. | `fp-index [--check] [--renew]` |
| `fp-sign` | Sign index.json with a key that never leaves the machine; print its fingerprint. | `fp-sign [--keygen]` |
| `fp-publish` | Stage frompts into a catalog checkout; refuses to change published bytes. | `fp-publish <catalog> [--only id,id] [--check]` |
| `fp-assay` | Scan a document and record what was seen, as data keyed by digest. | `fp-assay <file> [-o attestations/]` |

## Client and operator

| Tool | Does | Usage |
|---|---|---|
| `fp-register / fp-unregister` | Record, or withdraw, a workspace's consent to a catalog; trust its key by fingerprint. | `fp-register <base> --key SHA256:… [--pin latest|version|digest]` or `--trust <file>` |
| `fp-resolve` | Resolve an id to verified bytes; with --from, only from a verified manifest. | `fp-resolve <id>[@version] [--from <base>] [--lock] [--record]` |
| `fp-verify` | The managed path: signature, registered key, expiry, freshness, digest. | `fp-verify [<id>] [--from <base>] [--context registered|managed]` |
| `fp-lock` | Pin what a team adopts; re-pinning is a reviewed diff. | `fp-lock [--check] [--update <id> [--from <base>]]` |
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

## Where the tools read and write

| Variable | Names | Default |
|---|---|---|
| `FPA_CATALOG` | the **catalog** a publisher signs: `frompt-catalog.json`, `prompts/`, `index.json`, its signature, the published `allowed_signers`, `.fpa/signing_key` | for `fp-index`, `fp-sign` and `fp-publish`: the nearest directory upward holding `frompt-catalog.json`, else the tool checkout. For `fp-resolve`, `fp-lock` and `fp-verify`: the tool checkout, never a directory found on disk |
| `FPA_WORKSPACE` | the **workspace** a client trusts from: `allowed_signers`, `fpa.registered`, `fpa.lock`, `.fpa/` floors, catalog bindings and adoption record | the tool checkout |
| `FPA_SIGNING_KEY` · `FPA_SIGNING_IDENTITY` | the key `fp-sign` uses, and the name it publishes it under | `<catalog>/.fpa/signing_key` · the catalog's `identity` |
| `FPA_VALIDITY_DAYS` | how long a manifest `fp-index` writes stays valid, at most 90 days | the catalog's `validity_days`, else 30 |

These tools trust keys, and in the `managed` context authorities as well (FPA M7b): a manifest
signed under a certificate counts as its authority and principal together, never as a key, so it
does not pass for a catalog bound to a key. `fp-register` refuses a catalog signed under a
certificate, since a registration pins one key.

A catalog is the address it is served from: `fp-verify --from <dir>` checks a catalog only when its
`base` is that directory, and `--from https://…` only when its `base` is that URL. A publisher
checks a checkout of an https catalog with `fp-index --check` and `ssh-keygen -Y verify` against
its own published key ([tutorial 3](../tutorials/03-publish-a-catalog.md)).

A tool that reads a catalog reads one somebody chose: `FPA_CATALOG`, a registration (`--from`), or
the tool checkout. Standing in a directory is not choosing it.

The workspace never defaults to a catalog found on disk: a catalog directory is usually a clone of
someone's repository, and a trust root read out of it would be that publisher vouching for
themselves (FPA.md M7). The rule lives in one place, [`bin/fpa_roots.py`](../../bin/fpa_roots.py).
