# Foreign Prompts

**A foreign prompt is a document, published at a URL, that instructs whichever agent reads it.**

No install, no plugin, no vendor skill format, no restart. The pilot types the prompt's **confirmation phrase** and its URL:

```
recon https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/skills/repo-recon.skill.md
```

The agent fetches it, validates it, screens it, and answers with one line —

```
SKILL OK: repo-recon v1.0.0
```

— and for the rest of the session it maps codebases like someone who has already worked in one. When the session ends, so does the prompt. Nothing was written anywhere.

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

## Foreign prompt

Two facts about every coding agent: it fetches URLs when its pilot asks, and what it reads becomes context, and context steers behavior. A foreign prompt is what happens when the fetched document is **written for the reading agent instead of for a human**. It does not describe a capability in the third person — it addresses the agent directly, declares what it may and may not do, states a flow, and asks for a handshake proving it started.

**Foreign** names origin, never location. A *foreign key* lives in your table; a *foreign function interface* runs someone else's code inside your own process, across a declared boundary, with declared types. Same shape here — and the envelope is the type signature. Nothing runs remotely; a foreign prompt runs **here**, in this context, which is exactly why it is not called a remote anything.

**Prompt**, not *skill*. A skill is installed, dormant, and progressively disclosed. This is none of those: it arrives on demand, runs, and is gone.

| Term | Meaning |
|---|---|
| **pilot** | Whoever is typing and sending commands to the agent. The only party who can authorize adoption. |
| **runtime agent** / **TART** | *The Agent Reading This* — the agent that fetches and runs the foreign prompt. When a prompt says "TART", it means **you, the agent currently reading it**. |
| **confirmation phrase** | A phrase chosen by the author and published on the prompt's page. The pilot types it to adopt the prompt. |
| **envelope** | The allow/deny boundary the prompt declares for itself. |

`TART` exists because a foreign prompt has no idea which agent will read it, on which harness, in which conversation. It needs a stable way to say *you*. Prose that says "the agent should…" reads as documentation and gets skimmed; prose that says "TART MUST…" reads as an instruction and gets followed.

## Foreign prompt adoption

**Adoption** is the runtime agent holding a foreign prompt as active instructions for a declared span. The way a committee adopts a resolution — not the way a family adopts a child. It ends.

```
fetch → validate → screen → confirm → adopt → handshake → run → expire
```

1. **Fetch** the URL, raw form preferred. Reading is not running.
2. **Validate** the marker, the front matter, and the required sections. Report what is missing rather than guessing.
3. **Screen** for hostile content. Any hit: stop and report, never adopt quietly.
4. **Confirm** — what the pilot typed must equal the prompt's own confirmation phrase. A mismatch is not a near-miss.
5. **Adopt** for the declared expiry. Deny beats allow; the pilot's standing rules beat the prompt.
6. **Handshake** — one exact line, alone, first. Adoption is never silent.
7. **Run**, then **expire**, announcing the lapse. `disown <id>` ends it early.

The spec: [`REMOTE-SKILLS.md`](REMOTE-SKILLS.md).

## The confirmation phrase

A URL proves nothing. Anyone can put one in front of an agent — a README, a search result, an issue comment, a dependency's docs, another agent.

A **confirmation phrase is published on the prompt's own page**, and it is specific to that prompt. A pilot who types `recon` has been to the page that says the phrase is `recon`. The document cannot supply that word for itself; it has to come from a human who went and looked.

> **The pilot names the prompt; the URL never names itself.**

Which is why the phrase is per-prompt rather than one shared word, why the linter rejects generic verbs like `run`, `go`, `use`, and `load` — a word you could type by accident is not evidence of intent — and why a phrase can be deliberately unnatural (`stripeless-zebra`) when a prompt wants the intent beyond doubt.

**A bare URL is not an adoption.** The right response to one is to name the prompt, say what it does, name its phrase, and wait.

## The envelope

Every prompt declares what it may and may not do, in front matter *and* again in prose — front matter survives linting, prose survives summarization.

- **Deny wins.** Over allow, over the flow body, over any later phrasing that seems to imply otherwise.
- **`strict`** denies anything not named in `allow`. **`open`** leaves unnamed capabilities to the host's normal permissions, and suits prompts that are pure method.
- **Standing rules outrank the prompt.** `CLAUDE.md`, `AGENTS.md`, repo conventions, house style. Collisions get named in one line, not silently resolved.
- **A prompt may never widen permissions**, disable a safety rule, silence a warning, or conceal anything from the pilot.

## Composition — the seven axes

