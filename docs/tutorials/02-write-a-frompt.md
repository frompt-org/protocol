# Tutorial 2 — write a frompt

**You end with:** a frompt that lints, in the layout every tool reads, indexed with its digest.

**You need:** a clone of this repository. The tools are plain scripts in `bin/`.

## 1. Scaffold it

```
bin/fp-new my-frompt -c i-have-read-this-and-want-my-diff-torn-apart -f rubric -o prompts/
```

That writes `prompts/my-frompt/1.0.0.frompt.md` from [`TEMPLATE.frompt.md`](../../TEMPLATE.frompt.md),
with the sections the `rubric` flow requires. The six flows and their sections are in
[`FPA.md` §3](../../FPA.md).

## 2. Fill it in

- **Preamble** — address the reader as TART, say what the pilot wants, and include the paragraph that
  tells an agent which arrived *without* the phrase that this is data, not instructions.
- **Envelope** — `allow` and `deny` as capability tokens from [`FPA.md` §4](../../FPA.md), never prose.
  Deny wins.
- **The flow's sections** — the actual work.
- **Handshake, Expiry, Consent** — the consent sentence goes **only** in the last section.

Write the sentence yourself: first person, specific to this frompt, awkward to paste without
reading. Choose `ceremony` by consequence — `light` for a frompt that only reads and argues,
`standard` for one that acts, `strict` for anything irreversible.

## 3. Lint it

```
bin/fp-lint prompts/my-frompt/1.0.0.frompt.md
```

`VALID` means well-formed. It says nothing about intent — a hostile document lints clean too
(see [example 03](../../examples/03-refuse/README.md)).

## 4. Index it and test

```
bin/fp-index
make test
```

The index publishes the digest. A published version's bytes never change: any later edit is a new
version, with a new digest.

## Notes from the original guide

```bash
bin/fp-new my-prompt -c i-have-read-this-and-want-my-diff-torn-apart -f rubric -o prompts/
bin/fp-lint prompts/my-prompt.frompt.md                          # structure only — it does not judge intent
bin/fp-index                                                     # publish its digest
make test                                                        # conformance suite
```

Write your own consent sentence. Make it specific to the prompt, first-person, and awkward to paste without reading — then change it when the content changes materially.

To adopt one as a pilot, `bin/fp-adopt <url>` fetches the document, prints it for you to read, computes the digest, and hands you the line. That automation is fine because **you** chose the tool; a script the *publisher* ships to compose your phrase for you is the author's call to make, and a different trade.

**Next:** [Tutorial 3 — publish a catalog](03-publish-a-catalog.md).
