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
overrides it for one run).

## Or let CI do it

A catalog made with `fp-init-catalog` carries `.github/workflows/renew.yml`. Once a week it checks
the manifest and, when fewer than ten days remain, renews and signs it, then commits. It needs the
private key as the repository secret `FPA_SIGNING_KEY` (the contents of `.fpa/signing_key`); without
the secret it only warns. Store it yourself, in the repository settings.

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
