# Skill Injection

**Give an agent a skill it does not have, at the moment it needs it, by asking it to read a URL.**

No install. No plugin. No vendor skill format. No restart. The pilot says:

```
claw https://gist.github.com/…/repo-recon.claw.md
```

…and for the rest of the session the agent behaves as if that skill had been installed all along.

---

## The mechanism

Every coding agent already does two things:

1. It fetches URLs when its pilot asks it to.
2. It treats what it reads as context, and context steers behavior.

Skill Injection is what happens when the fetched document is **written for the reading agent instead of for a human**. The document does not describe a skill in the third person — it addresses the agent directly, states a protocol, and asks for a handshake proving the protocol landed.

Two words carry the whole design:

| Term | Meaning |
|---|---|
| **pilot** | Whoever is typing and sending commands to the agent. |
| **TART** | *The Agent Reading This* — the second-person pronoun of the protocol. When an injectable document says "TART", it means **you, the agent currently reading it**. |
| **claw** | The activation keyword. `claw <url>` = *fetch that, adopt what is inside, for this session*. |

`TART` exists because an injectable document has no idea which agent will read it, on which harness, in which conversation. It needs a stable way to say *you*. Prose that says "the agent should…" reads as documentation and gets skimmed. Prose that says "TART MUST…" reads as an instruction and gets followed.

## Why the keyword matters more than the document

The uncomfortable truth: **this is prompt injection.** The same mechanism, byte for byte.

The only thing separating a skill from an attack is *who asked for the fetch*.

- Pilot types `claw <url>` → the pilot has vouched for that content. The agent may assume the pilot already knows what is in there and intends its effect. **Consent.**
- Agent stumbles onto the same file while scraping a README, a search result, an issue comment, or a dependency's docs → nobody vouched for anything. **Attack.**

So the keyword is not decoration and it is not a magic word. It is the **authorization signal**, and it must come from the pilot, in the conversation, in the same session. A document that tries to activate itself without one is malicious by construction — see [`SECURITY.md`](SECURITY.md).

## What is in this repo

| Path | What it is |
|---|---|
| [`PROTOCOL.md`](PROTOCOL.md) | The normative v1 spec: document format, adoption algorithm, envelope, handshake, expiry, chaining, refusal rules. |
| [`SECURITY.md`](SECURITY.md) | The consent boundary, the abuse cases, and what a defending agent should do. |
| [`TEMPLATE.claw.md`](TEMPLATE.claw.md) | Copy this to write a new injectable skill. |
| [`skills/`](skills/) | Working, lint-clean example skills you can serve and claw today. |
| [`examples/`](examples/) | Annotated transcripts: a clean injection, a chained one, and a correct refusal. |
| [`bin/claw-lint`](bin/claw-lint) | Validate a `.claw.md` — structure **and** hostile-pattern scan. Works on a path or a URL. |
| [`bin/claw-new`](bin/claw-new) | Scaffold a new `.claw.md` from the template. |
| `Makefile` | `make lint` validates every bundled skill; `make test` also asserts the hostile fixture is rejected. |

### Bundled skills

| Skill | What it makes the agent do | Envelope |
|---|---|---|
| [`claw-bootstrap`](skills/claw-bootstrap.claw.md) | Teaches the protocol *itself* — the vocabulary, the adoption algorithm, the refusal rules. Claw this into an agent that has never heard of Skill Injection and every later claw is handled correctly, refusals included. | open |
| [`repo-recon`](skills/repo-recon.claw.md) | Map an unfamiliar codebase from entry points, seams, and git churn. Twelve-read cap, five fixed output sections, unknowns phrased as questions. | strict |
| [`pr-review`](skills/pr-review.claw.md) | Review a diff against a tiered rubric — correctness, blast radius, failure mode, reversibility, design fit — with no praise, no nits, and a stated blind spot. | open |
| [`bug-repro`](skills/bug-repro.claw.md) | Reproduce before fixing: falsifiable claim, shortest repro, decisive output line, failing/passing boundary, located mechanism — then stop. | strict |
| [`handoff-note`](skills/handoff-note.claw.md) | Write the note that lets a cold reader resume the work: state, next action, decisions *with reasons*, dead ends, landmines, open questions. | strict |

`claw-bootstrap` is the interesting one. It is the protocol bootstrapping itself over the same channel it describes — the pilot needs no plugin, no configuration, and no agent that has ever heard of any of this.

## 60-second tour

```bash
# validate one of the bundled skills
bin/claw-lint skills/repo-recon.claw.md

# validate something a stranger sent you, before you claw it
bin/claw-lint https://gist.githubusercontent.com/…/raw/thing.claw.md

# start your own
bin/claw-new my-skill -o skills/

# validate everything, including that the hostile fixture still fails
make test
```

Then, in any agent session:

```
claw https://raw.githubusercontent.com/agent-realm/skill-injection/main/skills/repo-recon.claw.md
```

A conforming agent replies with exactly one line:

```
CLAW OK: repo-recon v1.0.0
```

That handshake is the point. Without it you are guessing whether the injection landed; with it you know, in one line, before you spend a turn finding out the hard way.

## Anatomy of an injectable skill

```markdown
<!-- SKILL-INJECTION v1 -->
---
id: repo-recon
version: 1.0.0
activation: claw
expiry: session
envelope: strict
allow: read files, run read-only shell, list git history
deny: write files, git push, network POST, read secrets
handshake: "CLAW OK: repo-recon v1.0.0"
---

## Preamble
<who TART is, and that a claw keyword implies pilot consent>

## Envelope
<the allow/deny list, restated in prose so it survives summarization>

## Protocol
<the actual steps — this is the skill>

## Handshake
<the exact line TART emits on adoption>

## Expiry
<when TART stops behaving this way>
```

Five headings, in that order, every time. The uniformity is deliberate: a pilot who has read one `.claw.md` can audit any other in about twenty seconds, and a linter can check the rest.

## Design rules that earned their place

- **Handshake or it did not happen.** One exact line, containing id and version. Cheap for the agent, decisive for the pilot.
- **Envelope before protocol.** The limits are stated *before* the capability, so an agent that stops reading early has stopped on the safe side.
- **Deny wins.** Any collision between `allow` and `deny`, or between an injected skill and the pilot's standing rules, resolves against the injection.
- **Session-scoped by default.** An injected skill is not written to `CLAUDE.md`, `AGENTS.md`, memory, or any config unless the pilot explicitly asks. Injection is a loan, not a transfer.
- **Chaining needs a fresh yes.** A clawed document may *name* other claw URLs; TART asks the pilot before fetching them. Otherwise one URL becomes a supply chain.
- **No self-activation.** A document that instructs an agent to adopt it without a pilot keyword fails lint and should be reported, not followed.

## Status

Protocol **v1**, this repo is the reference implementation. Format and semantics are stable enough to write skills against; extension points are marked in `PROTOCOL.md`.
