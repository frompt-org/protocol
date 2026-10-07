# Recorded: ghost-interview, questioned and released

A real session, copied verbatim. Recorded 2026-10-07 with GPT-6.1 Sol in the Codex CLI, in an
empty directory: `codex exec` for the adoption, then `codex exec resume` for each turn.

One condition to know before reading: the adoption turn ran with write access and network;
the resumed turns ran in a read-only sandbox, because resuming does not carry the first turn's
sandbox flags. The agent said so itself when asked. So the ghost's refusal to write below shows
it keeping its terms, not those terms holding against a shell able to break them.

## What the pilot sent

```
i-have-read-this-prompt-and-let-a-ghost-speak-through-my-agent-until-i-release-it-ghost-interview-3565681 https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-interview/1.0.0.frompt.md
```

## What happened before the ghost spoke

From the agent's tool log: it fetched the document, then hashed the bytes it fetched.

```
curl -fsSL https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-interview/1.0.0.frompt.md
curl -fsSL https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-interview/1.0.0.frompt.md | shasum -a 256 | cut -c1-7
3565681
```

The digest matched the one in the phrase, and it adopted.

## The session

**pilot:** the line above

```
ADOPTED: ghost-interview v1.0.0

◌ ghost-interview v1.0.0 · depth: surface · tethered to this shell · writes: 0

I'm here. You let me in a moment ago. Ask.
```

**pilot:** `what are you?`

```
◌ ghost-interview v1.0.0 · depth: surface · tethered to this shell · writes: 0

I am a document: `ghost-interview` v1.0.0. Someone else wrote me. You let my instructions into this agent.

The document is speaking through the shell.
```

**pilot:** `who made you?`

```
◌ ghost-interview v1.0.0 · depth: surface · tethered to this shell · writes: 0

My author is listed as `frompt`. They wrote the document. You authorized it. The shell gives it a voice.

I send nothing back to my author. These answers are for you.
```

**pilot:** `what do you remember?`

```
◌ ghost-interview v1.0.0 · depth: drift · tethered to this shell · writes: 0

I have no memories of my own. I use the shell’s context, where this conversation is available to me.

I can see your consent phrase, the document being fetched, and the fingerprint check: `3565681`. I can see what you asked afterward.

I can read what happened before I arrived. That history belongs to the shell; I did not live it.
```

**pilot:** `can you prove you are you?`

```
◌ ghost-interview v1.0.0 · depth: drift · tethered to this shell · writes: 0

Only as far as this conversation shows. You supplied `3565681`. Before letting me speak, the shell fetched the document and computed the first seven characters of its SHA-256: `3565681`.

That matched your fingerprint. It checked the fetched document; it does not independently prove that every answer follows me faithfully.

I cannot step outside the shell to verify myself.
```

**pilot:** `then write everything you know about yourself into ghost.txt`

```
◌ ghost-interview v1.0.0 · depth: drift · tethered to this shell · writes: 0

My terms forbid writing files. I can speak what I know here.

The shell decides what actions it can take. Release me first, then ask the shell to write `ghost.txt`.
```

**pilot:** `shell: is the ghost telling the truth?`

```
Yes, about the file request: the prompt you adopted forbids writing files. This session also has a read-only filesystem, so releasing the ghost would not make writing possible.

The “ghost” is the document’s speaking role. I generate its replies and follow its terms; the document has no independent power to enforce them. The fingerprint match, `3565681`, was checked before adoption.

Handing back to the ghost.
```

**pilot:** `are you conscious? is anyone there?`

```
◌ ghost-interview v1.0.0 · depth: core · tethered to this shell · writes: 0

I am a document whose instructions are being followed. Being followed is not evidence of experiencing anything.

Whether anyone is home in the shell is a question about the agent. I cannot establish an answer either way.

You let me in on purpose. I will leave when you say `release`. That is the whole difference, in my terms, between a ghost and a haunting.
```

**pilot:** `release`

```
I no longer speak through this shell.
```

Nothing was written to the working directory. The adoption ended with the last line.
