# Guide — keep a catalog fresh

**When:** your catalog's manifest is about to expire, or a client reports it expired.

Every manifest carries `not_after`. Past it, every verifying client refuses the catalog — a signature
stays valid forever, and expiry is what stops an old signed manifest from being replayed (FPA M6a).
The default window is 30 days.

```
cd ~/path/to/catalog
fp-index --renew      # moves not_after; the serial changes only if the frompts did
fp-sign
git add index.json index.json.sig INDEX.md && git commit -m "renew manifest" && git push
```

The window is the catalog's `validity_days` in `frompt-catalog.json` (`FPA_VALIDITY_DAYS`
overrides it for one run), at most 90 days: `fp-index` refuses a longer one. `fp-index --renew`
refuses as well when the documents differ from the manifest, so a renewal never publishes new
content.

## Or let CI do it

A catalog made with `fp-init-catalog` carries `.github/workflows/renew.yml`. Once a week it checks
the manifest and, when fewer than ten days remain, renews and signs it, then commits. It needs the
private key as the secret `FPA_SIGNING_KEY` (the contents of `.fpa/signing_key`) of the
**environment** `frompt-signing`, not as a repository secret. Set it up yourself, in the
repository settings under Environments:

1. create the environment `frompt-signing`;
2. add **required reviewers**, so every renewal waits for a person to approve it;
3. limit its deployment branches to the default branch;
4. add the secret `FPA_SIGNING_KEY` to the environment.

GitHub creates a missing environment the first time a job names it, with no protection at all, so
the job checks for required reviewers itself and does not sign without them. Without the secret
it only warns. It re-signs only a manifest its own key already signed, and only with the documents
unchanged.

That is a trade: the key then lives with your CI provider, and anything that can run a workflow in
that repository can sign for your domain. If that is not acceptable, leave the secret unset and
renew by hand.

Check when it ends:

```
python3 -c "import json; print(json.load(open('index.json'))['not_after'])"
```

`fp-verify` also warns when a manifest it accepts expires within three days. A catalog nobody renews
stops working on its own, on purpose: that is the half of freshness that needs no memory on the
client's side.
