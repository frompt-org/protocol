# Guide — revoke a published version

**When:** a published frompt is wrong in a way a newer version cannot fix for people who already
pinned it — it teaches the wrong protocol, or it permits what the spec forbids.

A published version's bytes never change, so you do not edit it. You publish a fixed version and
drop the bad one from the manifest. Revocation is dropping an entry (FPA M4).

```
# in this repository
cp prompts/repo-recon/1.0.0.frompt.md prompts/repo-recon/1.1.0.frompt.md   # then fix it, bump version and handshake
git rm prompts/repo-recon/1.0.0.frompt.md
bin/fp-index && bin/fp-sign && bin/fp-lock && make test

# in the catalog
bin/fp-publish ~/path/to/catalog --only repo-recon     # from this repository
cd ~/path/to/catalog && git rm prompts/repo-recon/1.0.0.frompt.md
bin/fp-index && bin/fp-sign
```

What happens to people already using it:

- **Interactive pilots** holding the old phrase can still adopt the old URL if it is still served —
  so stop serving it, which `git rm` does.
- **Registered clients** resolving `@latest` move to the new version on their next run.
- **Clients pinned to the revoked version** are refused, because it is no longer in the manifest.
  They re-pin deliberately with `bin/fp-lock --update <id>`.

Write the reason in the commit message. The bytes stay in git history, which is the record.
