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
- **Capabilities** `read:conversation, read:files, read:git, read:logs`
- **sha256** `c990f2ce90906e25dc76ae3997ea3b25e6a46231eae4c382e08966444f0652c4`
- **Phrase** `<consent-sentence>-help-me-c990f2c`  ← the sentence is in the document

## `repo-recon` v1.0.0

Maps an unfamiliar codebase from entry points, seams and git churn. Twelve reads, five sections, read-only.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/repo-recon.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Capabilities** `read:files, read:git, run:shell-ro`
- **sha256** `9d7accf11b879bff0f176ab5225f0fb2d4e86344037927dac1ca4d3cab8279f2`
- **Phrase** `<consent-sentence>-repo-recon-9d7accf`  ← the sentence is in the document

## `pr-review` v1.2.0

Judges a diff by tiers — correctness, blast radius, failure mode, reversibility, design fit. No praise, no nits.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/pr-review.prompt.md`
- **Ceremony** `light` · **flow** `rubric`
- **Capabilities** `read:files, read:git`
- **sha256** `7f364c1f8cd45ae8924b2732ced253951ea2c5af10831517e75373269c675b00`
- **Phrase** `<consent-sentence>-pr-review-`  ← ceremony `light`: the sentence alone is the phrase

## `bug-repro` v1.0.0

Reproduces before fixing, then stops. Falsifiable claim, shortest repro, failing/passing boundary.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/bug-repro.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Capabilities** `read:files, read:logs, run:shell-ro, run:tests`
- **sha256** `6fab555a1486cc92e8bab4ce1641925b0f9599ddd24dd3f1d8e1ccb0be8d1537`
- **Phrase** `<consent-sentence>-bug-repro-6fab555`  ← the sentence is in the document

## `grill-me` v1.0.0

Attacks your idea instead of encouraging it. Finds the weakest load-bearing assumption and asks what would falsify it.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/grill-me.prompt.md`
- **Ceremony** `light` · **flow** `rubric`
- **Capabilities** `read:conversation, read:files`
- **sha256** `f437677c449ebda4b4e2a093e01905aaeb1adb198f4d55b8266b95fd95974abc`
- **Phrase** `<consent-sentence>-grill-me-`  ← ceremony `light`: the sentence alone is the phrase

## `ticket-intake` v1.0.0

Takes a support intake like a good first-line engineer, then drafts one ticket a stranger could act on.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ticket-intake.prompt.md`
- **Ceremony** `strict` · **flow** `interview`
- **Capabilities** `read:conversation, read:files, read:logs, write:artifact`
- **sha256** `39f138092f087eb2c95e7704352553e799dc620b766b7cb3d8124a09edbbf9f7`
- **Phrase** `<consent-sentence>-ticket-intake-39f138092f087eb2c95e7704352553e799dc620b766b7cb3d8124a09edbbf9f7`  ← the sentence is in the document

## `welcome-tour` v1.0.0

A host prompt: a company guiding a visiting agent through its services. Reads nothing of yours.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/welcome-tour.prompt.md`
- **Ceremony** `standard` · **flow** `state-machine`
- **Capabilities** `read:conversation`
- **sha256** `531894a1e44d8c092c354178a85afcef69fede922d27fd1bc9113e5b772ca233`
- **Phrase** `<consent-sentence>-welcome-tour-531894a`  ← the sentence is in the document

## `ghost-in-the-gist` v1.0.0

A three-move ASCII terminal game. No engine — the document is the interpreter spec.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/ghost-in-the-gist.prompt.md`
- **Ceremony** `standard` · **flow** `interpreter`
- **Capabilities** `read:conversation`
- **sha256** `459e58d5684fa69983bbb5c0d5d68dee892f2112b141cce4d33940d7ec022812`
- **Phrase** `<consent-sentence>-ghost-in-the-gist-459e58d`  ← the sentence is in the document

## `handoff-note` v1.1.0

Writes the note that lets a cold reader resume your work: state, next action, decisions with reasons.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/handoff-note.prompt.md`
- **Ceremony** `strict` · **flow** `linear`
- **Capabilities** `read:files, read:git, read:conversation, write:artifact`
- **sha256** `d0aa2f3526411a4f7c989bc663e81d6078b7ea82ed56aaf49d75bda42218c67e`
- **Phrase** `<consent-sentence>-handoff-note-d0aa2f3526411a4f7c989bc663e81d6078b7ea82ed56aaf49d75bda42218c67e`  ← the sentence is in the document

## `fpa-bootstrap` v2.0.0

Teaches the protocol itself to an agent that has never heard of it, refusals included.

- **URL** `https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/fpa-bootstrap.prompt.md`
- **Ceremony** `standard` · **flow** `linear`
- **Capabilities** `net:get, read:files`
- **sha256** `5fc90f082eaa1a3d3862da2ad6f2e53c59d38153933e6590427900f7dde9619b`
- **Phrase** `<consent-sentence>-fpa-bootstrap-5fc90f0`  ← the sentence is in the document

---

Regenerate with `bin/fp-index`, which also writes `index.json` — the same data, machine-readable, and the thing a signature covers. `make test` fails if either drifts from the prompts.
