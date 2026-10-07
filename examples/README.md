# Examples — smallest to full

Each directory is a working example with its own README: what it shows, what it introduces, how to
run it, and what passing looks like.

| # | Example | Introduces | Real agent output? |
|---|---|---|---|
| 01 | [adopt one](01-adopt-one/README.md) | the phrase, the `ADOPTED:` line | annotated |
| 02 | [two and a disown](02-two-and-disown/README.md) | several adopted, `what is adopted?`, `disown` | annotated |
| 03 | [refuse](03-refuse/README.md) | data versus instructions, a hostile fixture that lints clean | annotated |
| 04 | [terminal game](04-terminal-game/README.md) | a frompt that is a program | **recorded** session |
| 05 | [ghost interview](05-ghost-interview/README.md) | addressing, relays, E7, disown | **recorded** session |
| 07 | [a machine that may have a ghost](07-ghost-in-the-machine/README.md) | a character with hidden state, verdict endings, character versus agent | **recorded** session |
| 06 | [catalog end to end](06-catalog-end-to-end/README.md) | publish, sign, register, resolve, verify | runnable script, run by `make test` |

*Annotated* transcripts are written to illustrate. *Recorded* ones are real agent output, copied
verbatim. Everything under [`../conformance/results/`](../conformance/results/) is real output too,
misses included.
