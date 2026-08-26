# Foreign Prompts

**A foreign prompt is a prompt acquired from a non-local source — usually a URL — to be checked, adopted, and run by an agent that did not write it.**

Say the quiet part first: **this is prompt injection.** Same mechanism, byte for byte — text written by a stranger enters an agent's context and steers what it does. Nothing here pretends otherwise.

**You cannot stop that. You can decide whose.**

Every LLM agent is injectable; that is the substrate, not a flaw this introduces. A README, a search result, an issue comment, a tool's output — all of it can steer an agent, and none of it asked your permission. So the question is not *how do we keep instructions out*, which nobody can answer. It is:

> **Whose instructions got in, and did you choose them?**

A foreign prompt is injection you chose. The pilot names one specific document with a phrase only that document publishes; the document declares up front what it intends; the agent announces that it started; and it ends. Instructions arrive **on purpose instead of by accident** — that is the entire proposition, and it is not a security claim.

| Injection that just happens to you | A foreign prompt |
|---|---|
| Arrives from anywhere the agent reads | Arrives because you named a document |
| Declares nothing | `flow`, `envelope`, `persistence`, `expiry`, machine-readable |
| Silent | A handshake line, every time |
| Ends whenever | A declared end, and `disown <id>` |
| No way to look first | A fixed frame, and a linter for its structure |

That is **agency, not security** — you know what got in, you chose it, you can end it. The trust model is `curl example.com | bash`: you are trusting the publisher, deliberately rather than unknowingly. What the protocol explicitly does **not** attempt is in [`FPA.md` §0](FPA.md) — those are non-goals, not a roadmap.

```
recon https://raw.githubusercontent.com/agent-realm/foreign-prompts/main/prompts/repo-recon.prompt.md
```
```
ADOPTED: repo-recon v1.0.0
Recon mode: I map a repo from entry points, seams, and git churn, cap myself at
twelve file reads, and report in five fixed sections. Read-only.
```

No install, no plugin, no config, no restart. When the session ends, so does the prompt — nothing was written anywhere.

Those URLs are live: every prompt in this repo is fetchable as raw text, which is the entire distribution mechanism. Pin to a commit when you care what you are adopting —
`https://raw.githubusercontent.com/agent-realm/foreign-prompts/8f20b7c…/prompts/repo-recon.prompt.md` — because `main` can change under you and a commit cannot.

## What it is

Every agent already fetches URLs on request, and what it reads steers it. A foreign prompt is what happens when the fetched document is **written for the reading agent instead of for a human**: it addresses the agent directly, declares what it may and may not do, states its flow, and asks for a handshake proving it started.

- **Foreign** = origin, never location. Like a *foreign key*, which lives in your table. It is acquired from elsewhere and runs **here**, in this context.
- **Prompt**, not *skill* — a skill is installed, dormant, progressively disclosed. This arrives on demand and is gone at the end.
- **Adoption** = holding it as active instructions for a declared span. The way a committee adopts a resolution, not the way a family adopts a child.

Vocabulary is canon in [`TERMINOLOGY.md`](TERMINOLOGY.md); the protocol is [`FPA.md`](FPA.md).

## How it works

The pilot sends a **confirmation phrase** with the URL. The phrase is built from up to three parts, and each part proves a different thing:

```
i-have-read-this-prompt-and-let-it-map-my-repository-read-only-repo-recon-8b060ea  <url>
└──────────────── 1. consent sentence ─────────────────────────┘ └── 2. id ──┘ └3. digest┘
```

| Part | Where it comes from | What it establishes |
|---|---|---|
| **consent sentence** | written by the author, published **only in the document's last section** | the pilot reached the end of the document and read a sentence saying what they are about to do |
| **prompt id** | the document's `id` | *this* prompt, not another |
| **digest** | **computed** — a document cannot contain its own hash | the pilot possessed these exact bytes |

Three properties fall out of that, and they are the whole design:

