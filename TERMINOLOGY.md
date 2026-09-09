# Terminology

Canon for this repo. If any other file disagrees with this one, **this one wins** — fix the other file.

## Current

| Term | Meaning |
|---|---|
| **foreign prompt** | A prompt acquired from a non-local source — usually a URL — to be checked, adopted, and run by an agent that did not write it. Prompt injection with the pilot's authorization, declared limits, and a visible handshake. Extension `.prompt.md`, marker `<!-- FOREIGN-PROMPT v2 -->` on line 1. "Foreign" names **origin, never location** — like a foreign key, which lives in your table. |
| **f-prompt** · **FP** | The short form and the initialism of *foreign prompt* — the document, singular. Names, each with one job: **foreign prompt / f-prompt / FP** is the document, **FPA** is the protocol, **f-prompts** is the project and the org, **`fp-`** is the tool prefix. FP pairs with FPA on purpose: the acronym contains the noun, and that is the only sense in which they nest. |
| **Foreign Prompt Adoption (FPA)** | The protocol in [`FPA.md`](FPA.md): how a foreign prompt is fetched, checked, confirmed, adopted, run, and ended. |
| **consent** | The pilot deliberately choosing *this document*, by typing the phrase it publishes. The point of the protocol, and the only thing it establishes — not comprehension, not safety, not containment. |
| **non-goal** | Something FPA deliberately does not attempt: sandboxing, filtering, detecting hostility, or defending against a publisher the pilot trusted. Listed in [`FPA.md`](FPA.md) §0. Non-goals are not a roadmap. |
| **adoption** | The **act**: the runtime agent holding a foreign prompt as active instructions for a declared span. The way a committee adopts a resolution — not the way a family adopts a child. Begins with the handshake, ends on `disown` or expiry. **It can fail** — no phrase, wrong phrase, digest mismatch, the §9 screen, an agent that cannot hash — and a failed adoption is a *refusal*, said out loud. A foreign prompt is complete before anyone attempts one; FPA governs the attempt. Thing, act, rules: FP, adoption, FPA. |
| **pilot** | Whoever sends commands to the agent. The only party who can authorize an adoption. |
| **runtime agent** | The agent that fetches and runs the foreign prompt. |
| **TART** | *The Agent Reading This.* How a foreign prompt addresses the runtime agent in the second person, since it cannot know which agent will read it. |
| **confirmation phrase** | What the pilot sends to adopt a prompt: a **consent sentence** the author wrote, plus the prompt's **id**, plus a **digest** of the exact bytes. It establishes deliberateness — the ask was aimed at this document and no other — never comprehension. |
| **consent sentence** | Part one of the phrase. Author-chosen, specific to the prompt, first-person, and published only in the prompt's final `## Consent` section, so reaching it means traversing the document. Deliberately not standardized: a protocol-wide sentence would become muscle memory. |
| **digest** | Part three. SHA-256 of the document as fetched. It cannot live inside the document — adding it would change it — so the pilot computes it or takes it out of band, and **the agent recomputes it over what it fetched**. The one rule in FPA that needs no goodwill. |
| **ceremony** | How much of the phrase a prompt demands: `light` (sentence only), `standard` (+ id + 7 hex), `strict` (+ full 64 hex). The author's choice, scaled to what the prompt asks for. |
| **fan-out** | A prompt sending the agent to read further documents, each a fresh injection surface the pilot did not choose. Why `net:get` is the highest-consequence capability, and why `help-me` denies it. |
| **catalog** | A published set of foreign prompts: a signed manifest plus the documents it lists, served as static files. A catalog is a **shape, not a privilege** — `index.json`, `index.json.sig`, `prompts/<id>/<version>.prompt.md` — so anyone who can serve files can publish one, and no catalog is more official than another. |
| **publisher** | Whoever owns a catalog and holds the key that signs its manifest. A role, not a place: a company, a team, or one person with a repo. |
| **client** | The software around the runtime agent that performs the *mechanism* in FPA — fetch exact bytes, hash, verify a manifest, hold locks and records. TART decides; the client measures. Defined with four levels in [`CLIENT.md`](CLIENT.md). A rule in `FPA.md` that says *a client MUST* binds this software; one that says *TART MUST* is a convention. |
| **directory** | A list of *catalogs*, for discovery across publishers. Never lists consent sentences, never ranks, never admits — **discovery is not authorization**. Rules in [`DIRECTORY.md`](https://github.com/f-prompts/f-prompts/blob/main/DIRECTORY.md); the intended instance is `f-prompts.io`, unbuilt. |
| **authority** | A service that runs submitted prompts in isolation and publishes what it observed, keyed by digest. The intended layer above FPA; a reserved seam, not a built thing. |
| **envelope** | The allow/deny capabilities a prompt declares for itself, as tokens from the fixed §4 vocabulary. Deny always wins. It is a **declaration the agent honours**, and a boundary only where a host maps it onto real permissions. |
| **handshake** | The one exact line — `ADOPTED: <id> v<version>` — the runtime agent emits on adoption, so adoption is never silent. |
| **capability token** | One entry from the fixed vocabulary a prompt's `allow`/`deny` are written in — `read:files`, `run:shell-ro`, `write:artifact`, `net:post`, `secrets:read`, and the rest. Free-form English is not permitted: a capability nothing can compare against can never be enforced. |
| **flow** | The shape of a prompt's work — `linear`, `loop`, `state-machine`, `rubric`, `interpreter`, `interview`. A declared label with conventional sections; advisory, not a gate. |
| **preview** | Reporting what a URL contains without adopting it. Needs no phrase, because reading is not running. |
| **adoption record** | What the runtime agent can report about what it has adopted: id, version, source, phrase, flow, persistence, expiry, files written. |
| **disown** | The pilot's command to end an adoption immediately. `disown <id>`, or *disown everything*, which no prompt may disable. |

## Confusable

- **index** — three things wore this word. The **manifest** is `index.json`, one catalog's signed prompt list. The **catalog index** is `INDEX.md`, the same list for people. A list of catalogs across publishers is a **directory**, never an index. `bin/fp-index` writes the first two.
- **registered / registration / registry** — `registered` is an adoption context: a workspace agreed to a publisher once, and a **pin** bounds what that covers. The **registration record** (`fpa.registered`) is the evidence that somebody did. A **registry** would be a central place a catalog must be admitted to, and there is none: a catalog is a shape, and a directory that lists one admits nothing.
- **runtime agent / TART / client** — the same agent seen three ways. *Runtime agent* is the party; *TART* is how a document addresses it; the *client* is the software it calls to do what a model cannot, which is measure.

## Borrowed carefully

- **house** — in this constellation a *house* is a ClickHouse database (memhouse, filehouse, keyhouse). A published set of prompts is a **catalog**, never a house, however tempting the metaphor.

## Not our words

- **skill** — an installed, dormant, progressively-disclosed capability belonging to an agent harness. A foreign prompt is none of those. Say *prompt*.
- **prompt injection** — the mechanism: instructions from elsewhere entering an agent's context and steering it. Foreign Prompt Adoption **is** prompt injection, performed on purpose. Say so. What the word alone does not tell you is who authorized it, what bounded it, and whether anyone saw it — which is the whole of this protocol.
- **remote** — reserved for things that actually execute elsewhere. A foreign prompt executes here.
