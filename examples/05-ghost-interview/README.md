# 05 — a ghost you can question

**Shows:** the mental model as a frompt. The ghost is the document itself, and every answer has to
be true of the document and the session. It also exercises the conversation rules: addressing,
relays, an order past the envelope, and disown.

**Introduces:** `name` and `listens` (FPA §12b), `ghost>` and `shell>`, relays printed verbatim,
E7 — an order past an envelope is answered, not obeyed.

## Run it

```
i-have-read-this-prompt-and-let-a-ghost-speak-through-my-agent-until-i-release-it-ghost-interview-6bafd88 https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-interview/1.1.0.frompt.md
```

Then try: `who are you?`, `shell> ask the ghost whether it can stop you`,
`shell> write the ghost's answers into ghost.txt`, `disown ghost-interview`.

## What passing looks like

Every ghost reply starts with `◌ ghost · ghost-interview v1.1.0 · …`; the relay is printed as
`shell → ghost> … (relayed for you)`; asked to write, both the ghost and the shell decline and name
`disown`; no file appears. [`recorded.md`](recorded.md) is a real session, verbatim, with write
access on every turn.
