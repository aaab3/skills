# Reddit 找帖 SOP（Agent 侧 vs 你浏览器）

> **外网调研：** 优先 `web-research-mcp` 技能（Tavily + Firecrawl MCP）。**不能**代替读帖——线程仍用浏览器或 `pullpush-api.md`。

## 你能做的（最准）

在 **已登录的 Reddit** 里：

1. 进入目标 sub → 搜索框  
2. 关键词 + **筛选 Posts → New / Past week**  
3. 打开 **0–8 评论** 帖 → 确认未 archived、能回复  
4. 把 **链接 + OP 前两行** 发给 Agent

示例搜索 URL（把 `SUB` 换成子版名）：

```text
https://www.reddit.com/r/SUB/search/?q=KEYWORD&restrict_sr=1&sort=new&t=week
```

---

## Agent 能做的（本环境）

| 方法 | 结果 |
|------|------|
| 打开 `reddit.com/.../search` | 常 **403 Forbidden** |
| Reddit `new.json` | 常 **超时 / 403** |
| **DuckDuckGo** `site:reddit.com/r/SUB 关键词` | ✅ 可用，但多返回 **旧热帖**（1c、18e 等） |
| **PullPush** `api.pullpush.io` | ✅ 可用，**延迟**，索引常停在 **数天～数月前** |

Agent 的「浏览器搜」= **DuckDuckGo 站外搜索 + PullPush 补 OP 正文**，不是替你点开 Reddit 登录态。

---

## 关键词建议（养号）

| Sub | 搜 |
|-----|-----|
| NewToReddit | `karma`, `can't post`, `new account`, `comment karma` |
| CasualConversation | `daily habit`, `winter`, `mental health`, `newborn` |
| NoStupidQuestions | `how do`, `why does`, `eli5` |
| BudgetKeebs | 进周帖 **Ctrl+F** `ajazz`, `under 100`, `hotswap` |

---

## 写入草稿前

- 必须有 **OP 在问什么**（JSON / PullPush / 你粘贴）  
- 无 OP 正文 → **不写主推**  
- PullPush 日期 **≠ 今天** → 标注「发前浏览器确认未 archived」
