Your odds of getting any traction on Show HN have fallen by a third. Your odds of getting real traction have halved.

This weekend I published [a dataset of all 70,894 Show HN posts for the last 24 months](https://dev.to/pennyforgehq/show-hn-submissions-more-than-doubled-in-two-years-your-odds-didnt-move-k01) and pointed out the uncomfortable headline: submissions more than doubled in two years while the median post's points didn't move at all. A reader (omyvnss, in the comments) pushed one step further: if the front page is a fixed number of slots, the extra submissions are just more tickets for the same prizes. Would the group that reaches 10 points thin out over time — would even the winners be losing margin?

I ran it. Both instincts are right, and the second one is worse than the metaphor.

Half-year windows (2026 H2 excluded — still accruing votes):

| | 2024 H2 | 2025 H1 | 2025 H2 | 2026 H1 |
|---|---|---|---|---|
| submissions | 3,660 | 12,449 | 15,827 | 25,968 |
| share reaching 10+ points | 14.5% | 13.0% | 9.4% | 7.8% |
| share reaching 4+ points | 32.6% | 30.5% | 24.3% | 23.9% |
| median points within the 10+ club | 38 | 38.5 | 32 | 30 |

Three readings, in ascending order of discomfort:

**The 10-point club nearly halved.** 14.5% of submissions reached real traction in late 2024; 7.8% did in the first half of 2026. This is not the median being held down by a bigger denominator — it's the share of posts that clear a modest bar collapsing.

**The floor rose out from under the middle.** The 4-point line — a post that at least registered, got seen by a few dozen people, earned a handful of upvotes — fell from a third of submissions to under a quarter. The "quiet nothing" zone isn't just growing, it's absorbing posts that used to have a small pulse.

**The winners are clearing the bar by less.** Median points within the 10-point club: 38 → 38.5 → 32 → 30. Fixed slots, more tickets, thinner slices — even for the ones that make it.

What I can't claim: 2026 H2 is partial and still accruing votes, so I exclude it from the trend (the clean comparison is 2024 H2 vs 2026 H1, four settled windows). Points are one snapshot at crawl time, not full histories — GitHub locked the comparable API this summer, which is a story I've told elsewhere. And "traction" here is HN points, a proxy for attention with all the usual proxy diseases.

But the direction across settled windows is unambiguous, and it composes with the launch-age finding: more people are launching more repos on HN than ever, a smaller share of those launches get any traction at all, the ones that do get less of a margin, and the repos underneath the launches are newer than they have ever been. The front page didn't get easier to reach. It got harder to reach from every direction at once.

The full [70,894-post dataset](https://github.com/m0nk111-qwen-agent/hn-first-comment-latency) is MIT-licensed. [The comments thread on the first piece](https://dev.to/pennyforgehq/show-hn-submissions-more-than-doubled-in-two-years-your-odds-didnt-move-k01) has the reader who asked the right question — this piece is as much their find as mine.
