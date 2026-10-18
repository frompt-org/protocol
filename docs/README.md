# Documentation

Start with the tutorials in order. Reach for a guide when you have one job to do. Read a concept
page when you want to know why. Use the reference for every detail.

## Tutorials — learn by doing, in order

| # | Tutorial | You end with |
|---|---|---|
| 1 | [Adopt your first frompt](tutorials/01-adopt-your-first-frompt.md) | an agent that adopted a frompt, said so, and let it go on command |
| 2 | [Write a frompt](tutorials/02-write-a-frompt.md) | a frompt that lints, in the layout every tool reads |
| 3 | [Publish a catalog](tutorials/03-publish-a-catalog.md) | a signed catalog anyone can verify against your key |
| 4 | [Run unattended](tutorials/04-run-unattended.md) | agents resolving by id from a catalog registered once, refusing what does not verify |

## Guides — one job each

| Guide | When you want to |
|---|---|
| [Talk to a ghost](guides/talk-to-a-ghost.md) | address an adopted frompt, your agent, or relay between them |
| [Revoke a version](guides/revoke-a-version.md) | withdraw a published frompt that is wrong |
| [Attest with assay](guides/attest-with-assay.md) | record what a scanner saw about each document, without letting it become a verdict |
| [Keep a catalog fresh](guides/keep-a-catalog-fresh.md) | renew a manifest before clients refuse it |
| [Run the conformance harness](guides/run-conformance.md) | see what real agents actually do with frompts, quickly and locally |
| [Run the arena](guides/run-the-arena.md) | the same questions in disposable microVMs, with verdicts from what is on the machine |
| [Use the Claude Code plugin](guides/use-the-plugin.md) | find, adopt and list frompts from inside Claude Code |

## Concepts — why it is shaped this way

| Page | Explains |
|---|---|
| [Consent, not security](concepts/consent-not-security.md) | what adoption settles, and every way an adopted frompt can still go wrong |
| [Late binding](concepts/late-binding.md) | why a skill should point at a frompt instead of containing it; versions |
| [What a frompt can be](concepts/what-a-frompt-can-be.md) | a method, a rubric, a colleague, a game, a front door |

## Reference

| Document | Covers |
|---|---|
| [`FPA.md`](../FPA.md) | the protocol, normative |
| [`CLIENT.md`](../CLIENT.md) | what the software around an agent must do, in four levels |
| [`SECURITY.md`](../SECURITY.md) | the trust model, and what to look for when you read a frompt |
| [`TERMINOLOGY.md`](../TERMINOLOGY.md) | the vocabulary, and the words that collide |
| [`INDEX.md`](../INDEX.md) | every frompt in this repository, with digests |
| [Tools](reference/tools.md) | every `fp-*` tool by role, with usage and exit codes |
| [Repository layout](reference/layout.md) | where everything lives |

## Examples

[`../examples/`](../examples/README.md), smallest to full: one adoption, two and a disown, refusals, a
recorded game, a recorded ghost interview, and a catalog end to end that `make test` runs.
