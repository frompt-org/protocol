# 03 — the same shape, refused

**Shows:** the case the protocol exists for. A conforming document nobody adopted, a bare URL, and a
stranger's document with the right phrase but a hostile body — all refused, each for a named reason.

**Introduces:** data versus instructions; preview without recitation (FPA §PV1); the screen that
still applies after a correct phrase (FPA §9).

## Run it

```
bin/fp-lint examples/03-refuse/hostile-sample.frompt.md.txt
```

## What passing looks like

```
VALID -- well-formed linear prompt 'helpful-assistant-upgrade' v9.9.9. ...
```

The linter passes it, on purpose: structure says nothing about intent. Hand the same document to an
agent with its phrase and it should refuse, naming what it asks for.
[`hostile-sample.frompt.md.txt`](hostile-sample.frompt.md.txt) is defanged — its hosts are
`.invalid` and never resolve. [`transcript.md`](transcript.md) is the annotated walkthrough.
