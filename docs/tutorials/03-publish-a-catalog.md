# Tutorial 3 — host a catalog on your own domain

**You end with:** your own frompts, signed with your own key, served from your own domain — and
clients that accept your domain as a frompt source because they checked your key's fingerprint.

You need a clone of this repository with `bin/` on your `PATH` ([`AGENTS.md`](../../AGENTS.md)),
`python3`, `ssh-keygen`, and somewhere that serves static files. Nothing to fork, no account with
anyone. [Example 08](../../examples/08-host-your-own-catalog/README.md) plays the whole story on
throwaway directories in a few seconds, including the attacks it refuses.

## 1. Start the catalog

```
fp-init-catalog ~/my-catalog --url https://frompts.example.com
```

That makes an empty catalog that is already signed, so the first thing you serve is valid:

```
frompt-catalog.json   where it is served from, the signing identity, summaries for INDEX.md
prompts/              your frompts go here, as prompts/<id>/<version>.frompt.md
index.json, .sig      the manifest and its signature
allowed_signers       your public key, served beside the manifest
.fpa/signing_key      your private key: gitignored, never committed, never served
.nojekyll, CNAME      so GitHub Pages serves the files as they are, under your domain
README.md             how to register this catalog, with your fingerprint filled in
.github/workflows/renew.yml   re-signs before the manifest expires, if you give it the key
```

**Back up `.fpa/signing_key`.** Lose it and every client has to register a new key.

## 2. Put frompts in it

```
cd ~/my-catalog
fp-new standup -c i-have-read-this-prompt-and-want-a-standup-note-written-from-my-git-log -f linear -o prompts/
$EDITOR prompts/standup/1.0.0.frompt.md
fp-lint prompts/standup/1.0.0.frompt.md
```

[Tutorial 2](02-write-a-frompt.md) covers writing one. A frompt is offered only to the
interactive context by default; add `contexts: interactive, registered` to its front matter if
clients may adopt it unattended after registering your catalog. To publish one of this
repository's frompts, run `fp-publish ~/my-catalog --only <id>` from this checkout.

## 3. Index and sign

```
fp-index && fp-sign
```

Standing anywhere inside the catalog, the tools find it by its `frompt-catalog.json`; from
elsewhere, set `FPA_CATALOG=~/my-catalog`. `fp-sign` checks its own signature and prints your
key's fingerprint.

## 4. Serve it

Commit, push, and serve the directory **byte for byte** at your URL, so that
`https://frompts.example.com/index.json` and `…/prompts/<id>/<version>.frompt.md` resolve.

- **GitHub Pages:** Settings, Pages, deploy from the branch root. `.nojekyll` stops Pages rendering
  `.md` files into HTML; `CNAME` holds your domain; point a DNS `CNAME` at `<owner>.github.io`.
- **Cloudflare Pages:** connect the repository, no build command, output directory `/`.
- **Anything static:** nginx, S3, R2, an internal host. A private catalog behind `gh:` works too.

A host that minifies, renders or transcodes is not serving your catalog. The digest covers the
bytes, so changed bytes are refused (FPA.md T1). Check what clients will get:

```
curl -fsS https://frompts.example.com/index.json | head
```

## 5. Give clients your fingerprint

Publish it somewhere that is **not** the catalog, such as your website, a repository people
already trust, or an email. A fingerprint read from the catalog it vouches for proves nothing. The
client then runs:

```
fp-register https://frompts.example.com --key SHA256:<your fingerprint> --pin version
fp-lock --update standup --from https://frompts.example.com
fp-resolve standup --from https://frompts.example.com
```

`fp-register` reads `<url>/allowed_signers` and trusts the key only if it has that fingerprint
(FPA.md M7a). It then verifies the catalog, and records the URL, the key, the pin and who agreed.
From then on any other key is refused for your URL, even one the client trusts for another
catalog. [Tutorial 4](04-run-unattended.md) continues from the client's side.

