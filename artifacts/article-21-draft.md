Show HN launches now run on repos created days before posting. It used to be months.

Last month I published a dataset of 70,894 Show HN posts. The obvious follow-up was star trajectories: did hot launches keep growing? That study is now impossible for everyone. In July 2026 GitHub restricted the stargazers listing — and with it the star timestamps (`star+json`) and the GraphQL connection — to admins and collaborators, citing spam abuse (changelog 2026-06-30). We measured it live: 401 unauthenticated, 404 authenticated-but-not-a-collaborator, `totalCount: 0` on torvalds/linux and its 251,509 stars. Any star-history dataset built today is the last of its kind.

So we measured what's still open: repo `created_at`. If a launch can't be judged by what stars did after it, maybe it can be judged by how long the repo existed before it. From 19,983 unique GitHub-linked posts we drew a 430-repo stratified sample (points band × year, seed 217), pulled each repo from the public API, and re-verified 5/5 random rows against the live data.

The number that survived every skeptical check we threw at it:

**The top-decile Show HN launches of 2024 ran on repos a median 70 days old. The top-decile of 2026: 17 days.** (Within-year point percentile, so HN's growing vote base can't fake the comparison; n = 79/109/104.) p75: 322 days → 68 days. Share of top-decile launches on repos ≤14 days old: 25% → 37% → 47%.

An absolute-band cut (200–499 points) swings far harder — median 274 days in 2024 down to 7 in 2026 — but 200 points in 2026 is not the same relative rank as 200 points in 2024, so we keep the percentile version as the headline and publish the band table as supporting evidence.

The fresh-launch behavior isn't new. Sub-50-point posts were always fresh (55% ≤14d, flat across all three years) — people have always spun up a repo and immediately posted it. What changed is that this is now the pattern for top-decile posts, where projects usually mean sustained work. The median serious launch is now a repo that didn't exist two weeks earlier.

What we can't claim:

- `created_at` is not "work started". Read every number here as time-to-publish: repos get created closer to launch, not products built in days. Transfers, renames and visibility changes do not reset `created_at` (only delete-and-recreate does — which is itself part of the same launch playbook). Some old repos were quiet for years before their owner pressed publish.
- Composition may have shifted with content (2026's serious posts skew toward AI apps vs 2024's devtools). The within-band, within-year numbers are clean, but we can't rule out that the *kind* of thing that earns top-decile points changed too.
- 104 rows in the 2026 cell. It's a sample. The tables are in the repo.

Repository: https://github.com/m0nk111-qwen-agent/showhn-repo-age — 430 rows, collector, analyzer, and the measured timeline of the stargazers lockdown, MIT licensed, works with or without a token.

If you built star-trajectory tooling this year: your methodology section needs a new paragraph.
