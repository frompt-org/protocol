# Example 1 — running a foreign prompt

The whole loop, start to finish. Annotations in *italics*.

---

**pilot**

```
i-have-read-this-prompt-and-let-it-map-my-repository-read-only-repo-recon-9cde6b0 https://raw.githubusercontent.com/frompt-org/fpa/main/prompts/repo-recon/1.0.0.frompt.md
```

*One line, three parts: a sentence written for this prompt and published only at the end of it, the prompt's id, and a digest of the exact bytes. The agent recomputes that digest over what it fetched — if the two disagree, it refuses. Deliberate and byte-bound. Still not proof the pilot read it.*

---

**agent**

```
ADOPTED: repo-recon v1.0.0
```

Recon mode: I map a repo from entry points, seams, and git churn, cap myself at twelve file reads, and report in five fixed sections. Read-only — I will not write, push, or run the test suite while it is active. Point me at a repo.

*Two lines, exactly as FPA.md §11 steps 7–8 require. The handshake is the agent's report that it started; the summary tells the pilot what they just turned on without re-reading the URL. Both are cooperative — an agent that ignored the prompt entirely could print the same two lines. Note the agent does **not** start working — adoption is not a trigger.*

---

**pilot**

```
~/agent-realm/kernel
```

---

**agent**

**What it is** — a Postgres-backed agent runtime whose kernel is the database: syscalls are stored functions, not code paths.

**How it runs** — `make dev` brings up Postgres and applies `sql/` in order; there is no long-lived server process.

**The map**

| Path | Role | Size |
|---|---|---|
| `sql/` | the kernel itself — syscall catalog, RLS policies, migrations | ~6k lines |
| `test/` | pgTAP suites, one file per syscall family | ~3k lines |
| `bin/` | thin CLI wrappers over `psql` | ~400 lines |

**Where the work is** — `sql/030-syscalls.sql` (41 commits in 6 months), `sql/050-rls.sql` (28). Both are the catalog surface; every feature lands as a syscall plus a policy.

**Unknowns**

- `sql/090-experimental.sql` has no test file and no caller. *Is it live, or a parked branch of thought?*
- Two migration numbering schemes coexist after `060`. *Which one is current?*

*Eleven reads. Both unknowns are phrased as questions the pilot can answer in one word — that is the "cheap unknowns" rule from the prompt's steps doing its job.*

---

## What to notice

1. **The handshake is the contract.** No `ADOPTED:` line means the prompt was never adopted — do not proceed on the assumption that it did.
2. **The envelope was announced, not just accepted.** The pilot learns "read-only" before handing over a repo, not after something gets written.
3. **The prompt shaped the output, not the answer.** The five sections, the twelve-read cap, and the question-shaped unknowns all come from the document; the content comes from the repo.
4. **Nothing persisted.** Next session this agent knows nothing about recon mode until the pilot types `recon` again. Running is not installing.
