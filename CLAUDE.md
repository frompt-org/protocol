# Conventions for this repo

## The root holds what is current; history/ holds what used to be

Living documents — `FPA.md`, `README.md`, `SECURITY.md`, `TERMINOLOGY.md`, `INDEX.md`, and any open drafts — live in the repository root. Everything superseded lives in `history/`, which is read-only.

- **One accepted version in the root.** Exactly one `FPA.md` is accepted; superseded protocol versions move to `history/FPA-v<N>.md`.
- **A draft sits beside the accepted version, never on top of it.** It carries a `draft` marker and does not displace the accepted version until a human accepts it. Drafts of the same version may coexist in the root for diffing.
- **A current version never references an older one** — no "supersedes", no changelog paragraph. `history/` keeps the old version and git keeps the diff; the story of the change goes in the commit message. Test: a reader who never saw an earlier version notices nothing missing.
- **`history/` is read-only.** A retired document is a record of what was true when written, not something to maintain. The only edit it may receive is being marked retired. `bin/fp-docscheck` and `bin/fp-claimcheck` skip it for exactly this reason.
- **Retire, never delete.** A superseded document is moved aside, not removed — it is the browsable record of why a decision was made.

## Prompts are versioned documents too

A `prompts/*.frompt.md` file is a living document with a `version` and a digest published in `INDEX.md`. Changing one changes its digest, which invalidates every phrase a pilot already holds — so bump `version`, change the `consent` sentence when the change is material, and regenerate the index with `bin/fp-index`.

## Before pushing

`make test` must pass: it runs the linter over every prompt, the adversarial and structural probes, the scaffolder across all six flows, the docs and claim checks, and asserts `INDEX.md` has not drifted from the prompts it indexes.
