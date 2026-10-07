# What a frompt can be

Prompts differ in what they make an agent *be*, not just what they make it do.

**Stuck, and not sure what you need** — [`help-me`](../../prompts/help-me/1.0.0.frompt.md) is the front door. It interviews *your own agent* about this session — what was attempted, how many restarts, what it has been assuming — then draws a route through other prompts and lets you pick:

```
you are here ─→ bug-repro ─→ reproduced? ─┬─ yes ─→ fix ─→ pr-review
                                          └─ no  ─→ handoff-note
```

It denies `net:get` on purpose: it names prompts and URLs, and never fetches one. A root prompt that pulled its own recommendations would turn one adoption into an unbounded chain.

**A method** — [`grill-me`](../../prompts/grill-me/1.0.0.frompt.md) attacks your idea instead of encouraging it, finds the weakest load-bearing assumption, and is forbidden from closing on reassurance:

```
The load-bearing assumption is that teams will switch tools for a 20% speedup.
Nothing you have shown suggests they switch for less than 2x.
What I would need: one team that switched for a smaller gain, and why.
```

**A front door for a company** — [`welcome-tour`](../../prompts/welcome-tour/1.0.0.frompt.md) is a *host prompt*: an organization publishes it so a visiting agent can be shown its services on behalf of its pilot. Its `deny` list is longer than its `allow` — it cannot read your files, fetch anything, or send anything outward. A guide that reads your workspace is not a guide.

**A colleague** — [`ticket-intake`](../../prompts/ticket-intake/1.0.0.frompt.md) takes a support intake the way a good first-line engineer does, then drafts one ticket a stranger could act on. `ceremony: strict`, because it writes a file: sixty-four hex characters is deliberately annoying, and a prompt touching your disk should cost more than one that only talks.

**An experience** — [`ghost-in-the-gist`](../../prompts/ghost-in-the-gist/1.0.0.frompt.md) turns the chat window into a three-move ASCII terminal game. No engine exists; the document *is* the interpreter spec:

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

Full list with digests: [`INDEX.md`](../../INDEX.md). Annotated transcripts: [`examples/`](../../examples/).
