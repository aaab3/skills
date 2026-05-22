# jscpd — AI-ready 重复代码检测 + MCP

**链接：** https://www.producthunt.com/products/jscpd  
**评论数：~1** · 20M+ 下载历史  
**背景：** 2013 年起 CLI，Rabin-Karp，150+ 语言；新版：MCP Server、AI Reporter（约省 79% token）、Agent Skill 自动 refactor 重复块。

**已有评论：** maker 长帖介绍 AI 集成

**评论缺口：** MCP 在 Cursor 里如何配置、Reporter 格式样例、误报（generated code）、与 agent 复制粘贴循环的关系

---

## 评论草稿（8 条）

1. Cursor agents copy-paste entire modules when stuck — jscpd in the loop could stop duplicate debt before merge. Does the MCP tool return file:line ranges the agent can act on, or only summary stats? | 中文：Cursor agent 常整模块复制——MCP 返回可操作的 file:line 还是只有汇总 | Question | 🟡 | **首选**

2. The ~79% token savings on AI Reporter is the detail I'd actually use — paste-friendly output matters when you're piping scan results into a 200k context window. What does one finding look like in that format? | 中文：AI Reporter 省 token 才有用——一条 finding 长什么样 | Question | 🟡

3. We run jscpd in CI already — curious if the new agent skill dedupes across generated OpenAPI clients or ignores vendor/ paths by default. | 中文：CI 已在跑——agent skill 会扫 generated OpenAPI 吗、默认忽略 vendor 吗 | Question | 🟡

4. Copy-paste duplication is tech debt that doubles bug fixes — glad you're meeting agents where they work now, not just humans in pre-commit. | 中文：复制粘贴让 bug 修两次——agent 时代接上很重要 | Insight | 🟢

5. Congrats on the AI launch. Rabin-Karp at scale is the boring right choice — most "AI code quality" tools skip deterministic checks entirely. | 中文：恭喜——大规模用 Rabin-Karp 是对的；很多 AI 质量工具跳过确定性检查 | Short Praise | 🟢

6. False positives kill trust — how do you handle near-duplicate boilerplate in test files vs real production clones? | 中文：误报伤信任——测试样板代码 vs 生产真重复怎么区分 | Question | 🟡

7. Planning to wire this into a pre-PR hook for agent-generated branches — does the skill auto-fix or only report? | 中文：打算给 agent 分支加 pre-PR hook——skill 自动修还是只报 | Question | 🟡

8. 20M downloads is social proof — I'll try MCP in Cursor tonight if there's a one-liner config in the repo README. | 中文：2000 万下载有说服力——README 有一行 Cursor MCP 配置今晚就试 | Personal Experience | 🟢

**建议实发：** #1
