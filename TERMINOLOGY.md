# Terminology

Canon for this repo. If any other file disagrees with this one, **this one wins** — fix the other file.

## Current

| Term | Meaning |
|---|---|
| **foreign prompt** | A prompt acquired from a non-local source — usually a URL — to be checked, adopted, and run by an agent that did not write it. Prompt injection with the pilot's authorization, declared limits, and a visible handshake. Extension `.prompt.md`, marker `<!-- FOREIGN-PROMPT v1 -->` on line 1. "Foreign" names **origin, never location** — like a foreign key, which lives in your table. |
| **Foreign Prompt Adoption (FPA)** | The protocol in [`FPA.md`](FPA.md): how a foreign prompt is fetched, checked, confirmed, adopted, run, and ended. |
| **consent** | The pilot deliberately choosing *this document*, by typing the phrase it publishes. The point of the protocol, and the only thing it establishes — not comprehension, not safety, not containment. |
| **non-goal** | Something FPA deliberately does not attempt: sandboxing, filtering, detecting hostility, or defending against a publisher the pilot trusted. Listed in [`FPA.md`](FPA.md) §0. Non-goals are not a roadmap. |
| **adoption** | The runtime agent holding a foreign prompt as active instructions for a declared span. The way a committee adopts a resolution — not the way a family adopts a child. |
| **pilot** | Whoever sends commands to the agent. The only party who can authorize an adoption. |
| **runtime agent** | The agent that fetches and runs the foreign prompt. |
| **TART** | *The Agent Reading This.* How a foreign prompt addresses the runtime agent in the second person, since it cannot know which agent will read it. |
| **confirmation phrase** | A phrase chosen by the prompt's author and published on its page. The pilot types it to adopt that prompt. It establishes **explicit consent** — the ask was deliberate and aimed at this document — and not that the pilot read or understood it, since a phrase can be handed to someone. |
| **envelope** | The allow/deny capabilities a prompt declares for itself, as tokens from the fixed §4 vocabulary. Deny always wins. It is a **declaration the agent honours**, and a boundary only where a host maps it onto real permissions. |
| **handshake** | The one exact line — `ADOPTED: <id> v<version>` — the runtime agent emits on adoption, so adoption is never silent. |
| **capability token** | One entry from the fixed vocabulary a prompt's `allow`/`deny` are written in — `read:files`, `run:shell-ro`, `write:artifact`, `net:post`, `secrets:read`, and the rest. Free-form English is not permitted: a capability nothing can compare against can never be enforced. |
| **flow** | The shape of a prompt's work — `linear`, `loop`, `state-machine`, `rubric`, `interpreter`, `interview`. A declared label with conventional sections; advisory, not a gate. |
| **preview** | Reporting what a URL contains without adopting it. Needs no phrase, because reading is not running. |
| **adoption record** | What the runtime agent can report about what it has adopted: id, version, source, phrase, flow, persistence, expiry, files written. |
| **disown** | The pilot's command to end an adoption immediately. `disown <id>`, or *disown everything*, which no prompt may disable. |

## Not our words

- **skill** — an installed, dormant, progressively-disclosed capability belonging to an agent harness. A foreign prompt is none of those. Say *prompt*.
- **prompt injection** — the mechanism: instructions from elsewhere entering an agent's context and steering it. Foreign Prompt Adoption **is** prompt injection, performed on purpose. Say so. What the word alone does not tell you is who authorized it, what bounded it, and whether anyone saw it — which is the whole of this protocol.
- **remote** — reserved for things that actually execute elsewhere. A foreign prompt executes here.
