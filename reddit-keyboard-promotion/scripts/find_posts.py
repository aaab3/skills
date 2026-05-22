#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timezone

UA = "script:reddit-draft-research/1.0"
subs = ["keyboards", "BudgetKeebs", "MechanicalKeyboards"]
keywords_help = [
    "help", "recommend", "which", "advice", "issue", "problem",
    "buy", "budget", "fix", "broken", "question", "worth", "switch",
]


def fetch(sub, sort="new", limit=30):
    url = f"https://www.reddit.com/r/{sub}/{sort}.json?limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return json.load(r)


now = datetime.now(timezone.utc)
candidates = []
for sub in subs:
    try:
        data = fetch(sub)
        for p in data["data"]["children"]:
            d = p["data"]
            if d.get("stickied") or d.get("over_18"):
                continue
            age_h = (now.timestamp() - d["created_utc"]) / 3600
            if age_h > 96:
                continue
            title_l = d["title"].lower()
            flair = (d.get("link_flair_text") or "").lower()
            is_help = any(k in title_l or k in flair for k in keywords_help) or "help" in flair
            nc = d["num_comments"]
            score = 0
            if sub == "keyboards":
                score += 3
            if is_help:
                score += 4
            if nc <= 5:
                score += 5
            elif nc <= 15:
                score += 2
            if age_h <= 12:
                score += 3
            elif age_h <= 24:
                score += 1
            if nc == 0:
                score += 2
            candidates.append(
                {
                    "score": score,
                    "sub": sub,
                    "id": d["id"],
                    "title": d["title"],
                    "flair": d.get("link_flair_text"),
                    "comments": nc,
                    "age_h": round(age_h, 1),
                    "selftext": (d.get("selftext") or "")[:600],
                    "url": f"https://www.reddit.com/r/{sub}/comments/{d['id']}/",
                }
            )
    except Exception as e:
        print(f"FAIL {sub}: {e}")

candidates.sort(key=lambda x: -x["score"])
for c in candidates[:20]:
    line1 = (
        f"{c['score']:2d} | {c['comments']:3d}c {c['age_h']:5.1f}h | "
        f"r/{c['sub']} | {c['flair']} | {c['title'][:75]}"
    )
    print(line1)
    print(f"    {c['url']}")
    if c["selftext"]:
        op = c["selftext"][:150].replace("\n", " ")
        print(f"    OP: {op}")
    print()
