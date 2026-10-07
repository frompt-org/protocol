# Guide — keep a catalog fresh

**When:** your catalog's manifest is about to expire, or a client reports it expired.

Every manifest carries `not_after`. Past it, every verifying client refuses the catalog — a signature
stays valid forever, and expiry is what stops an old signed manifest from being replayed (FPA M6a).
The default window is 30 days.

```
cd ~/path/to/catalog
bin/fp-index --renew      # moves not_after; the serial changes only if the frompts did
bin/fp-sign
git add index.json index.json.sig INDEX.md && git commit -m "renew manifest" && git push
```

Check when it ends:

```
python3 -c "import json; print(json.load(open('index.json'))['not_after'])"
```

`fp-verify` also warns when a manifest it accepts expires within three days. A catalog nobody renews
stops working on its own, on purpose: that is the half of freshness that needs no memory on the
client's side.
