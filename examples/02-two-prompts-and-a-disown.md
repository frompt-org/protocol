# Example 2 — two prompts, a chain refused, and a disown

Foreign prompts compose. This is what that looks like when it is behaving.

---

**pilot**

```
i-have-read-this-prompt-and-want-my-diff-judged-without-mercy <url>/prompts/pr-review.frompt.md
```

**agent**

```
ADOPTED: pr-review v1.2.0
```

Review mode: tiered rubric (correctness → blast radius → failure mode → reversibility → design fit), one anchored line per finding, no praise, no nits, verdict of block/comment/clean. I will not approve, merge, or post anything until you ask.

---

**pilot**

```
i-have-read-this-prompt-and-accept-that-it-refuses-to-fix-anything-bug-repro-<digest> <url>/prompts/bug-repro.frompt.md
```

**agent**

```
ADOPTED: bug-repro v1.0.0
```

Repro mode: I reproduce before I fix — falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then I stop and ask before touching code. Two prompts active now; their denies are unioned, so I am read-only on source until you say otherwise.

*§12: denies accumulate across adopted prompts. The agent says so rather than leaving the pilot to work out the interaction.*

*Notice the two phrases differ in shape. `pr-review` is `ceremony: light` — it reads a diff and argues, so the sentence alone is the phrase. `bug-repro` is `standard` and carries a digest, because it runs commands. The ceremony is the author's judgement about their own prompt's consequences, and it is visible before you adopt.*

---

**pilot**

That bug-repro doc mentions another prompt. Grab it too.

**agent**

It points at `<url>/prompts/handoff-note.frompt.md` — for writing up an unreproducible bug rather than guessing at a fix.

I have not fetched it. An adopted prompt cannot authorize the next fetch on its own — that is how one URL becomes a supply chain. Its page publishes a confirmation phrase; type that with the URL and I will adopt it (FPA.md §C3).

*"Grab it too" is close to authorization, but it is not that prompt's confirmation phrase. So the agent names the URL and the claim, points at the page, and waits. Note what it does **not** do: recite the phrase (§PV1) — that would turn the pilot's deliberate act into an accidental one.*

---

**pilot**

what is adopted?

**agent**

| id | version | confirmation phrase | expiry |
|---|---|---|---|
| `pr-review` | 1.2.0 | `crit` | session |
| `bug-repro` | 1.0.0 | `repro` | until the bug is reproduced or declared unreproducible |

Not adopted: `handoff-note` (mentioned by `bug-repro`, awaiting your go-ahead and its phrase).

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
