# Tavily vs Firecrawl 工具矩阵

| MCP 工具 | 典型参数 | 成本感 | 何时 |
|----------|----------|--------|------|
| tavily_search | query, max_results, search_depth, include_domains | 低 | 不知道 URL |
| tavily_extract | urls[], format markdown | 中 | 已有 URL 列表 |
| tavily_research | 深度题 | 高 | 用户要报告 |
| firecrawl_scrape | url, formats, waitFor, onlyMainContent | 中/页 | **已知 URL** |
| firecrawl_search | query, limit, includeDomains | 中 | 开放搜索 + 可选再 scrape |
| firecrawl_map | url, search | 中 | 找站内子页 |
| firecrawl_crawl | url, limit | 高 | 整站（慎用） |

**Reddit 帖正文：** PullPush / old.reddit / 用户粘贴 — 非本矩阵替代。
