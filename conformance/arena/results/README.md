# Arena results

Reports written by [gentar](https://github.com/agent-realm/gentar), engine v0.9.2, each from a fresh
sbx microVM on the agent-realm bench host, run from a fresh clone of this repository. The verdict is
the exit code; each report lists every step with its output and every assertion with what it saw.

| Suite | Verdict | Run |
|---|---|---|
| [`floor-make-test`](floor-make-test.md) | **pass** — every check, with a throwaway key made in the bench | 2026-10-07 |
| [`floor-catalog-e2e`](floor-catalog-e2e.md) | **pass** — write, sign, register, resolve, verify, refuse tampering | 2026-10-07 |
| [`live-catalog-verifies`](live-catalog-verifies.md) | **pass** — the public catalog, over the real network | 2026-10-07 |
| the seven Claude Code suites | **not yet run** — they need a model credential | — |

The first `floor-make-test` run failed one check, and the failure was real: the sandbox carries a
placeholder `GH_TOKEN` that `gh auth status` accepts and the GitHub API rejects, and the test
trusted the former. It now guards on an actual read. The report above is the run after that fix.
