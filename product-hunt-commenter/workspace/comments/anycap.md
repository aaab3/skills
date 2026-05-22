# AnyCap — 给 coding agent 图像/搜索/发布能力

**链接：** https://www.producthunt.com/products/anycap  
**评论数：~1** · 0 upvotes（未 featured）  
**背景：** Agent 用自然语言要能力（mockup、竞品搜索、发网页），AnyCap 统一处理；一次安装一次登录，无 SDK。

**已有评论：** 极少

**评论缺口：** 定价/额度、与 Cursor 内置工具重叠、隐私（搜索/图片）、是否 OpenAPI 还是 MCP

---

## 评论草稿（8 条）

1. Wiring image gen and web search into agents usually means three API keys and brittle JSON — plain-English capability requests is the right UX if latency stays under a few seconds. What's the p95 for "search competitors"? | 中文：agent 接图像+搜索通常三个 key；若「搜竞品」p95 在几秒内才是好 UX | Question | 🟡 | **首选**

2. I use Cursor with MCP already — does AnyCap register as one MCP server with multiple tools, or separate installs per capability? | 中文：在 Cursor 用 MCP——AnyCap 是一个 server 多 tool 还是每种能力分开装 | Question | 🟡

3. Publishing "this as a webpage" from an agent sounds useful for internal demos — is hosting on your infra or do we bring our own bucket? | 中文：agent 发布网页做内 demo——托管在你们还是自带 bucket | Question | 🟡

4. The no-glue-code pitch is what every agent builder wants until billing shows up — free tier limits and what counts as one "capability call"? | 中文：不要胶水代码直到账单出现——免费额度和什么算一次调用 | Question | 🟡

5. Agents already hallucinate APIs — giving them real eyes (search) and hands (publish) only helps if errors surface clearly back to the model. | 中文：agent 会 hallucinate API——只有失败信息清晰回传模型才有用 | Insight | 🟡

6. Congrats on shipping — most coding agents stop at repo boundaries; cross-modal tasks are still duct tape for solo devs. | 中文：恭喜——多数 agent 止于仓库；跨模态任务个人开发者还在用胶带粘 | Short Praise | 🟢

7. For client work I'd need to know where prompts and generated images are stored — EU hosting, zero retention option? | 中文：客户项目要知道 prompt 和图片存哪——欧盟、零保留选项吗 | Question | 🟡

8. Trying this on a side project that needs a landing screenshot + competitor scan in one agent session — will report back if the one-login flow is real. | 中文： side project 要落地页截图+竞品扫描一次会话搞定——若真一键登录会反馈 | Personal Experience | 🟢

**建议实发：** #2（Cursor）或 #1
