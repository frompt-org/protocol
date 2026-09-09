# Vision — what this project is trying to become

[`FPA.md`](FPA.md) is the protocol: what a foreign prompt is and what an agent does with one.
This document is the **project** — why it exists beyond one repo, where prompts are meant to
live, who publishes them, and what is still missing. It is the answer to *where is this going*,
kept separate from the spec so the spec can stay normative and short.

Status is stated plainly throughout. Most of what follows is **not built**.

---

## 1. The thing that changed

Prompts became software. They encode methods, review rubrics, house rules, whole interactive
programs — and teams now maintain them, version them, and argue about them in review.

What they never got is a way to **distribute** one.

| Software has | Prompts have |
|---|---|
| a package name and a version | a file someone pasted into chat |
| a registry to fetch from | a Slack message, a gist, a wiki page |
| a digest that binds the bytes | nothing |
| a signature naming the publisher | nothing |
| an install step you consented to | a copy, forked the moment it was made |
| a way to say *use the current one* | re-paste, and hope |

So a prompt spreads by copying, and every copy is a fork that goes stale silently. The team
that wrote the good review rubric has no way to hand it to anyone that does not immediately
begin to rot.

**This project is the missing distribution layer** — and the consent that a distribution layer
for *instructions* has to carry, because unlike a package, a prompt steers the agent reading it.

## 2. Three parties, one shape

| Party | Who | What they do | Needs |
|---|---|---|---|
| **author** | anyone | writes a document addressed to `TART`, declares its envelope, publishes a consent sentence in its last section | [`TEMPLATE.prompt.md`](TEMPLATE.prompt.md), `bin/fp-new`, `bin/fp-lint` |
| **publisher** | anyone who can serve files | signs a manifest over a set of documents and serves it | `bin/fp-index`, `bin/fp-sign`, `bin/fp-publish` |
| **pilot** | anyone with an agent | names one document, authorizes it, ends it | a phrase, or a pin, or a signature |
| **client** | a harness, a plugin, a shell | does what a model cannot: fetches exact bytes, hashes, verifies, keeps the lock and the record | [`CLIENT.md`](CLIENT.md), levels 0–3 |
| **authority** | *reserved, unbuilt* | runs a submitted prompt in isolation and publishes what it observed | [`FPA.md` §15](FPA.md) |

Author and publisher are usually the same person and do not have to be. Pilot and author are
frequently the same person too — **the common case is your own prompts, in your own repos, fed
to your own agents**, which is a CDN for your own instructions and needs no ecosystem at all.

The ecosystem is what makes the *uncommon* case work: adopting someone else's.

## 3. Where prompts live

A **catalog** is a signed manifest plus the documents it lists, served as static files:

```
<base>/index.json
<base>/prompts/<id>/<version>.prompt.md
```

That is the entire standard. It is a **shape, not a privilege** — no catalog is more official
than another, and there is no registry to be admitted to. A company publishes `acme/prompts`
and serves it wherever it already serves static files; a person publishes from a repo.

`base` is any transport that returns exact bytes — public HTTPS, a `gh:` reference to a private
repo, an internal host, a local path. Trust arrives through a **publisher key held locally**,
never through the catalog it validates, so a private catalog is a complete deployment rather
than a degraded one. See [`README.md`](README.md) for the working commands.

### The org

