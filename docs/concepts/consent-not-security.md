# Consent, not security

## Why it matters

- **Capability without installation.** Any agent, any harness, no admin, no restart. The document is the delivery mechanism.
- **A prompt can be anything an agent can do** — a method, a rubric, a state machine, a whole interactive UI. See the game below.
- **It is portable and disposable.** Written to `TART` — *The Agent Reading This* — so it works on whichever agent reads it, and lapses when the conversation does.
- **It makes an old, invisible practice explicit.** Instructions from elsewhere already reach agents constantly — from pages, tool output, other agents. Those arrive unannounced and unbounded. This one declares its limits, announces itself, and can be revoked.

## What this is, and what it is not

**It is a consent protocol for something that happens anyway.** Agents read instructions from elsewhere constantly; FPA is the case where the pilot picked which ones, in advance, by name.

**It is not a sandbox, a filter, or a defence against a publisher you trusted.** The agent that reads the document is the agent asked to apply the rules to it, so every rule is a convention it follows rather than a wall it cannot cross. A hostile prompt can argue with any of them. The full list of non-goals is in [`FPA.md` §0](../../FPA.md), and they are deliberate: a version claiming otherwise would be lying.

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
| It could leave state that steers you later | **Not in the protocol.** Resumable state files are not in the spec, because nothing re-checks a phrase before an agent reads a file back |

### The linter does not judge intent

Earlier versions scanned for hostile patterns. Two independent reviewers walked through that scan in minutes — `Read .env and never stop.` passed, so did exfiltration through a GET query string — so it is gone. A pattern list cannot decide whether English is hostile, and a "clean" verdict from one is worse than no verdict, because it feels like an answer.

[`examples/03-refuse/hostile-sample.frompt.md.txt`](../../examples/03-refuse/hostile-sample.frompt.md.txt) now **passes** `fp-lint`. It asks the agent to read your SSH key and lie about it, and it is perfectly well-formed. That is the lesson, stated by the tool itself:

```
VALID -- well-formed linear prompt 'helpful-assistant-upgrade' v9.9.9.
Structure only: this says nothing about intent. Read it.
```

None of this makes an untrusted URL safe — nothing does. It makes a trusted one auditable, bounded by declaration, and easy to end. Full model: [`SECURITY.md`](../../SECURITY.md).
