# Codirigent — Rust 原生 AI coding CLI 工作区

**链接：** https://www.producthunt.com/products/codirigent  
**官网：** https://codirigent.dev/ · **Launch：** 2026-03-12 · **评论数：~3**  
**背景：** Windows+macOS；GPUI/Rust；多 session 网格跑 Claude Code/Codex/Gemini；git worktree；~40MB 内存；session 持久化；Working/Idle/Needs Attention 状态。

**已有评论：** HN/PH 上 Mac-only 工具痛点、Fortune 100 内部使用（maker 叙事）

**评论缺口：** Windows 与 WSL、Linux 计划、与 Orca 差异、权限状态持久化细节

---

## 评论草稿（8 条）

1. Every serious AI workspace shipped Mac-first until now — Rust + GPUI on Windows with worktree isolation is the first one I'd actually install. How do you handle ConPTY vs legacy console for Claude Code PTY sessions? | 中文：严肃 AI 工作区一直 Mac 优先——Windows+worktree 我会装；ConPTY 与旧控制台怎么处理 Claude Code | Question | 🟡 | **首选**

2. Session persistence including permission states is huge — nothing worse than re-approving tool calls after restart. Is that per-session file on disk or OS keychain backed? | 中文：重启后不用重新批 tool call 很重要——持久化存在哪 | Question | 🟡

3. Needs Attention vs Idle — is that inferred from CLI stdout patterns or hooks from the agents themselves? | 中文：Needs Attention 是从 stdout 猜还是 agent 有 hook | Question | 🟡

4. Orca is open source cross-platform too — Codirigent's angle seems native perf on Windows. Any plan for Linux or WSL2-only for now? | 中文：Orca 也开源跨平台——你们主打 Windows 原生；Linux/WSL2 计划 | Question | 🟡

5. ~40MB idle vs Electron terminals is the Tauri/GPUI story done right for devtools — congrats on shipping GPL. | 中文：空闲 40MB 对比 Electron 终端——GPL 恭喜 | Short Praise | 🟢

6. Paste images into terminal sessions is underrated for UI agent loops — does clipboard share across panes or per-session only? | 中文：终端贴图对 UI agent 循环有用——剪贴板跨 pane 还是每 session | Question | 🟡

7. I run three CLIs on one repo via worktrees — when two finish with conflicting package.json edits, is there a merge review queue or just git status in each pane? | 中文：三 CLI 同 repo 不同 worktree——两个改 package.json 冲突时有合并队列吗 | Personal Experience + Question | 🟡

8. Will try on a Windows laptop that never got a good tmux+agent setup — if worktree spawn is one click from the grid, that's the sell. | 中文：在从没配好 tmux+agent 的 Windows 本试——网格一键起 worktree 就是卖点 | Personal Experience | 🟢

**建议实发：** #1 或 #7
