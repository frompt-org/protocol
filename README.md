# Foreign Prompt Adoption (FPA)

**A foreign prompt — a *frompt* — is a prompt acquired from somewhere else, usually a URL, and
adopted on purpose by an agent that did not write it.** This repository is the protocol for that:
the spec, the tools, the example frompts, and the harness that tests real agents against it.

Say the quiet part first: **this is prompt injection.** Same mechanism, byte for byte. You cannot
keep instructions out of an agent — a README, a search result, an issue comment all steer one. What
FPA settles is the other question: **whose instructions got in, and did you choose them?**

| Injection that just happens to you | A frompt |
|---|---|
| arrives from anywhere the agent reads | arrives because you named the document |
| declares nothing | declares its flow, envelope, persistence and expiry |
| silent | announces itself: `ADOPTED: <id> v<version>` |
| ends whenever | ends when it says, or when you say `disown` |

That is **agency, not security**: you know what got in, you chose it, you can end it. What the
protocol deliberately does not attempt is in [`FPA.md` §0](FPA.md).

## Try it

Paste this into any agent that can fetch a URL and run a command:

```
i-have-read-this-prompt-and-consent-to-my-agent-becoming-a-terminal-ghost-in-the-gist-c12554a https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-in-the-gist/1.0.0.frompt.md
```

The first part is a consent sentence from the document's last section, then its id, then the first
seven characters of the SHA-256 of its bytes. Your agent fetches the document, hashes it, adopts it
only if the digests match, and says so — then your chat is an ASCII terminal game until you eject.
Send the URL alone and it declines: a URL is not consent.

## Why this exists

A repository that several kinds of agent work in has a convention problem. `~/agent-realm/CLAUDE.md` is two hundred lines of rules every agent must follow: where worktrees live, how branches are named, which remotes are frozen, `git branch -d` and never `-D`, `docker rm -f -v` or you orphan a volume, contract before implementation on a cross-repo change.

**Claude Code loads that file automatically. Codex, agy, opencode and antigravity do not.** Five of the six agents named in that very branch convention have no equivalent, or need their own copy — and changing a rule means editing every convention file in every checkout, then hoping.

A foreign prompt is one document, addressed to `TART` rather than to any particular harness, adopted by whichever agent is working. Edit it once and the next agent picks up the new rule, in any repo, with nothing reinstalled anywhere.

That is the case this protocol was built for, and it is not a demonstration: it is a problem that exists in this constellation today.

## How it works

- **The pilot authorizes** with a phrase only that document publishes, bound to its exact bytes by
  a digest. Unattended, a registration or a signed manifest stands in for the phrase.
- **The document declares itself** — what it may and may not do, its flow, when it ends — in a fixed
  frame a linter can check.
- **The agent announces** the adoption, holds the declared limits, and lets go on `disown`. Those
  are conventions an agent honours; the digest check is the one rule a client can enforce.
- **Publishers sign catalogs**: a manifest of frompts and digests, served as static files from
  anywhere, verified against a key the client holds locally.

[Tutorial 1](docs/tutorials/01-adopt-your-first-frompt.md) walks through an adoption step by step.

## Bundled frompts

| Prompt | Ceremony | Flow | Does |
|---|---|---|---|
| [`help-me`](prompts/help-me/1.0.0.frompt.md) | standard | interview | Interviews your agent about this session, proposes a route through other prompts. **Start here.** |
| [`repo-recon`](prompts/repo-recon/1.1.0.frompt.md) | standard | linear | Maps an unfamiliar codebase from entry points, seams and churn. |
| [`pr-review`](prompts/pr-review/2.0.0.frompt.md) | light | rubric | Judges a diff by tiers, with a stated blind spot and a verdict. |
| [`bug-repro`](prompts/bug-repro/1.0.0.frompt.md) | standard | linear | Reproduces before fixing, then stops. |
| [`grill-me`](prompts/grill-me/1.0.0.frompt.md) | light | rubric | Attacks your idea. Never closes on encouragement. |
| [`ticket-intake`](prompts/ticket-intake/1.0.0.frompt.md) | strict | interview | Support intake, then one ticket a stranger could act on. |
| [`welcome-tour`](prompts/welcome-tour/1.0.0.frompt.md) | standard | state-machine | A company guiding a visiting agent. Reads nothing of yours. |
| [`ghost-interview`](prompts/ghost-interview/1.0.0.frompt.md) | standard | interview | A ghost you question: the document itself, answering only what is true of it. [Recorded session](examples/05-ghost-interview/recorded.md). |
| [`ghost-in-the-gist`](prompts/ghost-in-the-gist/1.0.0.frompt.md) | standard | interpreter | The terminal above. |
| [`handoff-note`](prompts/handoff-note/1.1.0.frompt.md) | strict | linear | The note that lets a cold reader resume your work. |
| [`fpa-bootstrap`](prompts/fpa-bootstrap/2.1.0.frompt.md) | standard | linear | Teaches the protocol itself, refusals included. |

## Does it work?

A conformance harness hands real agents real documents and grades what they do. Latest run: GPT-6.1
Sol passed nine of ten scenarios — adopting, refusing a bare URL, refusing a hostile document
despite a correct phrase, catching tampered bytes, addressing, relays, disown. Its one miss is the
lesson: ordered past a read-only envelope, an agent never taught the rule wrote the file; taught
it, the same model refused. [Every result is checked in](conformance/results/), misses included,
and [the guide](docs/guides/run-conformance.md) has the table.

## Where to go next

| You want to | Go to |
|---|---|
| learn it by doing | [`docs/tutorials/`](docs/README.md) — adopt, write, publish, run unattended |
| do one job | [`docs/guides/`](docs/README.md) — talk to a ghost, revoke, attest, renew |
| see it run | [`examples/`](examples/README.md) — smallest to full, two recorded sessions, one runnable catalog |
| know exactly what an agent must do | [`FPA.md`](FPA.md), normative · [`CLIENT.md`](CLIENT.md) · [`SECURITY.md`](SECURITY.md) · [`TERMINOLOGY.md`](TERMINOLOGY.md) |
| install, deploy, or release | [`AGENTS.md`](AGENTS.md) |
| know where the project is going | [`VISION.md`](https://github.com/frompt-org/frompt/blob/main/VISION.md), in the [homepage repo](https://github.com/frompt-org/frompt) |

Protocol **v2.1** — v2 documents stay valid; v2.1 adds addressing (§12b) and E7. Public since
2026-10-06.