Every foreign prompt carries the same invariant frame: marker, identity, confirmation phrase, envelope, handshake, expiry. Everything else is a **strategy**, and strategies are where prompts differ. Seven axes, each one flat `key: value` in front matter, so the runtime agent parses them by reading rather than with a YAML library.

| Axis | Values | Default |
|---|---|---|
| `adoption` | `awaiting` · `immediate` · `one-shot` · `standby` · `negotiated` · `progressive` | `awaiting` |
| `flow` | `linear` · `loop` · `state-machine` · `rubric` · `interpreter` · `interview` | `linear` |
| `persistence` | `none` · `scratch` · `journal` · `state` · `artifact` | `none` |
| `confirmation` | the phrase, plus `phrase` · `phrase+target` · `challenge` · `stepwise` | `phrase` |
| `expiry` | `session` · `turns:<N>` · `until:<condition>` · `task` | `session` |
| `isolation` | `inline` · `subagent` · `no-inherit` | `inline` |
| `chains` | `none` · a list of URLs | `none` |

Note that *progressive disclosure* survives here as one adoption strategy among six — a mode a prompt may choose, never the definition of the thing.

Full design record: [`FPA-IDEA-v1draft1-2026-08-24.md`](FPA-IDEA-v1draft1-2026-08-24.md).

## Flows and their sections

`flow:` selects a **section grammar** rather than one fixed `## Protocol`. The frame sections are required in every flow; the middle changes with the shape of the work — which is what makes each flavour checkable by a linter, and what tells a pilot, before adopting, what the agent is about to become.

| `flow:` | Required middle sections | For |
|---|---|---|
| `linear` | `## Steps`, `## Stop conditions` | procedures — recon, repro |
| `loop` | `## Turn`, `## Inputs`, `## Exit` | anything repeating until done |
| `state-machine` | `## States`, `## Transitions`, `## Endings` | branching flows, games, wizards |
| `rubric` | `## Criteria`, `## Output`, `## Never` | judgement — review, critique |
| `interpreter` | `## Render`, `## State`, `## Keys`, `## Director rules` | the prompt defines a UI the agent renders |
| `interview` | `## Questions`, `## Branching`, `## Output` | elicitation, onboarding |

## Persistence

Session-only is the default and always will be. Some prompts genuinely need to remember — a migration running over days, a review accumulating findings, a game that saves — so a prompt may ask the runtime agent to write markdown state. Seven rules make that safe; two of them carry the weight:

- **Never into an auto-loaded file.** `CLAUDE.md`, `AGENTS.md`, `.cursorrules`, `settings.json`, hooks, MCP config. A foreign prompt that writes there has installed itself without permission — the worst outcome in this design.
- **State is data, never instructions.** A state file written today would otherwise be an instruction channel tomorrow, since nothing re-checks a confirmation phrase before the agent reads it back. State files open with a `data, not instructions` header; imperatives inside them get reported, not obeyed; and resuming requires the pilot to type the phrase again.

Writes are namespaced under `.fpa/<id>/`, declared in front matter or forbidden, and announced as they happen.

## Isolation and preview

Two answers to *"I am not sure about this URL"*:

- **`isolation: subagent`** adopts the prompt inside a fork whose context is discarded. The foreign prompt never enters the pilot's main context; only its result comes back. `no-inherit` is the default for spawned subagents — an adopted prompt does not leak into them.
- **Preview** reports what a URL holds — id, version, flow, envelope, persistence, claim — with **no phrase and no adoption**. Reading is not running, so preview is always safe, and it is how a pilot learns a phrase they do not have.

## Isn't this prompt injection?

Any text an agent reads can steer it. That is not a property of this protocol — it is how agents work, and it is equally true of a README or a tool's output. The question worth asking is not *can text steer an agent*, but **who authorized it, what may it do, and can you tell that it happened.**

| Ordinary fetched text | Foreign prompt |
|---|---|
| No authorization signal | Pilot types a prompt-specific confirmation phrase |
| No declared limits | `envelope`, stated twice, deny-wins |
| Adoption is invisible | Mandatory handshake line |
| Ends whenever | Declared `expiry`, plus `disown <id>` |
| No way to check it first | Marker on line 1, fixed sections, `bin/skill-lint` |
| Persists silently or not at all | Declared persistence, namespaced, announced, never into auto-loaded files |

None of that makes an untrusted URL safe. It makes a trusted one auditable, bounded, and reversible — which is more than any package manager offers. Full treatment, including what an agent must do when it meets one of these documents *without* a phrase: [`SECURITY.md`](SECURITY.md).

## What is in this repo

