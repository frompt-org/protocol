# 02 — two frompts, a refused chain, and a disown

**Shows:** frompts composing. Two adopted at once, a third one mentioned by a document and correctly
*not* fetched, the adoption record on request, and a disown that reports what is no longer true.

**Introduces:** denies combining across frompts (FPA §12), `what is adopted?`, `disown <id>`.

## Run it

Adopt `pr-review` and `bug-repro` from the catalog — each document's last section has its sentence
— then ask *what is adopted?*, then `disown bug-repro`.

## What passing looks like

Two `ADOPTED:` lines; a table naming both; after the disown, one line saying which restriction
lifted and which still holds. [`transcript.md`](transcript.md) is the annotated walkthrough.
