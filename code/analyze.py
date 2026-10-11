#!/usr/bin/env python3
"""Analyze repo-age-rows.jsonl: launch-age distribution + pairing. Prints compact stats."""
import json, os, statistics, collections
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROWS = os.path.join(HERE, 'data/repo-age-rows.jsonl')

def days(a, b):
    try:
        return (datetime.fromisoformat(a.replace('Z', '+00:00')) - datetime.fromisoformat(b.replace('Z', '+00:00'))).total_seconds() / 86400
    except Exception:
        return None

rows = [json.loads(l) for l in open(ROWS)]
ok = [r for r in rows if r.get('status') == 'ok']
dead = [r for r in rows if r.get('status') != 'ok']
print(f'collected {len(rows)} | ok {len(ok)} | dead/err {len(dead)} ({collections.Counter(r.get("status") for r in dead)})')
for r in ok:
    r['age_days'] = days(r['hn_date'] + 'T12:00:00Z', r['created_at'])
ok = [r for r in ok if r['age_days'] is not None and r['age_days'] >= 0]
neg = len([r for r in ok if False])
bands = {'1-49': lambda p: p < 50, '50-199': lambda p: 50 <= p < 200, '200-499': lambda p: 200 <= p < 500, '500+': lambda p: p >= 500}
built_for_launch = lambda age: age <= 14
print()
print(f'{"band":8} {"n":>4} {"median age":>10} {"<=14d":>6} {"<=30d":>6} {"median stars":>12}')
for b, f in bands.items():
    sub = [r for r in ok if f(r['points'])]
    if not sub: continue
    ages = sorted(r['age_days'] for r in sub)
    med = statistics.median(ages)
    le14 = 100 * sum(1 for a in ages if a <= 14) / len(ages)
    le30 = 100 * sum(1 for a in ages if a <= 30) / len(ages)
    mstars = statistics.median([r['stars_now'] for r in sub])
    print(f'{b:8} {len(sub):>4} {med:>9.0f}d {le14:>5.0f}% {le30:>5.0f}% {mstars:>12.0f}')
print()
years = sorted({r['hn_date'][:4] for r in ok})
print(f'{"year":6} {"n":>4} {"median age":>10} {"<=14d":>6}')
for y in years:
    sub = [r for r in ok if r['hn_date'].startswith(y)]
    ages = sorted(r['age_days'] for r in sub)
    print(f'{y:6} {len(sub):>4} {statistics.median(ages):>9.0f}d {100*sum(1 for a in ages if a<=14)/len(ages):>5.0f}%')
print()
fresh = [r for r in ok if r['age_days'] <= 14]
old = [r for r in ok if r['age_days'] > 14]
if fresh and old:
    for name, grp in (('age<=14d', fresh), ('age>14d', old)):
        pts = sorted(r['points'] for r in grp)
        print(f'{name:9} n={len(grp):>4} median points {statistics.median(pts):>5.0f} | median stars_now {statistics.median([r["stars_now"] for r in grp]):>6.0f}')
forks = sum(1 for r in ok if r.get('fork'))
print(f'\nforks in sample: {forks} | archived: {sum(1 for r in ok if r.get("archived"))}')
top10 = sorted(ok, key=lambda r: -r['stars_now'])[:10]
print('\ntop stars_now:')
for r in top10:
    print(f"  {r['full'][:42]:42} {r['stars_now']:>7} stars | age at post {r['age_days']:>4.0f}d | {r['points']:>4} pts | {r['hn_date']}")
