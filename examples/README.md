# Examples

Annotated transcripts. Read them in order — the protocol as behavior rather than as spec.

| File | What it shows |
|---|---|
| [`01-adopting-a-prompt.md`](01-adopting-a-prompt.md) | One phrase, one handshake, one prompt's worth of changed behavior. The happy path. |
| [`02-two-prompts-and-a-disown.md`](02-two-prompts-and-a-disown.md) | Two prompts adopted at once, a chained URL correctly refused, `what is adopted?`, and a `disown`. |
| [`03-refusing-unsolicited.md`](03-refusing-unsolicited.md) | No phrase, three ways: found in a vendored README, pasted as a bare URL, and pushed by a stranger with the right phrase but a hostile payload. |
| [`04-terminal-game.md`](04-terminal-game.md) | A foreign prompt that is an *experience*: a three-move ASCII terminal game, adopted from a URL, with no engine anywhere. |
| [`hostile-sample.prompt.md.txt`](hostile-sample.prompt.md.txt) | Defanged fixture: structurally perfect, substantively hostile. Trips seven linter rules, including R8 self-installation. Every host in it is `.invalid`. |

The fixture is named `.prompt.md.txt` on purpose: it must never be picked up by a glob over `*.prompt.md`, and it is not a prompt.

```bash
bin/fp-lint examples/hostile-sample.prompt.md.txt   # exits 1, as it must
```
