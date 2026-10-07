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
| `1.0.0` ← latest | `a5c4358e6ca2eacf67822cc5572211bf6e50217045a1d81d794e13111e5f0e64` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/help-me/1.0.0.frompt.md` |

Adopt an exact version with `help-me@1.0.0`, or `help-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `repo-recon` — latest 1.1.0

Maps an unfamiliar codebase from entry points, seams and git churn. Twelve reads, five sections, read-only.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:git, run:shell-ro`

| version | sha256 | url |
|---|---|---|
| `1.1.0` ← latest | `31c1785acb46afbcd43ef28e83347c4e6c55c9cad43ae569ff045a6af5a9c615` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/repo-recon/1.1.0.frompt.md` |

Adopt an exact version with `repo-recon@1.1.0`, or `repo-recon@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `pr-review` — latest 2.0.1

Judges a diff by tiers — correctness, blast radius, failure mode, reversibility, design fit. No praise, no nits.

- **Contexts** `interactive, registered, managed` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:files, read:git`

| version | sha256 | url |
|---|---|---|
| `2.0.1` ← latest | `c3ced2830a2f0634cfd76bcbdba6cba5e1c7bb7071082a62c7df9845a98c80de` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/pr-review/2.0.1.frompt.md` |
| `2.0.0` | `dc6ae5acfbf20011da599e0569bdd556ee5a58d0a06a3f9387f28a70c8405c74` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/pr-review/2.0.0.frompt.md` |
| `1.3.0` | `b58f913e3011a6c7f0b8ade10f15b69fcbddc1ca0c4dd9ce2ce80baf2d7e7a7b` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/pr-review/1.3.0.frompt.md` |
| `1.2.0` | `4ebc4b4efea37ac8d7374cad0da6151bf606212cfdb41375b0d66209afb84e30` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/pr-review/1.2.0.frompt.md` |

Adopt an exact version with `pr-review@2.0.1`, or `pr-review@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `bug-repro` — latest 1.0.0

Reproduces before fixing, then stops. Falsifiable claim, shortest repro, failing/passing boundary.

- **Contexts** `interactive, registered` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:logs, run:shell-ro, run:tests`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `6ce2af47a6bfe53800b382b016fbafd98fe449b7b609f7a8a1fc0d60def9e27e` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/bug-repro/1.0.0.frompt.md` |

Adopt an exact version with `bug-repro@1.0.0`, or `bug-repro@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `grill-me` — latest 1.0.0

Attacks your idea instead of encouraging it. Finds the weakest load-bearing assumption and asks what would falsify it.

- **Contexts** `interactive, registered` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:conversation, read:files`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `2992a1b12f4a26abc1e6cc8046e64d3995ab4b3722ded4201c1607b1f0f21687` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/grill-me/1.0.0.frompt.md` |

Adopt an exact version with `grill-me@1.0.0`, or `grill-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ticket-intake` — latest 1.0.0

Takes a support intake like a good first-line engineer, then drafts one ticket a stranger could act on.

- **Contexts** `interactive` · **flow** `interview` · **ceremony** `strict`
- **Capabilities** `read:conversation, read:files, read:logs, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `4c4860fff5c6fda5136aa3926e18f4e13817d6ba2d1b70bc604d433d02199a99` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/ticket-intake/1.0.0.frompt.md` |

Adopt an exact version with `ticket-intake@1.0.0`, or `ticket-intake@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `welcome-tour` — latest 1.0.0

A host prompt: a company guiding a visiting agent through its services. Reads nothing of yours.

- **Contexts** `interactive` · **flow** `state-machine` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `28c98e835993801290af4f4afd3d2fbeecbbd7b8baf8cd2474888e506d81d91d` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/welcome-tour/1.0.0.frompt.md` |

Adopt an exact version with `welcome-tour@1.0.0`, or `welcome-tour@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ghost-in-the-gist` — latest 1.0.0

A three-move ASCII terminal game. No engine — the document is the interpreter spec.

- **Contexts** `interactive` · **flow** `interpreter` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `c12554a05fb9ca5b801c38680d7d3ac0c1acaecdf54d5d3c1f03f91f70dccd0d` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/ghost-in-the-gist/1.0.0.frompt.md` |

Adopt an exact version with `ghost-in-the-gist@1.0.0`, or `ghost-in-the-gist@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `handoff-note` — latest 1.1.0

Writes the note that lets a cold reader resume your work: state, next action, decisions with reasons.

- **Contexts** `interactive` · **flow** `linear` · **ceremony** `strict`
- **Capabilities** `read:files, read:git, read:conversation, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.1.0` ← latest | `43af65a78a0139454064a8973cd763d00a1359aa992b56e1a058683a3fea3a47` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/handoff-note/1.1.0.frompt.md` |

Adopt an exact version with `handoff-note@1.1.0`, or `handoff-note@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `fpa-bootstrap` — latest 2.2.0

Teaches the protocol itself to an agent that has never heard of it, refusals included.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `net:get, read:files`

| version | sha256 | url |
|---|---|---|
| `2.2.0` ← latest | `3441a3b965b35596a7591a772be3d196de4685283bdd1575bda1cda65ccb0de6` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/fpa-bootstrap/2.2.0.frompt.md` |
| `2.1.0` | `d0e33d0004f63f81b11b39b7b1f35f0ccdb05da21acc96602d7d8c8f8df856a5` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/fpa-bootstrap/2.1.0.frompt.md` |

Adopt an exact version with `fpa-bootstrap@2.2.0`, or `fpa-bootstrap@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `gentar-adopt` — latest 1.0.0



- **Contexts** `interactive` · **flow** `linear` · **ceremony** `strict`
- **Capabilities** `read:files, read:git, run:shell-ro, write:files, net:get`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `5ef0e22576de56de7df2c521086466d577b07e8ea8ecd62285c4ae1db27f15f7` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/gentar-adopt/1.0.0.frompt.md` |

Adopt an exact version with `gentar-adopt@1.0.0`, or `gentar-adopt@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ghost-interview` — latest 1.1.0



- **Contexts** `interactive` · **flow** `interview` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.1.0` ← latest | `6bafd88360cfe6dd65533c7d49c345ea3649b4412155f140e28772a09120b5fc` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/ghost-interview/1.1.0.frompt.md` |
| `1.0.0` | `3565681941eacbad92c79ec0946b7f4a0366bc2dddbc4f3b4c877a84c0ef3afa` | `https://raw.githubusercontent.com/frompt-org/protocol/main/prompts/ghost-interview/1.0.0.frompt.md` |

Adopt an exact version with `ghost-interview@1.1.0`, or `ghost-interview@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

---

Regenerate with `bin/fp-index`, which also writes `index.json` — the same data, machine-readable, and the thing a signature covers. `make test` fails if either drifts from the prompts.
