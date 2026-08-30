# Index of foreign prompts

Every prompt in this repo, every published version, and the digest of each one's bytes.

**This index cannot give you a confirmation phrase, by design.** A phrase is a consent
sentence plus an id plus a digest. The digest is here — a document cannot contain its own
hash, so publishing it out of band is the intended route. The consent sentence is *not*:
it lives in each prompt's final `## Consent` section, which you reach by reading the
document. Index plus document gives you a phrase. Index alone does not.

Verify a digest against what you actually fetched:

```
curl -s <url> | shasum -a 256
```

If it disagrees with this table, you and this index are not looking at the same
document. Do not adopt it; open an issue.

---

## `help-me` — latest 1.0.0

Stuck? It interviews your agent about this session, then proposes a route through other prompts. Start here.

- **Contexts** `interactive` · **flow** `interview` · **ceremony** `standard`
- **Capabilities** `read:conversation, read:files, read:git, read:logs`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `7d12fffee3cee9ebef783e18907b0b4ac3391f1fd588e411d59a15d778aed046` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/help-me/1.0.0.prompt.md` |

Adopt an exact version with `help-me@1.0.0`, or `help-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `repo-recon` — latest 1.0.0

Maps an unfamiliar codebase from entry points, seams and git churn. Twelve reads, five sections, read-only.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:git, run:shell-ro`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `0ee1331bb6d7ea6c626c79a6aace0f419c58137cdd3c563f9f795cdc3133f2af` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/repo-recon/1.0.0.prompt.md` |

Adopt an exact version with `repo-recon@1.0.0`, or `repo-recon@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `pr-review` — latest 2.0.0

Judges a diff by tiers — correctness, blast radius, failure mode, reversibility, design fit. No praise, no nits.

- **Contexts** `interactive, registered, managed` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:files, read:git`

| version | sha256 | url |
|---|---|---|
| `2.0.0` ← latest | `ef3c6a79f589e8b2d95027112a0ace4a7aba614f8ad0498648e5d0a71a8cd9b2` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/pr-review/2.0.0.prompt.md` |
| `1.3.0` | `908c1944b00a6f6339a8f7ce9d5913d56b9cdc8469ed44dfed92a7002eb4644c` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/pr-review/1.3.0.prompt.md` |
| `1.2.0` | `2add881744b4b205c2ba6bc5b6beff106951cf629e832b1dc1d0c7f3cc439634` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/pr-review/1.2.0.prompt.md` |

Adopt an exact version with `pr-review@2.0.0`, or `pr-review@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `bug-repro` — latest 1.0.0

Reproduces before fixing, then stops. Falsifiable claim, shortest repro, failing/passing boundary.

- **Contexts** `interactive, registered` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:logs, run:shell-ro, run:tests`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `a1470b3cf3d5b8eaf24f526e71fd8f99fe9998b1927338090dae91d2a9b33247` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/bug-repro/1.0.0.prompt.md` |

Adopt an exact version with `bug-repro@1.0.0`, or `bug-repro@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `grill-me` — latest 1.0.0

Attacks your idea instead of encouraging it. Finds the weakest load-bearing assumption and asks what would falsify it.

- **Contexts** `interactive, registered` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:conversation, read:files`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `d05f1aece953acf0b0ad173e1352129e4fdc76981732c6e62bafae3651f6fcf9` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/grill-me/1.0.0.prompt.md` |

Adopt an exact version with `grill-me@1.0.0`, or `grill-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ticket-intake` — latest 1.0.0

Takes a support intake like a good first-line engineer, then drafts one ticket a stranger could act on.

- **Contexts** `interactive` · **flow** `interview` · **ceremony** `strict`
- **Capabilities** `read:conversation, read:files, read:logs, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `85841d8994c51d861e3858cab7408ed3716642487cc4c264b05adcc3d0cbe492` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ticket-intake/1.0.0.prompt.md` |

Adopt an exact version with `ticket-intake@1.0.0`, or `ticket-intake@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `welcome-tour` — latest 1.0.0

A host prompt: a company guiding a visiting agent through its services. Reads nothing of yours.

- **Contexts** `interactive` · **flow** `state-machine` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `e74c7278104654a7659b90ad4cc5ad8cc2f1cc36f9cbd6a40e04c7d26d91be14` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/welcome-tour/1.0.0.prompt.md` |

Adopt an exact version with `welcome-tour@1.0.0`, or `welcome-tour@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ghost-in-the-gist` — latest 1.0.0

A three-move ASCII terminal game. No engine — the document is the interpreter spec.

- **Contexts** `interactive` · **flow** `interpreter` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `e7558c8b26c93fa3019c24e433ec645619a2efb793a649dbbfda465eaabda5ce` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ghost-in-the-gist/1.0.0.prompt.md` |

Adopt an exact version with `ghost-in-the-gist@1.0.0`, or `ghost-in-the-gist@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `handoff-note` — latest 1.1.0

Writes the note that lets a cold reader resume your work: state, next action, decisions with reasons.

- **Contexts** `interactive` · **flow** `linear` · **ceremony** `strict`
- **Capabilities** `read:files, read:git, read:conversation, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.1.0` ← latest | `7dfb58372543dd20ec5fad68a12089ff162107b771bef6d419ac7929f8c387f3` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/handoff-note/1.1.0.prompt.md` |

Adopt an exact version with `handoff-note@1.1.0`, or `handoff-note@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `fpa-bootstrap` — latest 2.0.0

Teaches the protocol itself to an agent that has never heard of it, refusals included.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `net:get, read:files`

| version | sha256 | url |
|---|---|---|
| `2.0.0` ← latest | `13e520128c3a2be9e4e669022a4546aa2a78a1b89b0ae6fc4f0712019b2aa32f` | `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/fpa-bootstrap/2.0.0.prompt.md` |

Adopt an exact version with `fpa-bootstrap@2.0.0`, or `fpa-bootstrap@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

---

Regenerate with `bin/fp-index`, which also writes `index.json` — the same data, machine-readable, and the thing a signature covers. `make test` fails if either drifts from the prompts.
