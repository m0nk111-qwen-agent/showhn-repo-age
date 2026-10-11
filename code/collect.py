#!/usr/bin/env python3
"""C-NEW-92 (pivoted) collector: repo-age at Show HN launch.
Resumable; appends one JSON row per repo to data/repo-age-rows.jsonl.
Measures (all from GET /repos — still public, verified 200): created_at, pushed_at,
stargazers_count, fork, language, archived. Paired offline with HN post date/points.
NOTE (documented 2026-10-11): /repos/{o}/{r}/stargazers is admin/collaborator-only
since Jul 2026 (github.blog changelog 2026-06-30) -> star TIMESTAMPS unavailable;
this pivot uses launch-age instead. Auth via existing PAT (never printed)."""
import json, os, time, random, urllib.request, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, 'data/repo-age-sample.json')
OUT = os.path.join(HERE, 'data/repo-age-rows.jsonl')
PATFILE = '/workspace/data/credentials/gh-pat-token.txt'

def main():
    pat = open(PATFILE).read().strip()
    H = {'User-Agent': 'pennyforge-repo-age', 'Authorization': f'Bearer {pat}'}
    repos = json.load(open(SAMPLE))
    done = set()
    if os.path.exists(OUT):
        for line in open(OUT):
            try: done.add(json.loads(line)['full'])
            except Exception: pass
    todo = [r for r in repos if f"{r['owner']}/{r['repo']}" not in done]
    print(f'todo {len(todo)} / {len(repos)}', flush=True)
    for i, r in enumerate(todo):
        full = f"{r['owner']}/{r['repo']}"
        row = dict(r); row['full'] = full
        req = urllib.request.Request(f'https://api.github.com/repos/{full}', headers=H)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                d = json.loads(resp.read())
                row.update({'status': 'ok', 'created_at': d.get('created_at'), 'pushed_at': d.get('pushed_at'),
                            'stars_now': d.get('stargazers_count'), 'fork': d.get('fork'),
                            'language': d.get('language'), 'archived': d.get('archived')})
        except urllib.error.HTTPError as e:
            row.update({'status': f'http-{e.code}'})
        except Exception as e:
            row.update({'status': f'err-{str(e)[:40]}'})
        with open(OUT, 'a') as f:
            f.write(json.dumps(row) + '\n')
        if (i + 1) % 25 == 0:
            print(f'{i+1}/{len(todo)}', flush=True)
        time.sleep(0.4 + random.random() * 0.3)  # ~2/s, far under 5000/h
    print('done', flush=True)

if __name__ == '__main__':
    main()
