# Tutorial 3 — publish a catalog

**You end with:** a signed catalog that anyone can verify against your key, served from a repo or any
static host.

The fastest way to see the whole thing is [example 06](../../examples/06-catalog-end-to-end/README.md),
which does every step below on a throwaway copy and runs in seconds.

## 1. Stage the frompts you mean to publish

```
bin/fp-publish ~/path/to/your-catalog --only my-frompt
```

Name what you publish. Without `--only`, every frompt in this repository is staged, including ones
another author added here but never chose to publish.

## 2. Index and sign, in the catalog

```
bin/fp-index
bin/fp-sign --keygen      # once: makes .fpa/signing_key, which never leaves the machine
bin/fp-sign
```

Commit `index.json`, `index.json.sig`, `allowed_signers` and the documents together.

## 3. Give people your key out of band

Your `allowed_signers` line is how clients will trust you. They must get it from you, not from the
catalog it is used to check.

## What a catalog is

A **catalog** is a published set of prompts — a signed manifest and the documents it lists, served as static files:

```
<base>/index.json
<base>/prompts/<id>/<version>.frompt.md
```

That is the whole standard, and it is a **shape rather than a privilege**: anyone who can serve files can publish one, and no catalog is more official than another. The org's catalog lives at [`frompt-org/catalog`](https://github.com/frompt-org/catalog), under an org whose [profile page](https://github.com/frompt-org/.github) is the thirty-second version of this README; a company publishes `acme/prompts` and serves it wherever they already serve static files.

A client may adopt from several. Each carries its own freshness floor and is trusted through its own publisher key — held locally, never fetched from the catalog it validates.

Finding a catalog you do not already know is a different layer — a **directory** of catalogs, specified in [`DIRECTORY.md`](https://github.com/frompt-org/frompt/blob/main/DIRECTORY.md) and not built. It lists; it never authorizes.

`bin/fp-publish <catalog>` stages this repo's prompts into a catalog checkout and tells you what to run there. It refuses to overwrite a published version with different bytes, because that is the one rule everything else rests on.

## The index, and what it deliberately withholds

[`INDEX.md`](../../INDEX.md) publishes every prompt's **digest** — legitimate out-of-band conveyance of the one part a document cannot contain. It does **not** publish consent sentences.

So the index gives you part three, the document gives you part one, and you need both. An index that handed over whole phrases would be a copy-paste machine for the ceremony this protocol exists to create.

## Transports — a catalog need not be public

How bytes arrive is not the protocol's business. The digest is the constant; the fetcher is pluggable, so `base` can be any of:

```
https://raw.githubusercontent.com/frompt-org/catalog/main     public, anonymous
gh:frompt-org/catalog@main                                    the GitHub API, your own credential — works for a private catalog too
https://prompts.acme.internal                              your own static server
/opt/prompts                                               a path, airgapped
```

`gh:` is the one that matters for a private catalog. It fetches through the GitHub API with the caller's own credential and returns the blob, not a rendering of it — verified byte-identical to the raw file, which is what makes the digest still mean something:

```
$ bin/fp-verify repo-recon --from gh:frompt-org/catalog@main
manifest verified: index.json signed by frompt-catalog SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
authorized: repo-recon v1.1.0 digest 31c1785acb46 contexts [interactive, registered, managed] serial 5 expires 2026-11-05T15:05:25Z
```

Signature, freshness and digest, against a repository nobody can read without permission. **Publishing is a decision about audience, not a prerequisite for the protocol working.**

One caveat worth stating: a credentialed transport makes the *fetcher's* identity part of the story. For a fleet, that means a token per agent — a fine-grained PAT scoped to the catalog repo is the right granularity, and GitHub logs every read, which is an audit trail you get for free.

**Next:** [Tutorial 4 — run unattended](04-run-unattended.md).