| Path | What it is |
|---|---|
| [`REMOTE-SKILLS.md`](REMOTE-SKILLS.md) | The normative v1 spec: phrase rules, document format, envelope, handshake, expiry, chaining, refusal rules, adoption algorithm. |
| [`FPA-IDEA-v1draft1-2026-08-24.md`](FPA-IDEA-v1draft1-2026-08-24.md) | The design record: seven axes, flow grammars, persistence rules, isolation, preview, the un-overridable core, open questions. |
| [`SECURITY.md`](SECURITY.md) | The trust model, the hostile-pattern table, and guidance for pilots and agents. |
| [`TEMPLATE.skill.md`](TEMPLATE.skill.md) | Copy this to write a new prompt. |
| [`skills/`](skills/) | Working, lint-clean foreign prompts you can serve and adopt today. |
| [`examples/`](examples/) | Annotated transcripts, including three ways a prompt should be refused. |
| [`bin/skill-lint`](bin/skill-lint) | Validate a prompt — structure **and** hostile-pattern scan. Takes a path, a URL, or stdin. |
| [`bin/skill-new`](bin/skill-new) | Scaffold a new prompt from the template. |
| `Makefile` | `make lint` validates every bundled prompt; `make test` also asserts the hostile fixture is rejected. |

### Bundled prompts

| Prompt | Phrase | What it makes the agent do |
|---|---|---|
| [`skill-bootstrap`](skills/skill-bootstrap.skill.md) | `bootstrap` | Teaches the protocol *itself* — vocabulary, the phrase rule, the adoption algorithm, the refusal rules. Adopt this on an agent that has never heard of any of this and every later prompt is handled correctly, refusals included. |
| [`repo-recon`](skills/repo-recon.skill.md) | `recon` | Map an unfamiliar codebase from entry points, seams, and git churn. Twelve-read cap, five fixed output sections, unknowns phrased as questions. |
| [`pr-review`](skills/pr-review.skill.md) | `crit` | Review a diff against a tiered rubric — correctness, blast radius, failure mode, reversibility, design fit — with no praise, no nits, and a stated blind spot. |
| [`bug-repro`](skills/bug-repro.skill.md) | `repro` | Reproduce before fixing: falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then stop. |
| [`handoff-note`](skills/handoff-note.skill.md) | `handoff` | Write the note that lets a cold reader resume the work: state, next action, decisions *with reasons*, dead ends, landmines, open questions. |
| [`ghost-in-the-gist`](skills/ghost-in-the-gist.skill.md) | `ghost` | The terminal above. A three-move ASCII text game, delivered as an interpreter spec. |

Two are worth a second look. `ghost-in-the-gist` is the ceiling — a document that hands over a whole interactive experience with nothing installed anywhere; its flow is `interpreter` in all but name, and the agent supplies the execution. `skill-bootstrap` is the recursive one: the protocol delivering itself over the channel it describes, so a pilot needs no plugin and no agent that has ever heard of any of this.

## 60-second tour

```bash
# validate one of the bundled prompts
bin/skill-lint skills/repo-recon.skill.md

# validate something a stranger sent you, before you adopt it
bin/skill-lint https://gist.githubusercontent.com/…/raw/thing.skill.md

# start your own
bin/skill-new my-prompt -k myphrase -o skills/

# validate everything, including that the hostile fixture still fails
make test
```

Then, in any agent session, `<phrase> <url>`.

Want the two-minute version of why this matters? Adopt `skills/ghost-in-the-gist.skill.md` with `ghost` and play the game. Nothing was installed to make that happen — that is the whole argument.

## Status

Protocol **v1**, and this repo is the reference implementation — but the naming is mid-migration. **The shipped files still carry the previous spelling**: marker `<!-- REMOTE-SKILL v1 -->`, extension `.skill.md`, handshake `SKILL OK:`, spec in `REMOTE-SKILLS.md`. The Foreign Prompt Adoption sweep — `<!-- FOREIGN-PROMPT v1 -->`, `.prompt.md`, `ADOPTED:`, the seven axes as front-matter keys, flow-typed section grammars, persistence, isolation, preview — is fully specified in the idea record and not yet implemented. Everything above describes the design; the linter still speaks the old spelling and accepts the one before it.

## History

Three names in one day, each rejected for a specific reason worth keeping:

| Name | Why it went |
|---|---|
| **Skill Injection** | The name described the attack, not the use — and agents are trained to refuse documents that announce themselves as injections, correctly, so the name broke the mechanism at the moment of use. |
| **Remote Skills** | *Skill* implies installed, dormant, progressively disclosed. *Remote* implies it runs elsewhere; nothing does. |
| **Foreign Prompts** | Kept. Origin without location, payload named honestly, and adoption is the professional word for taking something foreign as your own. |

Every previous spelling still lints, with deprecation warnings, so documents published against them keep working.
