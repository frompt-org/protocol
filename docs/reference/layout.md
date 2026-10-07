# Repository layout

| Path | What |
|---|---|
| [`FPA.md`](../../FPA.md) | The protocol, normative. |
| [`CLIENT.md`](../../CLIENT.md) | What a harness implements — mechanism versus convention, four levels, how a level is claimed. |
| [`frompt-org/frompt`](https://github.com/frompt-org/frompt) | The umbrella — homepage, `VISION.md` (the project), `DIRECTORY.md` (discovery). Project documents live there, not here. |
| [`TERMINOLOGY.md`](../../TERMINOLOGY.md) | Canon vocabulary — the words this repo uses, and the ones it refuses. |
| [`SECURITY.md`](../../SECURITY.md) | Trust model, what to look for when you read a prompt, guidance for pilots and agents. |
| [`prompts/`](../../prompts/) · [`TEMPLATE.frompt.md`](../../TEMPLATE.frompt.md) | Working prompts, and the skeleton for a new one. |
| [`examples/`](../../examples/) | Annotated transcripts, plus a defanged hostile fixture. |
| [`INDEX.md`](../../INDEX.md) | Every prompt, with digests. No consent sentences. |
| [`bin/fp-lint`](../../bin/fp-lint) · [`bin/fp-new`](../../bin/fp-new) | Validate structure; scaffold. |
| [`bin/fp-adopt`](../../bin/fp-adopt) · [`bin/fp-index`](../../bin/fp-index) | Pilot-side: read a prompt and compose its phrase; regenerate the index. |
| [`bin/fp-resolve`](../../bin/fp-resolve) · [`bin/fp-demo`](../../bin/fp-demo) | Resolve an id to verified bytes; demonstrate late binding and the digest check. |
| [`bin/fp-lock`](../../bin/fp-lock) · [`fpa.lock`](../../fpa.lock) | Pin what a team adopts, so re-pinning is a reviewed diff. |
| [`bin/fp-sign`](../../bin/fp-sign) · [`bin/fp-verify`](../../bin/fp-verify) · [`index.json`](../../index.json) | Sign the manifest; verify a prompt against it. The managed path. |
| [`.claude/skills/f/`](../../.claude/skills/f/SKILL.md) | The skill that adopts a prompt by id — mode 3, dogfooded. |
| [`plugin/`](../../plugin/) | `/f:find`, `/f:prompt`, `/f:adopted`, and a session-start hook. |
| [`bin/fp-agent`](../../bin/fp-agent) · [`bin/fp-record`](../../bin/fp-record) | Who this agent is; what it has adopted. |
| [`history/`](../../history/) | Retired documents, read-only. What used to be true, kept rather than deleted. |
| [`bin/fp-register`](../../bin/fp-register) · [`bin/fp-unregister`](../../bin/fp-unregister) | Record, or withdraw, a workspace's consent to a catalog: `fpa.registered`. |
| [`bin/fp-publish`](../../bin/fp-publish) | Stage this repo's frompts into a catalog checkout; refuses to change a published version's bytes. |
| [`bin/fp-assay`](../../bin/fp-assay) | Run a scanner over a document and record what it saw, as data keyed by digest. Never a verdict. |
| [`bin/fp-conform`](../../bin/fp-conform) · [`conformance/`](../../conformance/) | Hand a real agent real documents and grade what it does. Results are checked in, misses included. |
| [`bin/fp-selftest`](../../bin/fp-selftest) | Conformance suite — every defect four review rounds found, as an assertion. |
| [`bin/fp-docscheck`](../../bin/fp-docscheck) · [`bin/fp-claimcheck`](../../bin/fp-claimcheck) | References and links resolve; the docs still describe the tool that exists. |

Protocol **v2**. Nothing is published against it yet, so the format is still free to change without a migration path.
