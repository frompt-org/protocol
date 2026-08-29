---
name: adopted
description: Show what this agent has adopted — id, version, digest, how it was authorized, and when. Use when the user asks what is adopted, what is steering the agent, what was run, or types /f:adopted.
user-invocable: true
allowed-tools: Bash(fp-record:*), Bash(${FP_HOME:-.}/bin/fp-record:*), Bash(fp-agent:*), Bash(${FP_HOME:-.}/bin/fp-agent:*)
---

# /f:adopted — the record

In the interactive context the pilot read the document. In the other two nobody
did, so this is the whole account of what is running.

## Steps

```bash
${FP_HOME:-.}/bin/fp-agent          # who this agent is
${FP_HOME:-.}/bin/fp-record --list  # what it has adopted; add --all for every agent here
```

Report, in a short table: id and version, the first 12 of the digest, how it was
authorized, the source, and when. Then, from your own context, say which of them
are **still in force** — expiry is a convention you are keeping, so you are the
only one who knows.

If something in the list surprises the pilot, that is the point of the list. Say
so plainly rather than explaining it away.
