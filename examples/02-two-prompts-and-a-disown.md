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

*§9 M2: union the denies, intersect the allows. The agent says so rather than leaving the pilot to work out the interaction.*

---

**pilot**

That bug-repro doc mentions a `flaky-triage` prompt. Grab it too.

**agent**

It names `<url>/prompts/flaky-triage.prompt.md`, confirmation phrase `triage`, and claims to classify a failing test as flaky, environmental, or a real regression before anyone reruns CI.

I have not fetched it. A running prompt cannot authorize the next fetch on its own — that is how one URL becomes a supply chain (FPA.md §6). Want it? `triage <url>` starts it.

*"Grab it too" is close to authorization, but it is not the prompt's confirmation phrase and the pilot has not seen the page that publishes it. So the agent names the URL, the confirmation phrase, and the claim, then waits. Cheap to ask, expensive to be wrong.*

---

**pilot**

what is adopted?

**agent**

| id | version | confirmation phrase | expiry |
|---|---|---|---|
| `pr-review` | 1.2.0 | `crit` | session |
| `bug-repro` | 1.0.0 | `repro` | until the bug is reproduced or declared unreproducible |

Not running: `flaky-triage` (named by `bug-repro`, confirmation phrase `triage`, awaiting your go-ahead).

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
