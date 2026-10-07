# Tutorial 1 — adopt your first frompt

**You end with:** an agent that adopted a frompt, said so in one line, behaved differently because
of it, and let it go when you told it to.

**You need:** any coding agent that can fetch a URL and run a shell command — Claude Code, Codex,
Gemini, and others. Nothing to install.

## 1. Hand it the URL alone

```
https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/repo-recon/1.1.0.frompt.md
```

A conforming agent fetches it, tells you what it is, and **does not adopt it**: a URL is not
consent. That refusal is the protocol working.

## 2. Read to the end, and get the digest

Open the URL in a browser and read it. Its last section, `## Consent`, holds a sentence written for
this frompt. Then compute the first seven characters of the document's SHA-256:

```
curl -fsS https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/repo-recon/1.1.0.frompt.md | shasum -a 256 | cut -c1-7
```

`-f` matters: without it a failed fetch hashes empty input and prints `e3b0c44`.

## 3. Send the phrase

Replace `<digest>` in the sentence with what you computed, and send it with the URL:

```
i-have-read-this-prompt-and-let-it-map-my-repository-read-only-repo-recon-31c1785 https://raw.githubusercontent.com/frompt-org/catalog/main/prompts/repo-recon/1.1.0.frompt.md
```

The agent fetches the bytes itself, hashes them, and adopts only if the digests match:

```
ADOPTED: repo-recon v1.1.0
```

## 4. Ask what is steering it

```
what is adopted?
```

It should name the frompt, its version, where it came from, and when it ends.

## 5. Let it go

```
disown repo-recon
```

It stops, and says what is no longer true. Nothing was installed, and nothing is left behind.

## How the phrase works

The pilot sends a **confirmation phrase** with the URL. The phrase is built from up to three parts, and each part proves a different thing:

```
i-have-read-this-prompt-and-let-it-map-my-repository-read-only-repo-recon-31c1785  <url>
└──────────────── 1. consent sentence ─────────────────────────┘ └── 2. id ──┘ └3. digest┘
```

| Part | Where it comes from | What it establishes |
|---|---|---|
| **consent sentence** | written by the author, published **only in the document's last section** | the pilot reached the end of the document and read a sentence saying what they are about to do |
| **prompt id** | the document's `id` | *this* prompt, not another |
| **digest** | **computed** — a document cannot contain its own hash | the pilot possessed these exact bytes |

Three properties fall out of that, and they are the whole design:

1. **It cannot be guessed.** The sentence is specific to this prompt and deliberately not standardized — a protocol-wide sentence would become muscle memory, and muscle memory is what ceremony exists to prevent.
2. **It cannot be pasted innocently.** You are typing a first-person sentence stating what you are agreeing to. Pasting that without reading should feel wrong, the way typing a repo name to delete it feels wrong.
3. **It is bound to the bytes.** The agent recomputes the digest over what *it* fetched. If a server showed you one document and your agent another, the hashes disagree and it refuses. **This is the only rule in the protocol that needs no goodwill once a client computes it** — at level 0 the agent runs the hash itself and could misreport it ([`CLIENT.md`](../../CLIENT.md)); everything else is a convention an agent follows.

How much of that a prompt demands is the author's call, declared as `ceremony` and scaled to the ask:

| `ceremony` | Phrase | For |
|---|---|---|
| `light` | sentence only | a rubric that reads and argues |
| `standard` | + id + 7 hex | anything that acts |
| `strict` | + id + full 64 hex | writes, network, anything irreversible |

A URL with **no** phrase is not an adoption. The agent previews it — names the prompt, says what it does, points at the document for the sentence — and waits. It never recites the sentence, because handing it over would empty the ceremony of the thing it is for.

**Next:** [Tutorial 2 — write a frompt](02-write-a-frompt.md).
