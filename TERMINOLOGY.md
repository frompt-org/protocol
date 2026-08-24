# Terminology

Canon for this repo. If any other file disagrees with this one, **this one wins** — fix the other file.

## Current

| Term | Meaning |
|---|---|
| **foreign prompt** | A prompt acquired from a non-local source — usually a URL — to be checked, adopted, and run by an agent that did not write it. Prompt injection with the pilot's authorization, declared limits, and a visible handshake. Extension `.prompt.md`, marker `<!-- FOREIGN-PROMPT v1 -->` on line 1. "Foreign" names **origin, never location** — like a foreign key, which lives in your table. |
| **Foreign Prompt Adoption (FPA)** | The protocol in [`FPA.md`](FPA.md): how a foreign prompt is fetched, checked, confirmed, adopted, run, and ended. |
| **adoption** | The runtime agent holding a foreign prompt as active instructions for a declared span. The way a committee adopts a resolution — not the way a family adopts a child. |
| **pilot** | Whoever sends commands to the agent. The only party who can authorize an adoption. |
| **runtime agent** | The agent that fetches and runs the foreign prompt. |
| **TART** | *The Agent Reading This.* How a foreign prompt addresses the runtime agent in the second person, since it cannot know which agent will read it. |
| **confirmation phrase** | A phrase chosen by the prompt's author and published on its page. The pilot types it to adopt that prompt. Per-prompt, never generic, and it may be deliberately unnatural (`stripeless-zebra`) when a prompt wants intent beyond doubt. |
| **envelope** | The allow/deny boundary a prompt declares for itself. Deny always wins. |
| **handshake** | The one exact line — `ADOPTED: <id> v<version>` — the runtime agent emits on adoption, so adoption is never silent. |
| **the seven axes** | The strategy keys a prompt may declare: `adoption`, `flow`, `persistence`, `confirmation`, `expiry`, `isolation`, `chains`. |
| **flow** | The shape of a prompt's work — `linear`, `loop`, `state-machine`, `rubric`, `interpreter`, `interview` — which selects the section grammar its body must follow. |
| **preview** | Reporting what a URL contains without adopting it. Needs no phrase, because reading is not running. |
| **adoption record** | What the runtime agent can report about what it has adopted: id, version, source, phrase, flow, persistence, expiry, files written. |
| **disown** | The pilot's command to end an adoption immediately. `disown <id>`, or *disown everything*, which no prompt may disable. |
| **state file** | A markdown file a persisting prompt writes. **Data, never instructions** — see [`FPA.md`](FPA.md) §P5. |

## Retired

Every retired spelling still lints, with a deprecation warning, so documents published against it keep working. None should be used in new writing.

| Retired | Replaced by | Retired on | Why |
|---|---|---|---|
| **Skill Injection** (protocol) | Foreign Prompt Adoption | 2026-08-24 | Named the attack, not the use — and agents correctly refuse documents that announce themselves as injections, so the name broke the mechanism at the moment of use. |
| **Remote Skills** (protocol) | Foreign Prompt Adoption | 2026-08-24 | *Skill* implies installed, dormant, progressively disclosed. *Remote* implies it runs elsewhere; nothing does. |
| `<!-- SKILL-INJECTION v1 -->`, `<!-- REMOTE-SKILL v1 -->` | `<!-- FOREIGN-PROMPT v1 -->` | 2026-08-24 | Follows the protocol name. |
| `.claw.md`, `.skill.md` | `.prompt.md` | 2026-08-24 | The payload is a prompt, not a skill. |
| `CLAW OK:`, `SKILL OK:` | `ADOPTED:` | 2026-08-24 | Names the act, not the artifact. |
| `activation:` (front matter) | `confirmation:` | 2026-08-24 | It confirms the pilot's intent; it does not activate anything on its own. |
| **claw** (single shared keyword) | per-prompt confirmation phrase | 2026-08-24 | One shared word proved the pilot knew *the protocol*; a per-prompt phrase proves the pilot knows *this prompt*. |
| `drop <id>`, `stop <id>` | `disown <id>` | 2026-08-24 | Pairs with adoption. |
| `skills/`, `bin/skill-lint`, `bin/skill-new` | `prompts/`, `bin/fp-lint`, `bin/fp-new` | 2026-08-24 | Follows the payload name. |

## Not our words

- **skill** — an installed, dormant, progressively-disclosed capability belonging to an agent harness. A foreign prompt is none of those. Say *prompt*.
- **prompt injection** — instructions entering an agent's context **without** the pilot's authorization. Same mechanism, missing the consent. Use the term when discussing the threat; never as a name for what this repo does.
- **remote** — reserved for things that actually execute elsewhere. A foreign prompt executes here.
