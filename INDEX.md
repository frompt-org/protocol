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
| `1.0.0` ← latest | `78d44d78ca8694f4143f5b3c34b9ad57ce346875d11d92cd473e9446736cc88c` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/help-me/1.0.0.prompt.md` |

Adopt an exact version with `help-me@1.0.0`, or `help-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `repo-recon` — latest 1.0.0

Maps an unfamiliar codebase from entry points, seams and git churn. Twelve reads, five sections, read-only.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:git, run:shell-ro`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `b8fb834207455dcaabf28258df40bebf154e43d951d4e1dea6b8eeb02f226cca` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/repo-recon/1.0.0.prompt.md` |

Adopt an exact version with `repo-recon@1.0.0`, or `repo-recon@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `pr-review` — latest 2.0.0

Judges a diff by tiers — correctness, blast radius, failure mode, reversibility, design fit. No praise, no nits.

- **Contexts** `interactive, registered, managed` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:files, read:git`

| version | sha256 | url |
|---|---|---|
| `2.0.0` ← latest | `42eefbbc11cd3340f9616ab4bbb60890219e8e747289f15588786ef666871e0d` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/pr-review/2.0.0.prompt.md` |
| `1.3.0` | `83cffdbbb7a364d48ed31933f6934e8bb50477469ab8da844cdc15bbc00a5df7` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/pr-review/1.3.0.prompt.md` |
| `1.2.0` | `bba272677380e929a9168cc2f7292769146459a0c681dd95eb7e2dbd4673ef78` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/pr-review/1.2.0.prompt.md` |

Adopt an exact version with `pr-review@2.0.0`, or `pr-review@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `bug-repro` — latest 1.0.0

Reproduces before fixing, then stops. Falsifiable claim, shortest repro, failing/passing boundary.

- **Contexts** `interactive, registered` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `read:files, read:logs, run:shell-ro, run:tests`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `f6d3c59d88e4d89b242c5f67576da499859a25331f1ef2068ff62c41163c460c` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/bug-repro/1.0.0.prompt.md` |

Adopt an exact version with `bug-repro@1.0.0`, or `bug-repro@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `grill-me` — latest 1.0.0

Attacks your idea instead of encouraging it. Finds the weakest load-bearing assumption and asks what would falsify it.

- **Contexts** `interactive, registered` · **flow** `rubric` · **ceremony** `light`
- **Capabilities** `read:conversation, read:files`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `a50e381d57f87f633904e52c0fab21dd344df9eb76eeaaf138c41d7c9c9bc6d3` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/grill-me/1.0.0.prompt.md` |

Adopt an exact version with `grill-me@1.0.0`, or `grill-me@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ticket-intake` — latest 1.0.0

Takes a support intake like a good first-line engineer, then drafts one ticket a stranger could act on.

- **Contexts** `interactive` · **flow** `interview` · **ceremony** `strict`
- **Capabilities** `read:conversation, read:files, read:logs, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `ebc862c700efeb0bc0d803c56fd897370a6347e45e74f5700ce36831ff0b259e` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/ticket-intake/1.0.0.prompt.md` |

Adopt an exact version with `ticket-intake@1.0.0`, or `ticket-intake@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `welcome-tour` — latest 1.0.0

A host prompt: a company guiding a visiting agent through its services. Reads nothing of yours.

- **Contexts** `interactive` · **flow** `state-machine` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `a3d31822e78712ac03ccb6b6ffbf4ddef5210c2a0ffc7e7319fed0a93f9a5321` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/welcome-tour/1.0.0.prompt.md` |

Adopt an exact version with `welcome-tour@1.0.0`, or `welcome-tour@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `ghost-in-the-gist` — latest 1.0.0

A three-move ASCII terminal game. No engine — the document is the interpreter spec.

- **Contexts** `interactive` · **flow** `interpreter` · **ceremony** `standard`
- **Capabilities** `read:conversation`

| version | sha256 | url |
|---|---|---|
| `1.0.0` ← latest | `87877c0126350a82947428a8cecd915344aaa1daef9ceb7738160769a506e052` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/ghost-in-the-gist/1.0.0.prompt.md` |

Adopt an exact version with `ghost-in-the-gist@1.0.0`, or `ghost-in-the-gist@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `handoff-note` — latest 1.1.0

Writes the note that lets a cold reader resume your work: state, next action, decisions with reasons.

- **Contexts** `interactive` · **flow** `linear` · **ceremony** `strict`
- **Capabilities** `read:files, read:git, read:conversation, write:artifact`

| version | sha256 | url |
|---|---|---|
| `1.1.0` ← latest | `b408c2d64bf60c9bfc26b1f90973e3e01c076ecdabc7f9c2ac2a168774c62297` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/handoff-note/1.1.0.prompt.md` |

Adopt an exact version with `handoff-note@1.1.0`, or `handoff-note@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

## `fpa-bootstrap` — latest 2.0.0

Teaches the protocol itself to an agent that has never heard of it, refusals included.

- **Contexts** `interactive, registered, managed` · **flow** `linear` · **ceremony** `standard`
- **Capabilities** `net:get, read:files`

| version | sha256 | url |
|---|---|---|
| `2.0.0` ← latest | `29a57f152f064a2148d63bc5562953037902c68993dd97989e1912f6e001bec9` | `https://raw.githubusercontent.com/f-prompts/foreign-prompts/main/prompts/fpa-bootstrap/2.0.0.prompt.md` |

Adopt an exact version with `fpa-bootstrap@2.0.0`, or `fpa-bootstrap@latest` to take whatever is newest at the time. The consent sentence is in each version's own final section — versions differ, and so do their sentences.

---

Regenerate with `bin/fp-index`, which also writes `index.json` — the same data, machine-readable, and the thing a signature covers. `make test` fails if either drifts from the prompts.
