# Research Protocol

> **Current date: May 2026.** All searches should prioritize results from late 2025 and 2026. Models, prices, and community opinions change fast — do not rely on information known to be older than 6 months.

Use research to make the comment specific and factually safe. Do not research every obvious term, but always research unfamiliar or current facts.

## Thread context first (before web search)

For each post link, load existing discussion **before** drafting comments:

1. **Reddit JSON** (new posts): `https://www.reddit.com/r/{sub}/comments/{post_id}.json?limit=200` — OP + current top comments.
2. **PullPush archive API** (tested; may lag on fresh comments): see `pullpush-api.md`
   - Same thread: `link_id=t3_{post_id}` + `subreddit={name}`
   - Broader sentiment: `q="model or issue"` + `subreddit=...`
3. **Web search** (this doc) — only when specs, prices, or facts are still unclear.

Do not repeat angles already covered by highly upvoted comments unless adding a clearly different caveat or fix.

## Search When

Search before writing if the post includes:

- an unfamiliar keyboard model, brand, switch, keycap set, or vintage board
- a technical claim about layout, switch type, mount style, firmware, wireless latency, VIA/QMK support, or compatibility
- **any comment that names specific products to recommend** (including HE / V2 / Max / Ultra suffixes) → also run **`product-recommendation-playbook.md` §4** connectivity table
- OP asks **wireless**, **like Mode**, **alternatives to {brand}**, or **gift/budget pick**
- current price, availability, group buy, pre-order, or discount
- strong community opinion, such as "best", "worst", "overrated", "worth it"
- subreddit rules, flair requirements, or whether a post is allowed
- missing context that changes the answer

## Search Queries

Prefer targeted queries:

```text
site:reddit.com "MODEL" keyboard
site:reddit.com/r/MechanicalKeyboards "MODEL"
"MODEL" mechanical keyboard review
"SWITCH NAME" switch feel reddit
"KEYCAP PROFILE" keycaps reddit
"ERROR OR ISSUE" mechanical keyboard reddit
"BRAND MODEL" VIA QMK
```

For vintage boards:

```text
"MODEL" keyboard deskthority
"MODEL" keyboard geekhack
site:reddit.com "MODEL" "keyboard"
```

## Extract

From search results, capture only what helps the comment:

- what the item is
- common sentiment in the community
- 1-2 concrete pros
- 1-2 concrete cons or caveats
- whether the claim is uncertain or debated

Do not turn research notes into a long explanation unless the user asks for analysis.

## Reliability Rules

- Prefer recent Reddit threads for current sentiment.
- Prefer vendor/docs/wiki pages for specifications.
- Prefer multiple sources when making a strong claim.
- Mark uncertainty when sources conflict.
- Never invent specs, switch types, prices, or personal ownership.

## Search-To-Comment Pattern

1. Search the exact model/topic.
2. Reduce findings to 2-4 facts.
3. Pick only the fact that matters to the OP.
4. Write a short comment that sounds like a response to the thread, not a research report.

**Type D（推荐）：** 在步骤 1 前完成 OP 合同 + 产品轴（`product-recommendation-playbook.md` §1–§2）。每个具名 SKU 在步骤 2 中必须含 **Connection: wired / 2.4G+BT / …** 一行。
