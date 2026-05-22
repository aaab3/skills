---
name: web-research-mcp
description: >-
  Routes web research through Tavily and Firecrawl MCP (search, extract, scrape, crawl).
  Use when facts are unknown, WebFetch/Reddit JSON fails, Product Hunt or docs need scraping,
  subreddit rules change, or user asks to search/scrape/research. Requires MCP green in Cursor.
  Keys only in env vars, never in chat or files.
---

# Web 调研：Tavily + Firecrawl（MCP）

## 前提

| 检查 | 要求 |
|------|------|
| MCP | `tavily-remote-mcp` 或 `tavily-mcp-local`、`firecrawl-mcp` 在 Cursor 里 **绿点** |
| Key | `TAVILY_API_KEY` / `FIRECRAWL_API_KEY` 用户环境变量；配置见 `%USERPROFILE%\.cursor\TAVILY-MCP-SETUP.md`、`FIRECRAWL-MCP-SETUP.md` |
| 降级 | MCP 不可用时：`WebSearch` + `WebFetch`；PH 见 `product-hunt-commenter/references/firecrawl-sop.md` PowerShell |

**有 MCP 时优先 CallMcpTool**，不要只用内置 WebSearch 敷衍。

---

## 选工具（一张表）

| 你要什么 | 首选 | 次选 |
|----------|------|------|
| 不知道去哪找、要最新概况 | **tavily_search** | firecrawl_search |
| 已知 URL，要整页读/摘要 | **firecrawl_scrape** (markdown) | tavily_extract |
| 多个已知 URL | tavily_extract | 多次 firecrawl_scrape |
| 站内很多页、找子路径 | firecrawl_map → 再 scrape | tavily_crawl（慎用额度） |
| 整站爬（慎用） | firecrawl_crawl | — |
| 结构化字段（价、规格表） | firecrawl_scrape **json** + schema | — |
| Reddit **线程正文** | PullPush / 用户粘贴 | 不用 Firecrawl 代替读帖 |
| PH 产品 / hunted.space | firecrawl_scrape | 专册见下 |

---

## Tavily 用法

### tavily_search

- **默认：** `search_depth: basic`，`max_results: 5`  
- **要准：** `advanced`；**要快：** `fast`  
- **限站：** `include_domains: ["reddit.com"]` 或 `site:xxx` 写进 query  
- **时效：** `time_range: week` / `month`；或 `start_date` / `end_date`  
- **要正文：** `include_raw_content: true`（更耗额度）

### tavily_extract

- 已有 1–5 个 URL，批量拉 markdown  
- 难站：`extract_depth: advanced`

### tavily_research / tavily_crawl

- 仅用户明确要「深度调研报告」或「跟链接爬」时用；**默认不用**（慢、贵）

---

## Firecrawl 用法

### firecrawl_scrape（最常用）

**整页理解（默认）：**

```json
{
  "url": "https://example.com/page",
  "formats": ["markdown"],
  "onlyMainContent": true,
  "waitFor": 5000
}
```

- JS 重页（PH、SPA）：`waitFor: 8000–10000`  
- PH / hunted：见 `references/product-hunt-urls.md`

**抽结构化字段：** `formats: ["json"]` + `jsonOptions.prompt` + `schema`（仅当用户要表格式数据）

### firecrawl_search

- 开放问题先 search（`limit: 5`），**不要**默认带 `scrapeOptions`（易超时）  
- 看中结果后再对 **单 URL** `firecrawl_scrape`  
- 用完可调 `firecrawl_search_feedback`（带返回的 `id`）

### firecrawl_map / firecrawl_crawl

- **map：** 大文档站找含某关键词的子 URL  
- **crawl：** 用户明确要求整站；设 limit，避免烧额度

### 少用除非必要

`firecrawl_agent`、`firecrawl_browser_*`、`firecrawl_monitor_*`

---

## 标准工作流

```
1. 澄清：要「搜」还是「抓已知链接」？
2. 搜 → tavily_search 或 firecrawl_search（二选一，勿重复同 query）
3. 抓 → firecrawl_scrape / tavily_extract
4. 综合进回答；标来源 URL
5. 写 Reddit 评论前：线程仍须读 OP+评论（reddit-engagement 技能）
```

**禁止：** 未搜未抓就编事实；把搜索摘要当 Reddit 楼里已有评论。

---

## 与垂直技能衔接

| 任务 | 本技能 | 再读 |
|------|--------|------|
| Reddit 评论/发帖 | 仅补 **陌生事实、版规** | `reddit-keyboard-promotion` → `communities.md` |
| Product Hunt 评论 | **scrape PH / hunted** | `product-hunt-commenter` + `references/firecrawl-sop.md` |
| 键盘型号/价格 | search + 必要时 scrape 官网 | 评论里仍标 🟡/🔴 |

---

## 场景速查

| 场景 | 动作 |
|------|------|
| NSQ 陌生机制 | tavily_search → 1–2 句机制答 |
| Ask/NSQ 版规变更 | tavily_search `include_domains: ["reddit.com"]` + query sub rules |
| WebFetch 403 | firecrawl_scrape 同 URL |
| PH 链接 | firecrawl_scrape products + hunted（`references/product-hunt-urls.md`） |
| 竞品定价 | firecrawl_scrape 定价页 json 或 markdown |
| 重复搜索 | 同一任务 Tavily **或** Firecrawl search 为主，避免双份同 query |

---

## 输出习惯

- 给用户：**结论 + 依据（哪条 URL/搜索词）**  
- 备稿评论：**不要把「来源：Tavily」写进 Reddit 正文**  
- 额度：优先 scrape 单页；crawl/agent 需用户同意

---

## 专册

- `references/product-hunt-urls.md` — PH / hunted 参数  
- `references/tool-matrix.md` — 工具对照扩展  

*路径：`web-research-mcp/SKILL.md`*
