# Late binding — the point of wrapping one in a skill

A skill that *contains* instructions is a copy: installed, versioned by whoever installed it, stale the moment upstream changes. A skill that *points at* a foreign prompt is late-bound — whatever the prompt says today is what runs today.

[`.claude/skills/f/SKILL.md`](../../.claude/skills/f/SKILL.md) is that skill, in five paragraphs. `bin/fp-demo` proves both halves of the trade:

```
1. What the skill resolves today
   resolved=pr-review version=1.2.0 digest=14ddafabd841 verified=yes
   verdict: one of exactly three: `block`, `comment`, `clean`

2. The publisher changes the prompt and republishes the index

3. What the skill resolves now — same command, nothing reinstalled
   resolved=pr-review version=1.3.0 digest=dec05a442774 verified=yes
   verdict: one of exactly four: `block`, `comment`, `clean`, `needs-a-second-reader`

4. Now the same edit WITHOUT republishing the index
   fp-resolve: DIGEST MISMATCH for pr-review
     index published dec05a442774…
     fetched bytes   ca464c29f9e5…
   Refusing.
```

Step 3 is the promise: one prompt at one URL, every agent current, **nothing deployed to anyone** — and it only holds because the manifest is fetched too. A client reading digests out of its own checkout is not late-bound at all; it is pinned to whenever it last pulled. Step 4 is what keeps "always current" from meaning "whatever anyone put there this morning" — the resolver checks the fetched bytes against the digest the index published, and a mismatch is a refusal, not a warning.

The ceremony is gone in this mode, deliberately: the pilot consented once, by installing the skill. What replaces it is the **adoption record** — id, version, digest, source — because the pilot never read the document and that line is the only account of what is steering them.

## Versions

A prompt's versions are separate immutable documents:

```
prompts/pr-review/1.2.0.frompt.md     three verdicts, verdict last
prompts/pr-review/1.3.0.frompt.md     adds `second-reader` for what it cannot settle
prompts/pr-review/2.0.0.frompt.md     verdict first — a breaking change to the output contract
```

Two selectors, and no more:

```bash
bin/fp-resolve pr-review@1.2.0     # exactly that one
bin/fp-resolve pr-review@latest    # newest non-prerelease
```

**No range grammar, deliberately.** `^1.2` exists to reconcile transitive dependencies, and a foreign prompt has none — a pilot adopts one document, and a chained one needs a fresh decision. There is no diamond to resolve, so the machinery that resolves diamonds is weight without a load.

And the digest is doing the real work anyway: a version number helps a human *choose*, while the digest *binds*. Choose wrong and you still provably got the bytes the manifest named.

One rule underneath: **published bytes never change.** A change is a new version. Without that, a lock file is a lie.

Selectors never appear in a confirmation phrase — a phrase binds a digest, and `latest` has none until it resolves. So `@latest` belongs to the pinned and signed contexts, where something other than a human is doing the authorizing.