[`github.com/f-prompts`](https://github.com/f-prompts) holds the protocol and one catalog of it,
and is deliberately not the only publisher the protocol expects:

| Repo | Role | Status |
|---|---|---|
| [`f-prompts/foreign-prompts`](https://github.com/f-prompts/foreign-prompts) | the protocol — spec, tools, reference prompts, conformance harness | exists, **private** |
| [`f-prompts/prompts`](https://github.com/f-prompts/prompts) | the reference catalog — manifest, signature, documents | exists, **private** |
| [`f-prompts/.github`](https://github.com/f-prompts/.github) | the org's public face — what a foreign prompt is, the three doors out, what an agent landing there should do | exists, **private** |

The protocol was born in the `agent-realm` constellation and moved out on 2026-09-09, before
anything was published. The constellation is meant to be this protocol's first **consumer**,
and stage 1 below is a more honest test when the publisher is external to it. The old address
redirects.

Standard and catalog are separate repositories on purpose. The catalog is a set of published,
immutable artifacts with its own rules; the protocol repo is edited freely. `bin/fp-publish`
crosses that boundary deliberately, and refuses to overwrite a published version with different
bytes. That a catalog is its own small repo is also the demonstration of the claim above — it is
a shape anyone can serve, and this one is not special for sitting next to the spec.

### f-prompts.io — a directory, not a bigger catalog

The intended front door is a **directory**: a list of catalogs across publishers, with each
catalog's manifest cached so a search can return an id, a version and a **digest** — the one
part a document cannot contain about itself.

Its rules are fixed in [`DIRECTORY.md`](DIRECTORY.md) before it exists, because the important
ones are the ones convenience erodes: it publishes digests and **never consent sentences**; it
never ranks; listing admits nothing and removal revokes nothing; and **discovery is not
authorization** — a client registers each catalog itself, by the pilot, recorded. A directory
answers *what exists*, never *may I*.

**Status: the domain is unregistered and nothing is built.**

## 4. How this gets used

Adoption in stages, each one useful alone, each one earning the next:

| Stage | What happens | Status |
|---|---|---|
| **0 — it works** | the protocol is specified, the tools run, an agent has been observed adopting, refusing, and holding an envelope | **done** |
| **1 — we use it** | the constellation's own conventions become foreign prompts; agents in `agent-realm` adopt them instead of each reading a different convention file | **next** |
| **2 — someone else uses it** | one team outside this constellation publishes a catalog and adopts from it | not started |
| **3 — public, and findable** | `f-prompts/prompts` and `f-prompts/.github` go public; a directory at `f-prompts.io` lists this catalog and any other; adoption needs no prior relationship with a publisher, only a registration | written, not flipped; directory specified, unbuilt |
| **4 — attestation** | authorities observe prompts and publish findings keyed by digest; pilots choose whose observations they value | reserved, unbuilt |

Stage 1 is the honest test. A protocol whose author will not run their own conventions through
it has not shown that it survives contact with anything.

## 5. Why anyone else would start

The problem that motivates this is not exotic. It is what happens the moment a repository is
worked on by more than one kind of agent.

`~/agent-realm/CLAUDE.md` is two hundred lines of rules every agent must follow. **Claude Code
loads it automatically. Codex, agy, opencode and antigravity do not** — and the branch
convention inside that very file names all six. Five of them need their own copy of the rules,
so changing one rule means editing every convention file in every checkout, then hoping.

Every team with more than one agent brand has some version of this, and the workarounds are all
copies: `AGENTS.md` beside `CLAUDE.md` beside `.cursorrules`, drifting apart from the day they
are made.

One document addressed to `TART` rather than to a harness is the alternative, and it is the
case this protocol was built for.

## 6. What late binding removes

A skill that *contains* instructions is a copy — installed, versioned by whoever installed it,
stale as soon as upstream moves. A skill that *points at* a foreign prompt holds an id, and
resolves it at use time.

The consequence is the part worth stating plainly: **editing the prompt is the deployment.**
Every agent that resolves it is current on its next run, with nothing installed, pushed, or
restarted anywhere. For instructions, the CD half of CI/CD stops being a thing that has to
exist — not because deployment got faster, but because there is nothing to deploy.

What keeps *always current* from meaning *whatever anyone put there this morning* is that the
manifest is fetched and checked too: the resolver compares the bytes it fetched against the
digest the publisher's signed manifest named, and a mismatch is a refusal. `bin/fp-demo` runs
both halves of that trade end to end.

## 7. Roadmap

**Built and tested** — the protocol, 15 tools, 10 prompts across 12 documents, three adoption
contexts, signed manifests with expiry and a per-catalog freshness floor, four transports, a
plugin, and a conformance harness that has put two independent agents through six scenarios.

**Next, in order:**

1. **Constellation conventions as prompts.** `constellation-conventions`, `cross-repo-change` —
   the rules from `CLAUDE.md`, authored properly, published to the catalog, adopted by agents
   working in `agent-realm`. Stage 1.
2. **Measure it.** Change a rule mid-week; confirm the next agent in a different repo picks it
   up with nothing reinstalled. That is the claim in §6, tested rather than asserted.
3. **Flip the org public.** The profile page and the catalog README are written; publication is
   two visibility switches, taken when there is something worth arriving at. GitHub renders an
   org profile only from a *public* `.github` repo, so today the page exists and does not
   display.

**Specified, unbuilt** — the directory ([`DIRECTORY.md`](DIRECTORY.md)) and a level-3 client that maps envelope tokens onto real permissions ([`CLIENT.md`](CLIENT.md)). Both have rules now so that building them is not also designing them.

**Reserved, deliberately unbuilt** — the authority ([`FPA.md` §15](FPA.md)), role scoping in the
manifest, and key rotation. Each has a seam so it can arrive without a protocol change; none has
a use case sharp enough yet to design against.

**Never** — the non-goals in [`FPA.md` §0](FPA.md) are permanent. This does not become a sandbox,
a scanner, or a defence against a publisher you chose to trust. A hostile-pattern scanner was
built here once and deleted, because a clean verdict from one is worse than no verdict.

## 8. Where we actually are

| | |
|---|---|
| Protocol | v2, specified, 89 checks passing |
| Agents observed adopting | 2 |
| Catalogs published | 1, private |
| Publishers other than this one | 0 |
| Pilots other than the author | 0 |

The last two lines are the whole remaining problem, and stage 1 is the only honest way to start
on them: use it here, on real conventions, where the failure would be visible.
