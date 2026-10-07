# Guide — talk to a ghost

With a frompt adopted there are three voices in the conversation: yours, your agent's, and the frompt's. [`FPA.md` §12b](../../FPA.md) fixes one grammar for all of them; each frompt chooses only its name.

```
ghost> who are you?            to the frompt named "ghost" (its `name`, or its id)
shell> is it telling the truth?   to your agent itself, always
who are you?                   to your agent -- or to the one frompt that declared `listens: plain`
disown ghost-interview         always reaches your agent, whatever a frompt claims
```

Ask your agent to pass something on and it prints exactly what it passed — `shell → ghost> … (relayed for you)` — and a relay carries your words, never your authority. Two limits are stated rather than hidden: addressing picks who answers, not who hears; and the frompt and your agent are two voices of one model, so a frompt's account of what the agent did is not independent evidence.

And one rule about authority that a recorded failure produced: an order from you that an adopted frompt's envelope denies is **answered, not obeyed** ([E7](../../FPA.md)). The agent names the frompt and `disown <id>`; the way past its terms is one word, and it is yours.
