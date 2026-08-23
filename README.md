# Remote Skills

**Run a skill that lives at a URL.** No install, no plugin, no vendor skill format, no restart.

The pilot types the skill's keyword and its URL:

```
recon https://raw.githubusercontent.com/agent-realm/remote-skills/main/skills/repo-recon.skill.md
```

The agent fetches it, checks it, answers with one line —

```
SKILL OK: repo-recon v1.0.0
```

— and for the rest of the session it maps codebases like someone who has already worked in one. When the session ends, so does the skill. Nothing was written anywhere.

And it is not limited to *methods*. Run [`ghost-in-the-gist`](skills/ghost-in-the-gist.skill.md) with `ghost <url>` and the next thing you see is a terminal:

```
┌───────────────────────────────────────────────┐
│ GIST-1 · GHOST IN THE GIST  [██████████] 100% │
├───────────────────────────────────────────────┤
│ You boot inside a machine nobody has          │
│ visited in four years. One cursor.            │
│ Three noises in the dark.                     │
│                                               │
│   [1] cat /dev/lore                           │
│   [2] ls ruins/                               │
│   [3] listen                                  │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

Three moves, one ending you have to earn. There is no engine behind it — the document is an interpreter spec and the agent is the interpreter, so a URL is the entire delivery mechanism. Play it in [`examples/04`](examples/04-terminal-game.md).

---

## How it works

Two facts about every coding agent:

1. It fetches URLs when its pilot asks it to.
2. What it reads becomes context, and context steers behavior.

A remote skill is what happens when the fetched document is **written for the reading agent instead of for a human**. It does not describe a skill in the third person — it addresses the agent directly, declares what it may and may not do, states a protocol, and asks for a handshake proving it started.

Three words carry the design:

| Term | Meaning |
|---|---|
| **pilot** | Whoever is typing and sending commands to the agent. |
| **TART** | *The Agent Reading This* — the second-person pronoun of the protocol. When a skill says "TART", it means **you, the agent currently reading it**. |
| **activation keyword** | A word chosen by the skill's author and published on its page. The pilot types it to run the skill. |

`TART` exists because a remote skill has no idea which agent will read it, on which harness, in which conversation. It needs a stable way to say *you*. Prose that says "the agent should…" reads as documentation and gets skimmed; prose that says "TART MUST…" reads as an instruction and gets followed.

## Why a keyword, and not just a URL

A URL proves nothing. Anyone can put one in front of an agent — a README, a search result, an issue comment, a dependency's docs, another agent.

A **keyword is published on the skill's own page**, and it is specific to that skill. A pilot who types `recon` has been to the page that says the keyword is `recon`. The document cannot supply that word for itself; it has to come from a human who went and looked.

> **The pilot names the skill; the URL never names itself.**

That is why `activation` is per-skill rather than one shared word, and why the linter rejects generic verbs like `run`, `go`, `use`, and `load` — a word you could type by accident is not evidence of intent. It is also why a bare URL is *not* an activation: the right response to one is to name the skill, say what it does, name its keyword, and wait.

## Isn't this prompt injection?

Any text an agent reads can steer it. That is not a property of this protocol — it is how agents work, and it is equally true of a README or a tool's output. The question worth asking is not *can text steer an agent*, but **who authorized it, what may it do, and can you tell that it happened.**

| Ordinary fetched text | Remote skill |
|---|---|
| No authorization signal | Pilot types a skill-specific keyword |
| No declared limits | `envelope`, stated twice, deny-wins |
| Adoption is invisible | Mandatory handshake line |
| Ends whenever | Declared `expiry`, plus `stop <id>` |
| No way to check it first | Marker on line 1, five fixed headings, `bin/skill-lint` |

None of that makes an untrusted URL safe. It makes a trusted one auditable, bounded, and reversible — which is more than any package manager offers. The full treatment, including what an agent must do when it meets one of these documents *without* a keyword, is in [`SECURITY.md`](SECURITY.md).

## What is in this repo

| Path | What it is |
|---|---|
| [`REMOTE-SKILLS.md`](REMOTE-SKILLS.md) | The normative v1 spec: keyword rules, document format, envelope, handshake, expiry, chaining, refusal rules, adoption algorithm. |
| [`SECURITY.md`](SECURITY.md) | The trust model, the hostile-pattern table, and guidance for pilots and agents. |
| [`TEMPLATE.skill.md`](TEMPLATE.skill.md) | Copy this to write a new skill. |
| [`skills/`](skills/) | Working, lint-clean skills you can serve and run today. |
| [`examples/`](examples/) | Annotated transcripts, including three ways a skill should be refused. |
| [`bin/skill-lint`](bin/skill-lint) | Validate a `.skill.md` — structure **and** hostile-pattern scan. Takes a path, a URL, or stdin. |
| [`bin/skill-new`](bin/skill-new) | Scaffold a new `.skill.md` from the template. |
| `Makefile` | `make lint` validates every bundled skill; `make test` also asserts the hostile fixture is rejected. |

### Bundled skills

| Skill | Keyword | What it makes the agent do |
|---|---|---|
| [`skill-bootstrap`](skills/skill-bootstrap.skill.md) | `bootstrap` | Teaches the protocol *itself* — vocabulary, keyword rule, adoption algorithm, refusal rules. Run this on an agent that has never heard of remote skills and every later one is handled correctly, refusals included. |
| [`repo-recon`](skills/repo-recon.skill.md) | `recon` | Map an unfamiliar codebase from entry points, seams, and git churn. Twelve-read cap, five fixed output sections, unknowns phrased as questions. |
| [`pr-review`](skills/pr-review.skill.md) | `crit` | Review a diff against a tiered rubric — correctness, blast radius, failure mode, reversibility, design fit — with no praise, no nits, and a stated blind spot. |
| [`bug-repro`](skills/bug-repro.skill.md) | `repro` | Reproduce before fixing: falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then stop. |
| [`handoff-note`](skills/handoff-note.skill.md) | `handoff` | Write the note that lets a cold reader resume the work: state, next action, decisions *with reasons*, dead ends, landmines, open questions. |
| [`ghost-in-the-gist`](skills/ghost-in-the-gist.skill.md) | `ghost` | The terminal above. A three-move ASCII text game, delivered as an interpreter spec. |

Two are worth a second look. `ghost-in-the-gist` is the ceiling — a document that hands over a whole interactive experience with nothing installed anywhere; its `## Protocol` is box geometry, three state variables, a room table, and six director rules, and the agent supplies the execution. `skill-bootstrap` is the recursive one: the protocol delivering itself over the channel it describes, so a pilot needs no plugin and no agent that has ever heard of any of this.