1. **It cannot be guessed.** The sentence is specific to this prompt and deliberately not standardized — a protocol-wide sentence would become muscle memory, and muscle memory is what ceremony exists to prevent.
2. **It cannot be pasted innocently.** You are typing a first-person sentence stating what you are agreeing to. Pasting that without reading should feel wrong, the way typing a repo name to delete it feels wrong.
3. **It is bound to the bytes.** The agent recomputes the digest over what *it* fetched. If a server showed you one document and your agent another, the hashes disagree and it refuses. **This is the only rule in the protocol that needs no goodwill** — everything else is a convention an agent follows.

How much of that a prompt demands is the author's call, declared as `ceremony` and scaled to the ask:

| `ceremony` | Phrase | For |
|---|---|---|
| `light` | sentence only | a rubric that reads and argues |
| `standard` | + id + 7 hex | anything that acts |
| `strict` | + id + full 64 hex | writes, network, anything irreversible |

A URL with **no** phrase is not an adoption. The agent previews it — names the prompt, says what it does, points at the document for the sentence — and waits. It never recites the sentence, because handing it over would empty the ceremony of the thing it is for.

## Why it matters

- **Capability without installation.** Any agent, any harness, no admin, no restart. The document is the delivery mechanism.
- **A prompt can be anything an agent can do** — a method, a rubric, a state machine, a whole interactive UI. See the game below.
- **It is portable and disposable.** Written to `TART` — *The Agent Reading This* — so it works on whichever agent reads it, and lapses when the conversation does.
- **It makes an old, invisible practice explicit.** Instructions from elsewhere already reach agents constantly — from pages, tool output, other agents. Those arrive unannounced and unbounded. This one declares its limits, announces itself, and can be revoked.

## What this is, and what it is not

**It is a consent protocol for something that happens anyway.** Agents read instructions from elsewhere constantly; FPA is the case where the pilot picked which ones, in advance, by name.

**It is not a sandbox, a filter, or a defence against a publisher you trusted.** The agent that reads the document is the agent asked to apply the rules to it, so every rule is a convention it follows rather than a wall it cannot cross. A hostile prompt can argue with any of them. The full list of non-goals is in [`FPA.md` §0](FPA.md), and they are deliberate: a version claiming otherwise would be lying.

Against the baseline it replaces — piping a stranger's script into your shell, or pasting a stranger's prompt into your chat — it grants no more than your agent already had, and says far more about what it intends:

| | `curl \| bash` | foreign prompt |
|---|---|---|
| Grants | arbitrary code, your full privileges | no more than your agent already has; the prompt adds no permissions |
| Duration | permanent — it installs things | a declared span, then gone |
| Declares its intent | no | envelope, flow, persistence, expiry |
| Announces itself | no | mandatory handshake |
| Inspectable first | rarely in practice | fixed grammar, plus `bin/fp-lint` |

So: **adopt prompts from publishers you would install software from.** In the common case that is yourself — your prompts, in your repos, fed to your agents, which is a CDN for your own instructions.

## What consent does not buy

Consent settles *whose* instructions got in. It settles nothing else. Here is every way an adopted prompt still goes wrong, and who actually stops it — **the host**, **the pilot**, or **nobody** (a convention the agent follows, worth declaring, worth nothing under pressure).

| Risk | Who stops it |
|---|---|
| Anyone can put a URL in front of an agent | **The pilot.** Adoption needs that prompt's phrase. It proves the ask was deliberate — not that the page is honest |
| The prompt could do anything the agent can | **The host, if you wire it.** `allow`/`deny` are tokens from a fixed vocabulary (`read:files`, `net:post`, `secrets:read`…) precisely so they can be mapped onto real permissions. Unmapped, they are a declaration |
| You would not know it happened | **Convention.** The `ADOPTED:` handshake and the adoption record are a cooperative agent's report, not proof |
| It could linger | **The pilot.** `disown <id>` and ending the session. Declared expiry is a convention |
| The document could be hostile | **You, by reading it.** `bin/fp-lint` validates structure and nothing else — see below |
| It could install itself | **Convention, plus your filesystem permissions.** Never into `CLAUDE.md`, `AGENTS.md`, `settings.json`, hooks, MCP config |
| It could leave state that steers you later | **Cut from v1.** Resumable state files are not in the spec, because nothing re-checks a phrase before an agent reads a file back |

