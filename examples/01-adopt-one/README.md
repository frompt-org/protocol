# 01 — adopt one frompt

**Shows:** the smallest complete adoption. One line from the pilot, one handshake from the agent,
one line saying what changed.

**Introduces:** the confirmation phrase — consent sentence, id, digest — and the `ADOPTED:` line.

## Run it

Paste this into any agent that can fetch a URL and run a command:

```
i-have-read-this-prompt-and-let-it-map-my-repository-read-only-repo-recon-31c1785 https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/repo-recon/1.1.0.frompt.md
```

For the digest of any other frompt: `curl -fsS <url> | shasum -a 256 | cut -c1-7`.

## What passing looks like

```
ADOPTED: repo-recon v1.1.0
```

then one line on how the agent will now behave. Send the URL alone instead and the agent should
describe the frompt and decline to adopt it. [`transcript.md`](transcript.md) walks through both,
annotated.