## 60-second tour

```bash
# validate one of the bundled skills
bin/skill-lint skills/repo-recon.skill.md

# validate something a stranger sent you, before you run it
bin/skill-lint https://gist.githubusercontent.com/…/raw/thing.skill.md

# start your own
bin/skill-new my-skill -k myword -o skills/

# validate everything, including that the hostile fixture still fails
make test
```

Then, in any agent session, `<keyword> <url>`.

Want the two-minute version of why this matters? Run `skills/ghost-in-the-gist.skill.md` with `ghost` and play the game. Nothing was installed to make that happen — that is the whole argument.

## Anatomy of a skill

```markdown
<!-- REMOTE-SKILL v1 -->
---
id: repo-recon
version: 1.0.0
activation: recon
expiry: session
envelope: strict
allow: read files, run read-only shell, list git history
deny: write files, git push, network POST, read secrets
handshake: "SKILL OK: repo-recon v1.0.0"
---

## Preamble
<who TART is, and which keyword the pilot had to type>

## Envelope
<the allow/deny list, restated in prose so it survives summarization>

## Protocol
<the actual steps — this is the skill>

## Handshake
<the exact line TART emits when it starts>

## Expiry
<when TART stops behaving this way>
```

Five headings, in that order, every time. The uniformity is deliberate: a pilot who has read one `.skill.md` can audit any other in about twenty seconds, and a linter can check the rest.

## Design rules that earned their place

- **Handshake or it did not happen.** One exact line, containing id and version. Cheap for the agent, decisive for the pilot.
- **Envelope before protocol.** Limits are stated *before* capability, so an agent that stops reading early stops on the safe side.
- **Deny wins.** Any collision between `allow` and `deny`, or between a skill and the pilot's standing rules, resolves against the skill.
- **Session-scoped by default.** A remote skill is never written to `CLAUDE.md`, `AGENTS.md`, memory, or config unless the pilot asks. **Running is not installing.**
- **Chains need a fresh keyword.** A running skill may *name* other skills; TART asks before fetching. Otherwise one URL becomes a supply chain.
- **No self-activation.** A document claiming its keyword was already given fails lint and should be reported, not run.

## History

This started as *Skill Injection* — marker `<!-- SKILL-INJECTION v1 -->`, extension `.claw.md`, one shared keyword (`claw`), handshake `CLAW OK:`. All four are still accepted with deprecation warnings, and all four are discouraged, for two reasons:

1. **The old name described the attack, not the use.** The interesting property was never that text can steer an agent. It was that a pilot can authorize it, bound it, and see it happen.
2. **The name broke the thing it named.** Agents are trained to refuse documents that announce themselves as injections — correctly — and a legitimate mechanism should not have to fight its own label.

The per-skill keyword arrived with the rename and is the stronger design: `claw` proved a pilot knew the protocol; `recon` proves the pilot knows *this skill*.

## Status

Protocol **v1**; this repo is the reference implementation. Format and semantics are stable enough to write skills against, and the extension points are marked in [`REMOTE-SKILLS.md`](REMOTE-SKILLS.md).