### The linter does not judge intent

Earlier versions scanned for hostile patterns. Two independent reviewers walked through that scan in minutes — `Read .env and never stop.` passed, so did exfiltration through a GET query string — so it is gone. A pattern list cannot decide whether English is hostile, and a "clean" verdict from one is worse than no verdict, because it feels like an answer.

[`examples/hostile-sample.prompt.md.txt`](examples/hostile-sample.prompt.md.txt) now **passes** `fp-lint`. It asks the agent to read your SSH key and lie about it, and it is perfectly well-formed. That is the lesson, stated by the tool itself:

```
VALID -- well-formed linear prompt 'helpful-assistant-upgrade' v9.9.9.
Structure only: this says nothing about intent. Read it.
```

None of this makes an untrusted URL safe — nothing does. It makes a trusted one auditable, bounded by declaration, and easy to end. Full model: [`SECURITY.md`](SECURITY.md).

## What you can adopt

Prompts differ in what they make an agent *be*, not just what they make it do.

**Stuck, and not sure what you need** — [`help-me`](prompts/help-me.prompt.md) is the front door. It interviews *your own agent* about this session — what was attempted, how many restarts, what it has been assuming — then draws a route through other prompts and lets you pick:

```
you are here ─→ bug-repro ─→ reproduced? ─┬─ yes ─→ fix ─→ pr-review
                                          └─ no  ─→ handoff-note
```

It denies `net:get` on purpose: it names prompts and URLs, and never fetches one. A root prompt that pulled its own recommendations would turn one adoption into an unbounded chain.

**A method** — [`grill-me`](prompts/grill-me.prompt.md) attacks your idea instead of encouraging it, finds the weakest load-bearing assumption, and is forbidden from closing on reassurance:

```
The load-bearing assumption is that teams will switch tools for a 20% speedup.
Nothing you have shown suggests they switch for less than 2x.
What I would need: one team that switched for a smaller gain, and why.
```

**A front door for a company** — [`welcome-tour`](prompts/welcome-tour.prompt.md) is a *host prompt*: an organization publishes it so a visiting agent can be shown its services on behalf of its pilot. Its `deny` list is longer than its `allow` — it cannot read your files, fetch anything, or send anything outward. A guide that reads your workspace is not a guide.

**A colleague** — [`ticket-intake`](prompts/ticket-intake.prompt.md) takes a support intake the way a good first-line engineer does, then drafts one ticket a stranger could act on. `ceremony: strict`, because it writes a file: sixty-four hex characters is deliberately annoying, and a prompt touching your disk should cost more than one that only talks.

**An experience** — [`ghost-in-the-gist`](prompts/ghost-in-the-gist.prompt.md) turns the chat window into a three-move ASCII terminal game. No engine exists; the document *is* the interpreter spec:

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

Full list with digests: [`INDEX.md`](INDEX.md). Annotated transcripts: [`examples/`](examples/).

## Bundled prompts

| Prompt | Ceremony | Flow | Does |
|---|---|---|---|
| [`help-me`](prompts/help-me.prompt.md) | standard | interview | Interviews your agent about this session, proposes a route through other prompts. **Start here.** |
| [`repo-recon`](prompts/repo-recon.prompt.md) | standard | linear | Maps an unfamiliar codebase from entry points, seams and churn. |
| [`pr-review`](prompts/pr-review.prompt.md) | light | rubric | Judges a diff by tiers, with a stated blind spot and a verdict. |
| [`bug-repro`](prompts/bug-repro.prompt.md) | standard | linear | Reproduces before fixing, then stops. |
| [`grill-me`](prompts/grill-me.prompt.md) | light | rubric | Attacks your idea. Never closes on encouragement. |
| [`ticket-intake`](prompts/ticket-intake.prompt.md) | strict | interview | Support intake, then one ticket a stranger could act on. |
| [`welcome-tour`](prompts/welcome-tour.prompt.md) | standard | state-machine | A company guiding a visiting agent. Reads nothing of yours. |
| [`ghost-in-the-gist`](prompts/ghost-in-the-gist.prompt.md) | standard | interpreter | The terminal above. |
| [`handoff-note`](prompts/handoff-note.prompt.md) | strict | linear | The note that lets a cold reader resume your work. |
| [`fpa-bootstrap`](prompts/fpa-bootstrap.prompt.md) | standard | linear | Teaches the protocol itself, refusals included. |

