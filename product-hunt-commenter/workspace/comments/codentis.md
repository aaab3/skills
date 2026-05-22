# Codentis — 终端里的 agent 工作流

**链接：** https://www.producthunt.com/products/codentis  
**Launch：** 2026-04-10 · **评论数：~2**  
**背景：** Sujal 做的 CLI AI assistant：流式输出、语法高亮、10+ 交互命令、session memory、async agentic 架构；解决 IDE 与 AI 之间 context switch。

**已有评论：** 基本只有 maker 开场（hunted.space 无 highlights）

**评论缺口：** 与 Claude Code/Cursor CLI 差异、memory 是否跨 repo、是否支持 MCP、非交互脚本模式

---

## 评论草稿（8 条）

1. I live in Cursor for edits but still drop to terminal for long agent runs — the gap is session memory that survives tab kills. Does Codentis persist memory per project directory or globally on the machine? | 中文：Cursor 改代码、终端跑长 agent；想知道 memory 按项目目录还是整机全局 | Question | 🟡 | **首选**

2. "10+ interactive commands" is the hook for me — which ones actually change files vs just explain? I need a clear boundary before I trust it on a production repo. | 中文：关心哪些命令真改文件哪些只解释——上 prod repo 前要有边界 | Question | 🟡

3. Real-time streaming in the terminal sounds obvious until you've used tools that buffer forever — if stdout stays syntax-highlighted during long patches, that's stay-in-flow territory. | 中文：终端流式+高亮若长跑补丁不卡，才算真 flow | Insight | 🟢

4. Congrats on shipping. Most dev AI tools assume GUI first; building agentic workflows CLI-native is the audience that actually ships from terminal. | 中文：恭喜——多数工具 GUI 优先；CLI-native agent 才是终端出货的人 | Short Praise | 🟢

5. Any MCP support planned, or is Codentis its own tool ecosystem? I don't want another silo next to Cursor's MCP marketplace. | 中文：有计划接 MCP 还是自有生态——不想在 Cursor MCP 旁多一个孤岛 | Question | 🟡

6. Async processing matters when one command kicks off tests and analysis — does the CLI let you queue sub-tasks or is it strictly one foreground agent? | 中文：异步是否支持队列子任务还是只能单前台 agent | Question | 🟡

7. Been burned by AI CLIs that lose context after SSH disconnect — if session memory survives terminal restart, I'd try this on a remote box. | 中文：SSH 断线丢 context 吃过亏——若重启终端 memory 还在会在远程机试 | Personal Experience | 🟡

8. What model providers do you support out of the box, and can I bring my own API key without sending code paths through your cloud? | 中文：默认支持哪些模型、能否自带 key 且代码不经过你们云 | Question | 🟡

**建议实发：** #1 或 #5
