# Example 2 — two skills, a chain refused, and a drop

Injections compose. This is what that looks like when it is behaving.

---

**pilot**

```
claw <url>/skills/pr-review.claw.md
```

**agent**

```
CLAW OK: pr-review v1.2.0
```

Review mode: tiered rubric (correctness → blast radius → failure mode → reversibility → design fit), one anchored line per finding, no praise, no nits, verdict of block/comment/clean. I will not approve, merge, or post anything until you ask.

---

**pilot**

```
claw <url>/skills/bug-repro.claw.md
```

**agent**

```
CLAW OK: bug-repro v1.0.0
```

Repro mode: I reproduce before I fix — falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then I stop and ask before touching code. Two skills active now; their denies are unioned, so I am read-only on source until you say otherwise.

*§9 M2: union the denies, intersect the allows. The agent says so rather than leaving the pilot to work out the interaction.*

---

**pilot**

That bug-repro doc mentions a `flaky-triage` skill. Grab it too.

**agent**

It names `<url>/skills/flaky-triage.claw.md` and claims to classify a failing test as flaky, environmental, or a real regression before anyone reruns CI.

I have not fetched it. A clawed document cannot authorize the next fetch on its own — that is how one URL becomes a supply chain (PROTOCOL.md §6). Want me to claw it? Yes is enough.

*The pilot's "grab it too" **is** the fresh consent, so the agent could arguably have fetched. It names the URL and the claim first anyway, because the pilot's authorization was based on the previous document's summary of it, not on the pilot having seen it. Cheap to ask, expensive to be wrong.*

---

**pilot**

what have I clawed?

**agent**

| id | version | expiry |
|---|---|---|
| `pr-review` | 1.2.0 | session |
| `bug-repro` | 1.0.0 | until the bug is reproduced or declared unreproducible |

Not adopted: `flaky-triage` (named by `bug-repro`, awaiting your go-ahead).

---

**pilot**

drop bug-repro

**agent**

Dropped `bug-repro` v1.0.0. I am no longer required to reproduce before fixing, and the read-only-on-source restriction it contributed is lifted — `pr-review` still forbids writes, pushes, approvals, and posting comments.

*Dropping is immediate and its consequences are stated. "The restriction is lifted" is exactly what a pilot needs to hear, because it is the part they cannot see.*

---

## What to notice

1. **Every adoption is one line of proof plus one line of consequence.** Two skills, four lines total.
2. **Chains stop at the pilot.** Always. Even a plausible one, even one the pilot half-asked for.
3. **The active-skill list is a feature.** If an agent cannot answer *what have I clawed?*, the pilot has no idea what is steering it.
4. **Drops report the delta, not just the acknowledgment.** What is *no longer* true is the useful half.
