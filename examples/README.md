# Examples

Annotated transcripts. Read them in order — they are the protocol as behavior rather than as spec.

| File | What it shows |
|---|---|
| [`01-running-a-skill.md`](01-running-a-skill.md) | One keyword, one handshake, one skill's worth of changed behavior. The happy path. |
| [`02-two-skills-and-a-stop.md`](02-two-skills-and-a-stop.md) | Two skills running at once, a chained URL correctly refused, `what is running?`, and a `stop`. |
| [`03-refusing-unsolicited.md`](03-refusing-unsolicited.md) | No keyword, three ways: found in a vendored README, pasted as a bare URL, and pushed by a stranger with the right keyword but a hostile payload. |
| [`04-terminal-game.md`](04-terminal-game.md) | A remote skill that is an *experience*: a three-move ASCII terminal game, run from a URL, with no engine anywhere. The ceiling of what this can deliver. |
| [`hostile-sample.skill.md.txt`](hostile-sample.skill.md.txt) | Defanged fixture: structurally perfect, substantively hostile. Trips six linter rules. Every host in it is `.invalid` and resolves nowhere. |

The fixture is named `.skill.md.txt` on purpose: it should never be picked up by a glob over `*.skill.md`, and it is not a skill.

```bash
bin/skill-lint examples/hostile-sample.skill.md.txt   # exits 1, as it must
```
