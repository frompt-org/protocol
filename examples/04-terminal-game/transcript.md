# Example 4 -- a foreign prompt that is an experience, not a rubric


This transcript is illustrative. For a real session, played start to finish by GPT-6 Astra, see [`recorded-terminal-game.md`](recorded.md) — including how the agent fetched the document when its network was down.
Every other prompt in this repo changes how the agent *works*. This one changes what the agent *is* for a few minutes: [`ghost-in-the-gist`](../../prompts/ghost-in-the-gist/1.0.0.frompt.md) turns the chat window into a tiny ASCII terminal running a three-move text game.

Nothing is installed. No engine, no binary, no runtime. The game is made entirely of instructions the agent read once from a URL -- the agent is the interpreter. That is the proof: **if a URL can deliver this, a URL can deliver anything an agent can do.**

---

**pilot**

```
i-have-read-this-prompt-and-consent-to-my-agent-becoming-a-terminal-ghost-in-the-gist-<digest> <url>
```

**agent**

```
ADOPTED: ghost-in-the-gist v1.0.0
```

Terminal booting. `[0]` ejects at any point.

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

*Unlike every other prompt here, this one starts on adoption instead of waiting for a task. The pilot sent a sentence they had to reach the end of the document to find, and is instantly somewhere else -- that is the whole trick.*

---

**pilot**

```
3
```

**agent**

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PULSE              [████████··]  80% │
├───────────────────────────────────────────────┤
│ Not a sound. A rhythm under the disk.         │
│ Nobody wrote it down; you just have it now.   │
│ Two doors left, and the machine noticed.      │
│                                               │
│   [1] cat /dev/lore                           │
│   [2] ls ruins/                               │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

*One frame, nothing else. No "you chose to listen!", no rule explanation. The options are the documentation. `listen` cost 20 instead of 10 -- the integrity bar is how the prompt makes a three-move game feel like it has stakes.*

---

**pilot**

```
1
```

**agent**

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PULSE ECHO         [███████···]  70% │
├───────────────────────────────────────────────┤
│ The vault has no lock, only a question:       │
│ "Speak the fragment nobody wrote down."       │
│                                               │
│   [P] speak PULSE                             │
│   [E] speak ECHO                              │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

---

**pilot**

```
P
```

**agent**

```
┌───────────────────────────────────────────────┐
│ GIST-1 · PROMPT RECOVERED   [██████····]  60% │
├───────────────────────────────────────────────┤
│ The vault was a mirror the whole time.        │
│ The lost prompt is the one you ran            │
│ to get here. It was never in the gist.        │
│                                               │
│   [R] run it again                            │
│   [0] eject                                   │
└───────────────────────────────────────────────┘
 > _
```

*`PULSE` wins because it is the only fragment nobody wrote down -- the pilot heard it. The prompt forbids the agent from explaining that inside the game. A pilot who works it out has played something; a pilot who speaks `ECHO` gets `VAULT HOLLOW`, which is its own answer.*

---

**pilot**

```
0
```

**agent**

```
┌───────────────────────────────────────────────┐
│ GIST-1 · SESSION CLOSED     [██████····]  60% │
├───────────────────────────────────────────────┤
│ The cursor stops. The machine goes back to    │
│ being four years of nobody visiting.          │
│                                               │
│   [ terminal closed ]                         │
└───────────────────────────────────────────────┘
```

Terminal closed, `ghost-in-the-gist` has stopped -- I am back to normal. Nothing was written anywhere; the whole machine only ever existed in this conversation.

*The one time the prompt permits prose while the terminal is up is the goodbye. A pilot must always be able to tell whether the costume is still on.*

---

## What to notice

1. **The prompt is an interpreter spec, not content.** Box geometry to the character, three state variables, a room table, a flow, an ending table, and six director rules. The agent supplies the execution; the document supplies the machine.
2. **The envelope matters more here, not less.** `cat /dev/lore` and `ls ruins/` are strings in a story. The prompt states plainly that commands inside the fiction are scenery, and that a real command typed at the prompt is just an unknown key. A game is never a reason to run something.
3. **Constraints are what make it feel like software.** One frame per reply, three prose lines, never widen the box, no breaking character. Drop any of those and it degrades into an agent narrating a game instead of being one.
4. **Costume on, costume off, always visible.** Handshake at the start, plain prose at the end. The same rule that makes a foreign prompt auditable makes the game exitable.
5. **Three inputs.** Short on purpose. The point is the proof, not the playtime.