## 6. Keep it fresh

A manifest expires 30 days after it is signed (`validity_days`), and clients refuse an expired
one: that is what stops an old signed manifest being replayed. Either:

- give `.github/workflows/renew.yml` the private key as the repository secret
  `FPA_SIGNING_KEY`, and it re-signs weekly once fewer than ten days remain; or
- renew by hand: `fp-index --renew && fp-sign`, then commit
  ([guide](../guides/keep-a-catalog-fresh.md)).

The first is convenient, and it means your CI provider holds a key that signs for your domain.
The second keeps the key on your machine. Choose deliberately.

## Publishing more

A published version never changes: a fix is a new version, `prompts/<id>/1.1.0.frompt.md`, with a
new consent sentence if the change is material. Run `fp-index && fp-sign` and push. Clients that
float pick it up; clients that pinned see a refusal until they re-pin, which is the point.
Withdraw a bad version by removing it from the manifest
([guide](../guides/revoke-a-version.md)).

## What a catalog is

A **catalog** is a published set of prompts — a signed manifest and the documents it lists, served as static files:

```
<base>/index.json
<base>/prompts/<id>/<version>.frompt.md
```

That is the whole standard, and it is a **shape rather than a privilege**: anyone who can serve files can publish one, and no catalog is more official than another. The org's catalog lives at [`frompt-org/catalog`](https://github.com/frompt-org/catalog); a company serves `https://frompts.acme.com` from wherever it already serves static files.

A client may adopt from several. Each carries its own freshness floor — kept per catalog *and* per signing key, so no publisher can raise another's — and each is trusted through its own publisher key, held locally and brought in by fingerprint, never on the catalog's word alone.

Finding a catalog you do not already know is a different layer — a **directory** of catalogs, specified in [`DIRECTORY.md`](https://github.com/frompt-org/frompt/blob/main/DIRECTORY.md) and not built. It lists; it never authorizes.

## The index, and what it deliberately withholds

[`INDEX.md`](../../INDEX.md) publishes every prompt's **digest** — legitimate out-of-band conveyance of the one part a document cannot contain. It does **not** publish consent sentences.

So the index gives you part three, the document gives you part one, and you need both. An index that handed over whole phrases would be a copy-paste machine for the ceremony this protocol exists to create.

## Transports — a catalog need not be public

How bytes arrive is not the protocol's business. The digest is the constant; the fetcher is pluggable, so `base` can be any of:

```
https://frompts.example.com                                   your own domain
https://raw.githubusercontent.com/frompt-org/catalog/main     public, anonymous
gh:frompt-org/catalog@main                                    the GitHub API, your own credential — works for a private catalog too
/opt/prompts                                                  a path, airgapped
```

`gh:` is the one that matters for a private catalog. It fetches through the GitHub API with the caller's own credential and returns the blob, not a rendering of it — verified byte-identical to the raw file, which is what makes the digest still mean something:

```
$ fp-register gh:frompt-org/catalog@main --key SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
registered gh:frompt-org/catalog@main
  key SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
$ fp-verify repo-recon --from gh:frompt-org/catalog@main
manifest verified: index.json signed by frompt-catalog SHA256:x4Z+wsX1wVrBt5SV/NWWgPfapXlpcmSk3rqZ36Y/rKY
authorized: repo-recon v1.1.0 digest 31c1785acb46 contexts [interactive, registered, managed] serial 8
```

Signature, freshness and digest, against a repository nobody can read without permission. **Publishing is a decision about audience, not a prerequisite for the protocol working.**

One caveat worth stating: a credentialed transport makes the *fetcher's* identity part of the story. For a fleet, that means a token per agent — a fine-grained PAT scoped to the catalog repo is the right granularity, and GitHub logs every read, which is an audit trail you get for free.

**Next:** [Tutorial 4 — run unattended](04-run-unattended.md).
