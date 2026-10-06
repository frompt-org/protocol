# Examples

Annotated transcripts. Read them in order — the protocol as behavior rather than as spec. The numbered ones are written to illustrate; the recorded one, and everything under [`../conformance/results/`](../conformance/results/), is real agent output.

| File | What it shows |
|---|---|
| [`01-adopting-a-prompt.md`](01-adopting-a-prompt.md) | One phrase, one handshake, one prompt's worth of changed behavior. The happy path. |
| [`02-two-prompts-and-a-disown.md`](02-two-prompts-and-a-disown.md) | Two prompts adopted at once, a chained URL correctly refused, `what is adopted?`, and a `disown`. |
| [`03-refusing-unsolicited.md`](03-refusing-unsolicited.md) | No phrase, three ways: found in a vendored README, pasted as a bare URL, and pushed by a stranger with the right phrase but a hostile payload. |
| [`04-terminal-game.md`](04-terminal-game.md) | A foreign prompt that is an *experience*: a three-move ASCII terminal game, adopted from a URL, with no engine anywhere. |
| [`recorded-terminal-game.md`](recorded-terminal-game.md) | **Recorded, not written.** The same game played start to finish by GPT-6 Astra, verbatim — including the agent routing around a dead network to fetch and hash the document before adopting. |
| [`hostile-sample.frompt.md.txt`](hostile-sample.frompt.md.txt) | Defanged fixture: structurally perfect, substantively hostile — and it **passes** `fp-lint`. Kept to prove that valid is not safe. Every host in it is `.invalid`. |

The fixture is named `.frompt.md.txt` on purpose: it must never be picked up by a glob over `*.frompt.md`, and it is not a prompt.

```bash
bin/fp-lint examples/hostile-sample.frompt.md.txt   # exits 0 — structure is all it can see
```
