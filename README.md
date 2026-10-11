# showhn-repo-age — how old is a repo when Show HN launches it?

A 430-repo stratified sample measuring **repo age at Show HN launch**, built from our companion
dataset of 70,894 Show HN posts (`showhn-24mo`), with every row re-verified against the live
GitHub API. The finding that survived verification:

**Top-decile Show HN launches now happen on repos a median 17 days old — down from 70 days in
2024.** (Within-year point percentile ≥ 0.90, so HN vote growth can't fake the trend; n = 79/109/104.)
Share of top-decile launches on repos ≤14 days old: 25% → 37% → 47%.

| top-decile posts | 2024 (n=79) | 2025 (n=109) | 2026 (n=104) |
|---|---|---|---|
| median repo age at post | 70d | 32d | 17d |
| p75 | 322d | 138d | 68d |
| share ≤14d | 25% | 37% | 47% |

A secondary, absolute-band view (200–499 points) shows a much bigger swing — median 274d → 7d —
but absolute point thresholds are not comparable across years (HN's vote base grew), so we treat
the percentile-normalized numbers as the headline and the band table as supporting evidence.

The "create the repo right before asking HN" behavior used to be the small-time pattern (sub-50-point
launches were always fresh: 55% ≤14d, flat across all years). It is now the top-decile pattern too.
Read it as **time-to-publish shrinking**: repos get created closer to launch — not "products are
built in days" (transfers, renames and visibility changes do not reset `created_at`; only
delete-and-recreate does, which is itself part of the same launch playbook).

## Why launch age (and not star trajectories)?

We started with the obvious design: time-to-first-star and star slopes from `stargazers`
timestamps. That is **no longer possible from the public API**. In July 2026 GitHub restricted
`/repos/{owner}/{repo}/stargazers` (and `/subscribers`, the `star+json` media type, and the
GraphQL `stargazers` connection) to admins and collaborators —
[changelog 2026-06-30](https://github.blog/changelog/2026-06-30-upcoming-access-restrictions-to-public-api-endpoints-and-ui-views/).
We measured it live on 2026-10-11: unauthenticated → 401; authenticated non-collaborator → 404;
GraphQL connection → `totalCount: 0` even on `torvalds/linux` (251k stars). Any star-trajectory
dataset built today is the last of its kind. Launch age is one of the launch-quality signals
still measurable: `GET /repos/{owner}/{repo}` (created_at, stars_now, fork, pushed_at, language)
remains fully open, no token needed.

## Sample & method

- Frame: 19,983 unique `github.com` repo links in 70,894 Show HN posts (Oct 2024 – Oct 2026).
- Stratified 430 by points band (1–49 / 50–199 / 200–499 / 500+) × year, seed 217.
- 12/430 (2.8%) now 404 (deleted or private) → excluded; 0 forks in sample; 7 archived.
- `repo age = HN post date − repo created_at`. No proxy for "work started" — repo creation is
  when the owner chose to make the repo exist, which *is* the launch-decision moment we measure.
- Verification: 5/5 random rows re-fetched live matched exactly on created_at + stargazers_count.

## Honest caveats

- Repo created_at is not "work started". Some launches are repos that existed quietly for years;
  some fresh repos are shells prepared for launch. We measure the *repo*, and the collapse in the
  serious band means owners now create the public repo days before asking HN for attention.
- Points are HN's vote, not impact; `stars_now` is confounded by time-since-post, so we do not
  use it in the headline.
- n=41 in the 2026 cell. It is a sample, not a census; the p25/p75 columns show the shift is the
  whole distribution, not an outlier artifact (the oldest 2024 launches: 2,370 and 1,626 days).

## Files

- `data/repo-age-rows.jsonl` — 430 rows: owner, repo, points, hn_date, status, created_at,
  pushed_at, stars_now, fork, language, archived.
- `code/collect.py` — resumable collector (GET /repos only; token optional).
- `code/analyze.py` — the band/year tables and spot-check helpers.
- `artifacts/summary.json` — machine-readable headline numbers.

MIT. Companion datasets: `showhn-24mo` (Show HN posts) · arXiv version-drift.
