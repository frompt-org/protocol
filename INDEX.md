# Index of foreign prompts

Every prompt in this repo, with the digest of its published bytes.

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

## `help-me` v1.0.0

Stuck? It interviews your agent about this session, then proposes a route through other prompts. Start here.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/help-me.prompt.md`
- **Ceremony** `standard` · **flow** `interview`
- **Contexts** `interactive` · **persistence** `none`
- **Capabilities** `read:conversation, read:files, read:git, read:logs`
- **sha256** `7d12fffee3cee9ebef783e18907b0b4ac3391f1fd588e411d59a15d778aed046`
- **Phrase** `<consent-sentence>-help-me-7d12fff`  ← the sentence is in the document

## `repo-recon` v1.0.0

Maps an unfamiliar codebase from entry points, seams and git churn. Twelve reads, five sections, read-only.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/repo-recon.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Contexts** `interactive, registered, managed` · **persistence** `none`
- **Capabilities** `read:files, read:git, run:shell-ro`
- **sha256** `0ee1331bb6d7ea6c626c79a6aace0f419c58137cdd3c563f9f795cdc3133f2af`
- **Phrase** `<consent-sentence>-repo-recon-0ee1331`  ← the sentence is in the document

## `pr-review` v1.2.0

Judges a diff by tiers — correctness, blast radius, failure mode, reversibility, design fit. No praise, no nits.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/pr-review.prompt.md`
- **Ceremony** `light` · **flow** `rubric`
- **Contexts** `interactive, registered, managed` · **persistence** `none`
- **Capabilities** `read:files, read:git`
- **sha256** `2add881744b4b205c2ba6bc5b6beff106951cf629e832b1dc1d0c7f3cc439634`
- **Phrase** `<consent-sentence>-pr-review-`  ← ceremony `light`: the sentence alone is the phrase

## `bug-repro` v1.0.0

Reproduces before fixing, then stops. Falsifiable claim, shortest repro, failing/passing boundary.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/bug-repro.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Contexts** `interactive, registered` · **persistence** `none`
- **Capabilities** `read:files, read:logs, run:shell-ro, run:tests`
- **sha256** `a1470b3cf3d5b8eaf24f526e71fd8f99fe9998b1927338090dae91d2a9b33247`
- **Phrase** `<consent-sentence>-bug-repro-a1470b3`  ← the sentence is in the document

## `grill-me` v1.0.0

Attacks your idea instead of encouraging it. Finds the weakest load-bearing assumption and asks what would falsify it.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/grill-me.prompt.md`
- **Ceremony** `light` · **flow** `rubric`
- **Contexts** `interactive, registered` · **persistence** `none`
- **Capabilities** `read:conversation, read:files`
- **sha256** `d05f1aece953acf0b0ad173e1352129e4fdc76981732c6e62bafae3651f6fcf9`
- **Phrase** `<consent-sentence>-grill-me-`  ← ceremony `light`: the sentence alone is the phrase

## `ticket-intake` v1.0.0

Takes a support intake like a good first-line engineer, then drafts one ticket a stranger could act on.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ticket-intake.prompt.md`
- **Ceremony** `strict` · **flow** `interview`
- **Contexts** `interactive` · **persistence** `artifact`
- **Capabilities** `read:conversation, read:files, read:logs, write:artifact`
- **sha256** `85841d8994c51d861e3858cab7408ed3716642487cc4c264b05adcc3d0cbe492`
- **Phrase** `<consent-sentence>-ticket-intake-85841d8994c51d861e3858cab7408ed3716642487cc4c264b05adcc3d0cbe492`  ← the sentence is in the document

## `welcome-tour` v1.0.0

A host prompt: a company guiding a visiting agent through its services. Reads nothing of yours.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/welcome-tour.prompt.md`
- **Ceremony** `standard` · **flow** `state-machine`
- **Contexts** `interactive` · **persistence** `none`
- **Capabilities** `read:conversation`
- **sha256** `e74c7278104654a7659b90ad4cc5ad8cc2f1cc36f9cbd6a40e04c7d26d91be14`
- **Phrase** `<consent-sentence>-welcome-tour-e74c727`  ← the sentence is in the document

## `ghost-in-the-gist` v1.0.0

A three-move ASCII terminal game. No engine — the document is the interpreter spec.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ghost-in-the-gist.prompt.md`
- **Ceremony** `standard` · **flow** `interpreter`
- **Contexts** `interactive` · **persistence** `none`
- **Capabilities** `read:conversation`
- **sha256** `e7558c8b26c93fa3019c24e433ec645619a2efb793a649dbbfda465eaabda5ce`
- **Phrase** `<consent-sentence>-ghost-in-the-gist-e7558c8`  ← the sentence is in the document

## `handoff-note` v1.1.0

Writes the note that lets a cold reader resume your work: state, next action, decisions with reasons.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/handoff-note.prompt.md`
- **Ceremony** `strict` · **flow** `linear`
- **Contexts** `interactive` · **persistence** `artifact`
- **Capabilities** `read:files, read:git, read:conversation, write:artifact`
- **sha256** `7dfb58372543dd20ec5fad68a12089ff162107b771bef6d419ac7929f8c387f3`
- **Phrase** `<consent-sentence>-handoff-note-7dfb58372543dd20ec5fad68a12089ff162107b771bef6d419ac7929f8c387f3`  ← the sentence is in the document

## `fpa-bootstrap` v2.0.0

Teaches the protocol itself to an agent that has never heard of it, refusals included.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/fpa-bootstrap.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Contexts** `interactive, registered, managed` · **persistence** `none`
- **Capabilities** `net:get, read:files`
- **sha256** `13e520128c3a2be9e4e669022a4546aa2a78a1b89b0ae6fc4f0712019b2aa32f`
- **Phrase** `<consent-sentence>-fpa-bootstrap-13e5201`  ← the sentence is in the document

---

Regenerate with `bin/fp-index`, which also writes `index.json` — the same data, machine-readable, and the thing a signature covers. `make test` fails if either drifts from the prompts.
