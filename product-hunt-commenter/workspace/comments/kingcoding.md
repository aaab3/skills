# KingCoding — Mac 上跑 Claude Code/Codex，手机遥控

**链接：** https://www.producthunt.com/products/kingcoding  
**Launch：** 2026-04-21 · **评论数：~4**  
**背景：** 控制塔：多任务、Discord 遥控、King Mode（目标→计划→执行→验证截图）、自动 review；solo dev Shingo，dogfood 自建。

**已有评论：** 一条较完整质疑 King Mode「adapts」遇 blocker 是停还是继续

**评论缺口：** 与 Orca 差异、Discord 安全、多 repo、验证截图假阳性、仅 Mac 限制

---

## 评论草稿（8 条）

1. King Mode "adapts when something goes wrong" is where I'd drill in — on a real blocker does it open a Discord approval with the failing command output, or silently retry until diff noise wins? | 中文：King Mode 遇真 blocker 是在 Discord 带失败输出求你批，还是静默重试到 diff 一团糟 | Question | 🟡 | **首选**（接已有质疑但更可操作）

2. Verification screenshots for UI tasks are smart — how do you handle flaky visual diffs (fonts, animations) without false failures blocking the queue? | 中文：UI 验证截图好——字体/动画 flaky 怎么避免误报堵队列 | Question | 🟡

3. I lose agent state across terminal tabs too — Discord as control plane is practical if message auth is tight. Is the bot token per-user or shared team channel? | 中文：我也丢 tab 状态——Discord 控制面实用但要消息鉴权紧；bot token 每人还是团队频道 | Question | 🟡

4. Running Claude Code from the train while the Mac stays on desk is the use case — what happens if the laptop sleeps mid-task? | 中文：地铁发任务 Mac 在家跑——笔记本睡眠中途任务怎么办 | Question | 🟡

5. Built with itself is a good stress test — congrats on launch. The hard part isn't dispatching tasks, it's mergeable output when three agents touch the same repo. | 中文：自建狗食物好——难在多个 agent 动同一 repo 还可合并 | Short Praise + Insight | 🟢

6. Orca is open source worktrees on all platforms — KingCoding's Discord + auto-review angle is different. Any plan for Windows or stay Mac-only? | 中文：Orca 开源全平台——你们 Discord+自动 review 不同；会出 Windows 吗 | Question | 🟡

7. Auto-review by another AI can rubber-stamp bad patches — do you surface the reviewer's objections to me before merge, or only on failure? | 中文：AI 审 AI 可能橡皮图章——反对意见会在 merge 前给我还是仅失败时 | Question | 🟡

8. I'll try King Mode on a small CSS refactor from phone — if approval flow is one tap with context, that's worth the install. | 中文：会用手机试小 CSS 重构——若一键批且带上下文就值得装 | Personal Experience | 🟢

**建议实发：** #1（maker 已表现出愿意深聊 King Mode）
