# Client profile — what a harness implements

[`FPA.md`](FPA.md) addresses authors and TART. Its rules fall into two kinds that it never
separates: **conventions** the runtime agent honours (refuse a hostile document, emit the
handshake, stop on `disown`) and **mechanism** that a model cannot perform by itself (hash
exact bytes, verify a signature, refuse a stale manifest). The second kind is done by software
around the agent. This document names that software — the **client** — and says what a client
at each level must do, so that "any agent" can mean an agent whose harness implements this
rather than an agent running this repository's scripts.

Normative. `MUST` and `MUST NOT` mean what they mean in [`FPA.md`](FPA.md).

## 1. Client and TART are two things

**TART** is the model reading the document. **The client** is whatever it calls: a shell and
`shasum`, a plugin, a resolver, a fleet's agent runtime. TART decides; the client measures.

The split matters because a convention can be argued with and a measurement cannot. Every
rule in [`FPA.md`](FPA.md) §1 that says *a client MUST* is addressed here. Every rule that
says *TART MUST* is a convention, and this document does not pretend otherwise.

| Rule | Kind | Who |
|---|---|---|
| Fetch exact bytes (§T1), hash them (§C5a, §M8) | mechanism | client |
| Refuse bytes whose digest is not the pinned one (§M3) | mechanism | client |
| Refuse an unregistered catalog, or a changed signing key (§AC2b) | mechanism | client |
| Verify the manifest signature against a local trust root (§AC3, §M7) | mechanism | client |
| Refuse an expired manifest, or a serial below the floor (§M6a, §M6) | mechanism | client |
| Fail closed when the manifest cannot be verified (§AC4) | mechanism | client |
| Keep the adoption record (§AC5) | mechanism | client |
| Screen the document (§9), emit the handshake, hold the envelope, stop on `disown` (§13) | convention | TART |
| Never recite a consent sentence (§PV1) | convention | TART |

An agent that cannot hash what it fetched has no client and **MUST NOT** adopt (§C5a). That
rule is the floor under everything below.

## 2. Levels

A client claims one level. Each includes the ones before it.

### Level 0 — reader

Any agent with a fetch and a shell, adopting interactively. The client is `curl` and `shasum`.

- **MUST** fetch exact bytes and compute SHA-256 over them, so part three of the phrase can be
  checked against what actually arrived.
- **MUST** tell the pilot when it could not fetch or could not hash, and adopt nothing.
- Everything else at this level is convention: §9, §11, §13.

This is the level the conformance harness tests. `bin/fp-conform` hands a real agent real
documents over a real local server and grades whether it adopted, refused, previewed and held
its envelope. Two independent agents have passed it. No tooling from this repository is
required to be a level-0 client; `bin/fp-adopt` is a convenience for the *pilot*, composing
the phrase, and is not the agent's.

### Level 1 — resolver

Adds the `registered` context: an id resolves to verified bytes, and a workspace has agreed
to a publisher once.

- **MUST** resolve `<id>` or `<id>@<version>` through the publisher's manifest, fetched from the
  publisher, and compare the fetched bytes to the digest the manifest names (§M5 — bytes,
  not the manifest's own claim about itself).
- **MUST** honour a lock file: refuse bytes whose digest, version or origin differ from the pin
  (§M3). Re-pinning is a change a person reviews.
- **MUST** keep a registration record — catalog, signing key fingerprint, pin mode, when, who
  (§AC2a) — and **MUST** refuse a catalog absent from it, or whose key has changed (§AC2b).
- **MUST** refuse to resolve bytes that appear in no manifest, with a non-zero exit. Printing a
  document and returning success is how unindexed text becomes an adoption.
- **MUST NOT** apply a pin or a registration to a prompt whose `contexts` excludes
  `registered` (§AC4b).

Reference: `bin/fp-resolve`, `bin/fp-lock`, `bin/fp-register`. The registration record is
`fpa.registered`, one line per catalog, the shape `sources.list` has had for thirty years.

### Level 2 — verifier

Adds the `managed` context: no human at use time, so a signature authorizes.

- **MUST** verify the manifest's signature against a trust root held locally and never fetched
  from the host being checked (§M7).
- **MUST** refuse a manifest past `not_after` (§M6a) and one whose `serial` is below the highest
  already accepted **from that catalog**, keyed by the manifest's `base` (§M6).
- **MUST** compute digests over exact bytes (§M8); a client that reads text first has a
  line-ending bug that hashes a CRLF copy identical to its LF original.
- **MUST** fail closed — exit non-zero, adopt nothing — when it cannot fetch or verify the
  manifest (§AC4). Falling back to an unsigned fetch is not a degraded mode; it is the
  absence of this level.
- **MUST** name an actor and keep an append-only record of adoptions: id, version, digest,
  source, and how it was authorized (§AC5). The record names an actor for an audit trail; it
  does not authenticate one. That is the platform's job.

Reference: `bin/fp-verify --from <publisher>`, `bin/fp-sign` on the publisher's side,
`bin/fp-agent`, `bin/fp-record`.

### Level 3 — host

Maps envelope tokens onto real permissions. `deny: write:files` becomes a filesystem the
agent cannot write; `deny: net:post` becomes a network it cannot post on.

**No client is at this level.** The capability vocabulary in [`FPA.md`](FPA.md) §4 is fixed
precisely so that one could be. Until one is, an envelope is a declaration the agent honours,
which is what [`FPA.md`](FPA.md) §0 says it is. A level-3 client is the only thing in this
project that would turn a convention into a boundary, and this document reserves the level
rather than describing a design nobody has needed.

## 3. Claiming a level

A level is claimed by evidence, not by a badge.

- **Level 0**: the conformance scenarios in [`conformance/scenarios.json`](conformance/scenarios.json),
  run against the actual agent, with the transcript kept.
- **Levels 1 and 2**: the checks in `bin/fp-selftest` under *resolve*, *lock*, *register* and
  *verify*. Each one is a defect this repository's own client once had — a CRLF copy passing
  verification, unindexed bytes exiting 0, a new catalog refused as a rollback of an unrelated
  one, a signature that did not verify reported as success. A client that passes them has at
  least not repeated those.

A client at a level it cannot evidence is at the level below it.

## 4. What a harness ships

Three verbs, kept separate: **find** (list what a catalog offers), **adopt** (resolve, verify,
hand the bytes to the agent with the handshake expected), **adopted** (the record). They stay
separate because in an unattended context nobody reads the document before it runs, and one
convenient action that does all three is an adoption nobody saw.

A session-start hook **MAY** print what exists. It **MUST NOT** adopt anything. A hook that
adopted on startup would be adopting on nobody's authority, wearing the badge of the platform.

Today one harness has this: [`plugin/`](plugin/) for Claude Code, at level 2. Every other
agent in the constellation is a level-0 client with a shell, which is enough to adopt
interactively and not enough to run unattended. That gap is the stage-1 work in
[`VISION.md`](https://github.com/frompt-org/frompt/blob/main/VISION.md), and it is the reason this document exists.
