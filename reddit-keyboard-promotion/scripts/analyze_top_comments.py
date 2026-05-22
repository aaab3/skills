#!/usr/bin/env python3
"""One-off: scrape top comments from Reddit JSON for pattern research."""
import json
import re
import urllib.request

UA = "Mozilla/5.0 (reddit-research/1.0)"
THREADS = [
    ("cursor_usage", "https://www.reddit.com/r/cursor/comments/1ti2z4p.json?limit=50&sort=top"),
    ("budget_kb", "https://www.reddit.com/r/keyboards/comments/1q77x4g.json?limit=50&sort=top"),
    ("he_appeal", "https://www.reddit.com/r/MechanicalKeyboards/comments/1ewyqf8.json?limit=50&sort=top"),
    ("via_qmk", "https://www.reddit.com/r/keyboards/comments/1c3phmh.json?limit=50&sort=top"),
    ("mousepad_build", "https://www.reddit.com/r/MechanicalKeyboards/comments/1s2qvjy.json?limit=50&sort=top"),
    ("model_m", "https://www.reddit.com/r/MechanicalKeyboards/comments/1jq98ma.json?limit=50&sort=top"),
    ("stab_rattle", "https://www.reddit.com/r/MechanicalKeyboards/comments/y6alba.json?limit=50&sort=top"),
]


def fetch(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def word_count(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", s or ""))


def tags(body: str) -> list[str]:
    b = (body or "").lower()
    w = word_count(body)
    t = []
    if w <= 15:
        t.append("short")
    elif w <= 60:
        t.append("mid")
    else:
        t.append("long")
    if re.search(r"https?://|docs\.|cursor\.com|github\.com", b):
        t.append("sourced")
    if body.count("?") >= 2:
        t.append("multi_q")
    elif "?" in body:
        t.append("question")
    if re.search(r"\$[0-9]|\b[0-9]+%|\b\d+\s*(usd|dollars|bucks)", b):
        t.append("numbers")
    if any(x in b for x in ("tl;dr", "edit:", "step 1", "first,", "1.", "2.")):
        t.append("structured")
    if any(x in b for x in ("same here", "me too", "happened to me", "i also", "i had the same")):
        t.append("me_too")
    if any(x in b for x in ("lol", "lmao", "unhinged")):
        t.append("meme")
    if any(x in b for x in ("if you", "depends on", "tradeoff", "unless", "in your case", "your mileage")):
        t.append("caveat")
    if any(x in b for x in ("try ", "check ", "settings", "dashboard", "disable", "go to")):
        t.append("actionable")
    if any(x in b for x in ("not a reset", "actually", "misconception", "the reason")):
        t.append("reframe")
    return t


def main():
    for name, url in THREADS:
        try:
            data = fetch(url)
            post = data[0]["data"]["children"][0]["data"]
            title = (post.get("title") or "")[:75]
            comments = [
                c["data"]
                for c in data[1]["data"]["children"]
                if c["kind"] == "t1" and c["data"].get("body")
            ]
            comments.sort(key=lambda x: x.get("score", 0), reverse=True)
            print(f"\n=== {name} | {title} ===")
            for c in comments[:12]:
                body = re.sub(r"\s+", " ", c["body"]).strip()
                preview = body[:260] + ("..." if len(body) > 260 else "")
                tg = ",".join(tags(body))
                print(
                    f"[{c['score']:4d} w={word_count(body):3d} {tg:28s}] "
                    f"{c['author']}: {preview}"
                )
        except Exception as e:
            print(f"FAIL {name}: {e}")


if __name__ == "__main__":
    main()