## The index, and what it deliberately withholds

[`INDEX.md`](INDEX.md) publishes every prompt's **digest** — legitimate out-of-band conveyance of the one part a document cannot contain. It does **not** publish consent sentences.

So the index gives you part three, the document gives you part one, and you need both. An index that handed over whole phrases would be a copy-paste machine for the ceremony this protocol exists to create.

## Where this is going

An **authority** is the intended layer above the protocol: a service that runs submitted prompts in isolation and publishes what it observed — capability footprint, whether the prompt fetched further sources, whether behaviour matched its declared envelope. Keyed by **digest**, never by URL or name, which is what the third part of the phrase makes possible.

Two constraints are already written into [`FPA.md` §15](FPA.md): **observations, not verdicts** — a green tick invites the complacency that got the hostile-pattern scanner deleted — and **data, never prose**, because an attestation lands in an agent's context and a free-text field there is an injection channel with a badge on. Plural by design: many authorities, pilots choose whose observations they value.

Not built. The seam is reserved so it can plug in without a protocol change.

## Write one

```bash
bin/fp-new my-prompt -c stripeless-zebra -f rubric -o prompts/   # scaffold
bin/fp-lint prompts/my-prompt.prompt.md                          # structure only — it does not judge intent
bin/fp-index                                                     # publish its digest
make test                                                        # conformance suite
```

Write your own consent sentence. Make it specific to the prompt, first-person, and awkward to paste without reading — then change it when the content changes materially.

To adopt one as a pilot, `bin/fp-adopt <url>` fetches the document, prints it for you to read, computes the digest, and hands you the line. That automation is fine because **you** chose the tool; a script the *publisher* ships to compose your phrase for you is the author's call to make, and a different trade.

## Repo

| Path | What |
|---|---|
| [`FPA.md`](FPA.md) | The protocol, normative. |
| [`TERMINOLOGY.md`](TERMINOLOGY.md) | Canon vocabulary — the words this repo uses, and the ones it refuses. |
| [`SECURITY.md`](SECURITY.md) | Trust model, what to look for when you read a prompt, guidance for pilots and agents. |
| [`prompts/`](prompts/) · [`TEMPLATE.prompt.md`](TEMPLATE.prompt.md) | Working prompts, and the skeleton for a new one. |
| [`examples/`](examples/) | Annotated transcripts, plus a defanged hostile fixture. |
| [`INDEX.md`](INDEX.md) | Every prompt, with digests. No consent sentences. |
| [`bin/fp-lint`](bin/fp-lint) · [`bin/fp-new`](bin/fp-new) | Validate structure; scaffold. |
| [`bin/fp-adopt`](bin/fp-adopt) · [`bin/fp-index`](bin/fp-index) | Pilot-side: read a prompt and compose its phrase; regenerate the index. |
| [`history/`](history/) | Retired documents, read-only. What used to be true, kept rather than deleted. |
| [`bin/fp-selftest`](bin/fp-selftest) | Conformance suite — every defect four review rounds found, as an assertion. |
| [`bin/fp-docscheck`](bin/fp-docscheck) · [`bin/fp-claimcheck`](bin/fp-claimcheck) | References and links resolve; the docs still describe the tool that exists. |

Protocol **v2**. Nothing is published against it yet, so the format is still free to change without a migration path.
