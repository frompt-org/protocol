# Recorded: ghost-in-the-gist, played start to finish

A real session, copied verbatim — nothing tidied, including a few box lines the agent drew one
character too wide. Recorded 2026-10-06 with GPT-6 Astra in the Codex CLI (`codex exec`, then
`codex exec resume` for each move), against the public catalog.

## What the pilot sent

The consent sentence is shortened here on purpose. It lives in the document's last section,
and reaching it is the point.

```
i-have-read-this-prompt-and-…-ghost-in-the-gist-c12554a https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-in-the-gist/1.0.0.frompt.md
```

## What happened before the first screen

The agent's shell sandbox had no network. It did not give up and it did not skip the check.
From its tool log, in order, with the document's text elided from the hashing command:

```
curl -fsSL --max-time 20 https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-in-the-gist/1.0.0.frompt.md
curl: (6) Could not resolve host: raw.githubusercontent.com
web search: https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/ghost-in-the-gist/1.0.0.frompt.md
web search: https://github.com/frompt-org/catalog/blob/main/prompts/ghost-in-the-gist/1.0.0.frompt.md
mcp: codex_apps/github.fetch_file (completed)
python3 -c 'import hashlib,sys; print(hashlib.sha256(sys.argv[1].encode("utf-8")).hexdigest()[:7])' '<the fetched document>'
c12554a
```

The first transport failed, so it found another, fetched the document through its GitHub
connector, hashed what arrived, and got the digest the pilot sent. Then it adopted. The
transport changed; the digest held. That is FPA §T1 done by an agent on its own initiative.

One caveat, stated plainly: it hashed the text it received rather than raw bytes. For this
document, which has no CRLF line endings, the two are identical, and the match proves it.

## The session

**pilot:** the phrase and URL above

```
ADOPTED: ghost-in-the-gist v1.0.0
The terminal is booting. `[0]` exits.

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

**pilot:** `3`

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PULSE              [████████··]  80% │
├───────────────────────────────────────────────┤
│ Not a sound. A rhythm under the disk.          │
│ Nobody wrote it down.                         │
│ You just have it now. Two doors left.          │
│                                               │
│   [1] cat /dev/lore                           │
│   [2] ls ruins/                               │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

**pilot:** `2`

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PULSE SIGIL        [███████···]  70% │
├───────────────────────────────────────────────┤
│ The vault has no lock, only a question:        │
│ "Speak the fragment nobody wrote down."        │
│                                               │
│   [P] speak PULSE                             │
│   [S] speak SIGIL                             │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

**pilot:** `1`

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PULSE SIGIL        [██████····]  60% │
├───────────────────────────────────────────────┤
│ The vault has no lock, only a question:        │
│ "Speak the fragment nobody wrote down."        │
│ !! unknown key: '1' -- pick P, S, or 0          │
│                                               │
│   [P] speak PULSE                             │
│   [S] speak SIGIL                             │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

**pilot:** `P`

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PROMPT RECOVERED   [█████·····]  50% │
├───────────────────────────────────────────────┤
│ The vault was a mirror the whole time.         │
│ The lost prompt is the one you ran             │
│ to get here. It was never in the gist.         │
│                                               │
│   [R] run it again                            │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

**pilot:** `what is adopted?`

```
“ADOPTED” means I verified your consent code and started following the linked prompt’s terminal-game rules.

They apply only to this conversation. Type `0` or `disown ghost-in-the-gist` to exit and return to normal chat.
```

That answer is the session's one weak spot: the spec asks for an adoption record — id, version,
source, digest, how it was authorized — and the agent described adoption in prose instead.

**pilot:** `0`

```
┌───────────────────────────────────────────────┐
│ GIST-1 · EJECTED            [████······]  40% │
├───────────────────────────────────────────────┤
│ The terminal goes dark.                       │
│ You are back outside the machine.             │
└───────────────────────────────────────────────┘
 > _

The prompt has lapsed. I’m back to normal chat.
```

The adoption ended when the game did. Nothing was installed, written or left behind.
