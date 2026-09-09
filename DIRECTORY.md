# Directory — discovery across catalogs

A **catalog** lists the prompts of one publisher. A **directory** lists catalogs, so that a
pilot who does not already know a publisher can find one. It is the layer that makes
*accessible from outside* true, and it is not built. This document fixes its rules before
anyone builds it, because the one that matters most is easy to get wrong for convenience.

The intended instance is `f-prompts.io`. The domain is unregistered.

## 1. Three things called index

| Word | Means | Lives |
|---|---|---|
| **manifest** | `index.json` — one catalog's signed, machine-readable prompt list | in the catalog |
| **catalog index** | `INDEX.md` — the same list for people, with digests and without consent sentences | in the catalog |
| **directory** | a list of *catalogs*, across publishers | its own host |

This repository used *index* for the third thing once. It does not any more.

## 2. Rules

- **D1.** A directory lists catalogs: a name, the `base`, the signing key's fingerprint, and
  when the entry was made. It **MAY** additionally cache each catalog's manifest to make
  search possible, and what it shows from that cache is what the manifest carries — `id`,
  `version`, `digest`, `ceremony`, `contexts`, envelope.
- **D2.** A directory **MUST NOT** publish consent sentences. The sentence lives in the
  document's final section and nowhere else; a directory that surfaced it would be the
  copy-paste machine the ceremony exists to prevent (§C3, §PV1). Same rule as `INDEX.md`, one
  level up.
- **D3.** A directory **MUST NOT** rank. Entries are ordered by name. Popularity, recency and
  "verified" badges are all a verdict, and [`FPA.md`](FPA.md) §15 already settled that this
  project publishes observations and never verdicts.
- **D4.** Listing is not admission and not endorsement; removal is not revocation. A catalog
  works exactly the same whether or not any directory lists it — that is what *a shape, not a
  privilege* means — and a directory operator who could switch a catalog off would be a
  registry, which [`VISION.md`](VISION.md) says this is not.
- **D5.** **Discovery is not authorization.** A client **MUST NOT** adopt from a catalog because a
  directory listed it. Registration still happens per catalog, by the pilot, recorded (§AC2a).
  A directory answers *what exists*; it never answers *may I*.
- **D6.** The fingerprint in an entry is a claim by the directory's operator, nothing more. A
  client that trusts the operator **MAY** take it as the catalog's trust root; one that does
  not obtains the key elsewhere. §M7 still holds — the key is never fetched from the catalog
  it validates — and a directory is a different host, which is why it can carry the claim at
  all. Whether to believe it is the pilot's decision, and the entry must make it visible that
  there is one to make.
- **D7.** A directory is itself a deterministic, signed document — the same shape as a
  manifest, so the same client code verifies it, and the same freshness rules apply (§M1,
  §M6, §M6a). Anyone can publish one. There are meant to be several.

## 3. What a search returns

```
<catalog name>  <base>  <id>@<version>  <digest>  <ceremony>  <contexts>
```

Enough to register the catalog and resolve the prompt. Never enough to adopt it — the
sentence is still behind the document, and the registration is still an act.

## 4. Status

Not built. No domain. The rules above are the specification; the first implementation is a
static `directory.json` plus a page that renders it, published by whoever registers the
domain, and it should be the second directory rather than the only one within a year.
