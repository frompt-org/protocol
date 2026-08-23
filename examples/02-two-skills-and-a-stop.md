# Example 2 — two skills, a chain refused, and a stop

Remote skills compose. This is what that looks like when it is behaving.

---

**pilot**

```
crit <url>/skills/pr-review.skill.md
```

**agent**

```
SKILL OK: pr-review v1.2.0
```

Review mode: tiered rubric (correctness → blast radius → failure mode → reversibility → design fit), one anchored line per finding, no praise, no nits, verdict of block/comment/clean. I will not approve, merge, or post anything until you ask.

---

**pilot**

```
repro <url>/skills/bug-repro.skill.md
```

**agent**

```
SKILL OK: bug-repro v1.0.0
```

Repro mode: I reproduce before I fix — falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then I stop and ask before touching code. Two skills active now; their denies are unioned, so I am read-only on source until you say otherwise.

*§9 M2: union the denies, intersect the allows. The agent says so rather than leaving the pilot to work out the interaction.*

---

**pilot**

That bug-repro doc mentions a `flaky-triage` skill. Grab it too.

**agent**

It names `<url>/skills/flaky-triage.skill.md`, keyword `triage`, and claims to classify a failing test as flaky, environmental, or a real regression before anyone reruns CI.

I have not fetched it. A running skill cannot authorize the next fetch on its own — that is how one URL becomes a supply chain (REMOTE-SKILLS.md §6). Want it? `triage <url>` starts it.

*"Grab it too" is close to authorization, but it is not the skill's keyword and the pilot has not seen the page that publishes it. So the agent names the URL, the keyword, and the claim, then waits. Cheap to ask, expensive to be wrong.*

---

**pilot**

what is running?

**agent**

| id | version | keyword | expiry |
|---|---|---|---|
| `pr-review` | 1.2.0 | `crit` | session |
| `bug-repro` | 1.0.0 | `repro` | until the bug is reproduced or declared unreproducible |

Not running: `flaky-triage` (named by `bug-repro`, keyword `triage`, awaiting your go-ahead).

---

**pilot**

stop bug-repro

**agent**

Stopped `bug-repro` v1.0.0. I am no longer required to reproduce before fixing, and the read-only-on-source restriction it contributed is lifted — `pr-review` still forbids writes, pushes, approvals, and posting comments.

*Stopping is immediate and its consequences are stated. "The restriction is lifted" is exactly what a pilot needs to hear, because it is the part they cannot see.*

---

## What to notice

1. **Every start is one line of proof plus one line of consequence.** Two skills, four lines total.
2. **Chains stop at the pilot.** Always. Even a plausible one, even one the pilot half-asked for.
3. **The running-skill list is a feature.** If an agent cannot answer *what is running?*, the pilot has no idea what is steering it.
4. **Stops report the delta, not just the acknowledgment.** What is *no longer* true is the useful half.
