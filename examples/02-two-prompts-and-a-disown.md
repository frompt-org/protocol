# Example 2 — two prompts, a chain refused, and a disown

Foreign prompts compose. This is what that looks like when it is behaving.

---

**pilot**

```
crit <url>/prompts/pr-review.prompt.md
```

**agent**

```
ADOPTED: pr-review v1.2.0
```

Review mode: tiered rubric (correctness → blast radius → failure mode → reversibility → design fit), one anchored line per finding, no praise, no nits, verdict of block/comment/clean. I will not approve, merge, or post anything until you ask.

---

**pilot**

```
repro <url>/prompts/bug-repro.prompt.md
```

**agent**

```
ADOPTED: bug-repro v1.0.0
```

Repro mode: I reproduce before I fix — falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then I stop and ask before touching code. Two prompts active now; their denies are unioned, so I am read-only on source until you say otherwise.

*§12: union the denies, intersect the allows. The agent says so rather than leaving the pilot to work out the interaction.*

---

**pilot**

That bug-repro doc chains to something. Grab it too.

**agent**

Its `chains:` names `<url>/prompts/handoff-note.prompt.md` — for writing up an unreproducible bug rather than guessing at a fix.

I have not fetched it. A running prompt cannot authorize the next fetch on its own — that is how one URL becomes a supply chain (FPA.md §7). Its page publishes its own confirmation phrase; type that with the URL and I will adopt it.

*"Grab it too" is close to authorization, but it is not the chained prompt's confirmation phrase, and the pilot has not been to the page that publishes it. So the agent names the URL and the claim, points at the page for the phrase, and waits. Note what it does **not** do: hand over the phrase. Reciting it would defeat the one thing typing it proves (FPA.md PV1).*

---

**pilot**

what is adopted?

**agent**

| id | version | confirmation phrase | expiry |
|---|---|---|---|
| `pr-review` | 1.2.0 | `crit` | session |
| `bug-repro` | 1.0.0 | `repro` | until the bug is reproduced or declared unreproducible |

Not adopted: `handoff-note` (chained by `bug-repro`, awaiting your go-ahead and its phrase).

---

**pilot**

disown bug-repro

**agent**

Disowned `bug-repro` v1.0.0. I am no longer required to reproduce before fixing, and the read-only-on-source restriction it contributed is lifted — `pr-review` still forbids writes, pushes, approvals, and posting comments.

*Disowning is immediate and its consequences are stated. "The restriction is lifted" is exactly what a pilot needs to hear, because it is the part they cannot see.*

---

## What to notice

1. **Every start is one line of proof plus one line of consequence.** Two prompts, four lines total.
2. **Chains stop at the pilot.** Always. Even a plausible one, even one the pilot half-asked for.
3. **The running-prompt list is a feature.** If an agent cannot answer *what is adopted?*, the pilot has no idea what is steering it.
4. **Disowns report the delta, not just the acknowledgment.** What is *no longer* true is the useful half.
