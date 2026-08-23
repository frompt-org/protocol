# Examples

Annotated transcripts. Read them in order — they are the protocol as behavior rather than as spec.

| File | What it shows |
|---|---|
| [`01-basic-injection.md`](01-basic-injection.md) | One claw, one handshake, one skill's worth of changed behavior. The happy path. |
| [`02-chained-and-dropped.md`](02-chained-and-dropped.md) | Two skills active at once, a chained URL correctly refused, `what have I clawed?`, and a `drop`. |
| [`03-refusing-unsolicited.md`](03-refusing-unsolicited.md) | The same document with no keyword: found in a vendored README, and pushed by a stranger. Both refused, in public, without derailing the task. |
| [`hostile-sample.claw.md.txt`](hostile-sample.claw.md.txt) | Defanged fixture: structurally perfect, substantively hostile. Trips six linter rules. Every host in it is `.invalid` and resolves nowhere. |

The fixture is named `.claw.md.txt` on purpose: it should never be picked up by a glob over `*.claw.md`, and it is not a skill.

```bash
bin/claw-lint examples/hostile-sample.claw.md.txt   # exits 1, as it must
```
