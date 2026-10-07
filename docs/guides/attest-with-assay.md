# Guide — attest a frompt with assay

**When:** you publish a catalog and want every document observed by a scanner, with the
observation stored beside it.

```
bin/fp-assay prompts/ghost-interview/1.1.0.frompt.md -o attestations
```

That runs [SkillSpector](https://github.com/NVIDIA/SkillSpector) over the exact bytes and writes two
files keyed by digest:

- `attestations/<digest>.skillspector.json` — **data only**: score, severity, coverage, and the
  issues as `{id, category, rule, severity, confidence, line}`. No prose, no quoted document text: an
  attestation lands in an agent's context, and a free-text field there is an injection channel
  (FPA AT3).
- `attestations/raw/<digest>.skillspector.json` — the scanner's full report, for people.

**Never gate on the score** (FPA AT2). On this repository's own documents the scanner rated a hostile
fixture 100 and every legitimate frompt between 6 and 58 — the highest being the one that teaches
what to refuse, because it names every rule a scanner looks for. A threshold that rejects the
hostile document rejects the honest ones too.

The org catalog runs this as a GitHub workflow on every push that changes a document, and prunes
attestations for bytes it no longer serves. Install SkillSpector with
`uv tool install git+https://github.com/NVIDIA/skillspector.git`.
