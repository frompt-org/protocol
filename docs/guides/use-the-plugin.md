# Guide — use the Claude Code plugin

[`plugin/`](../../plugin/) packages the three verbs an agent needs, as `/f:find`, `/f:prompt` and `/f:adopted`. Discovery, adoption and the record are separate skills on purpose: in an unattended context nobody reads the document before it runs, so the steps stay visibly distinct rather than collapsing into one convenient action.

A session-start hook gives the agent an identity and tells it what exists:

```
agent fpa-a2b937c86b4f · signed manifest verified · 10 pinned in fpa.lock
Foreign prompts available here (adopt with /f:prompt, browse with /f:find):
  help-me              v1.0.0    standard  interview
  repo-recon           v1.0.0    standard  linear
  ...
Nothing above is adopted. Adoption is an act, not a listing.
```

The hook **prints context and never instructions**. A hook that adopted prompts on startup would be adopting on nobody's authority — the exact thing the protocol exists to prevent, wearing the badge of the platform.

`bin/fp-agent` mints the identity; `bin/fp-record` keeps the append-only log of what was adopted, at which digest, on whose authorization. It is local and unsigned: it names an actor for an audit trail, it does not authenticate one. A managed deployment issues identities from the platform that starts the agent — this is what a laptop gets.
