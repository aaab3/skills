# Execution Runbook（唯一执行入口）

> 写评论时 **只跟本文件 + Phase 内列出的子文件**。其余 references 为 **on-demand**，见文末表。  
> 输出缺必填字段 = 未完成。

---

## Phase 1 · 读帖

1. **`fetch-playbook.md`** — old.reddit `?sort=top`
2. **`thread-router.md`** — 定 `thread_mode`
3. **`op-info-gate.md`** — 定 `info_density`：`sufficient` | `thin`
4. 写一句 **OP合同**（中文可对用户）

**产出（进入 Phase 4 模板）：** `thread_mode` · `info_density` · `OP合同`

---

## Phase 2 · 写池（10–12 条）

按 `thread_mode` + `info_density` 配比（`info_thin` 覆盖 help 配比，见 `op-info-gate.md`）。

| 条件 | 必读 | 不读 |
|------|------|------|
| `gallery_*` | `real-comments.md` 扫 3 条 · `mk-thread-samples.md` 可选 | `product-recommendation-playbook` · `quality-comment-examples` §1–7 |
| `help_fresh` + `info_density=sufficient` | `human-voice-gate.md` | playbook 全文（无具名型号时） |
| `help_fresh` + 将出现具名 SKU | `human-voice-gate.md` + **`product-recommendation-playbook.md` §0–2** + `research-protocol.md` | `quality-comment-examples` 全扫 |
| `info_thin` | `human-voice-gate.md` + `op-info-gate.md` | playbook · Tradeoff 条 |

**具名 SKU：** 每行末尾 `| 核实: URL` 或 `| 核实: 未核实→🔴`（见 playbook）。

---

## Phase 3 · 批检（整批，再选实发）

顺序固定：

1. **`dedup-gate.md`** — 顶评摘录 + 撞车
2. **`batch-rhythm-gate.md`** — 整批节奏；填 **节奏自检** 一行
3. **`human-voice-gate.md`** — Tradeoff≤1 · 假摩擦禁 · 实发优先级

**备选池仅过：** `quality-checklist.md` §备选池 3 项。  
**不要** 对 10–12 条逐条跑 5 Rules。

---

## Phase 4 · 实发 1 条

1. 按 human-voice 优先级 + dedup 选 **1 条**（常 0–1 实发）
2. **`quality-checklist.md` §实发** — 完整 5 Rules + 型号来源（若有）
3. **`batch-output-template.md`** — 写入 `C:\Users\a\Desktop\评论\`

---

## 输出必填字段（缺一则重做）

```markdown
**OP合同：** …
**info_density：** sufficient | thin
**thread_mode：** …
**楼里顶评摘录：** …
**核实来源：**（无 SKU 写「无」）
**节奏自检：** 像不同时间写的 ✓ | 像一次生成的表格 ✗（须 Phase 3 重写）
```

---

## On-demand 参考（非每次打开）

| 文件 | 何时 |
|------|------|
| `quality-comment-examples.md` | 陌生帖型，只读对应一节 |
| `comment-style-guide.md` | Ban List 存疑 |
| `comment-patterns.md` | **已废弃执行** — 维护者对照 human-voice-gate |
| `communities.md` · `subreddit-context.md` | 版规争议 |
| `account-safety.md` | 新号 / 高 karma 风险 |
| `keyboard-domain-guide.md` | 术语不懂 |
| `regression-2026-05-28.md` | 改技能后自测 |

*路径：`reddit-keyboard-comments/references/execution-runbook.md`*
