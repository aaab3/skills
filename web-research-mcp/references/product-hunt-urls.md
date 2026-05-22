# Product Hunt · Firecrawl URL

> 完整 SOP：`product-hunt-commenter/references/firecrawl-sop.md`

| 目的 | URL | scrape 参数 |
|------|-----|-------------|
| 产品 + launch | `https://www.producthunt.com/products/{slug}` | `onlyMainContent: true`, `waitFor: 8000`, `timeout: 90000` |
| 评论摘要 | `https://hunted.space/product/{slug}` | `onlyMainContent: false`, `waitFor: 5000` |

**成功标志：** PH 页含 launch 标题 / maker；hunted 含 `Comment highlights`。

**做不到：** 未登录 PH 讨论全文（常停在 Login to comment）。
