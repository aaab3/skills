# Execution Runbook（唯一执行入口）

> 写评论时 **只跟本文件 + Phase 内列出的子文件**。输出缺必填字段 = 未完成。

---

## Phase 1 · 读帖

1. **`fetch-playbook.md`** — old.reddit `?sort=top`
2. **`thread-router.md`** — `thread_mode`
3. **`op-info-gate.md`** — `info_density` + **盲点扫描**
4. **OP合同** 一句（中文可对用户）

**产出：** `thread_mode` · `info_density` · **`盲点候选`**（0–1 或 `无`）· `OP合同`

---

## Phase 2 · 写池（10–12 条）

### 写前核心原则

1. **One action** — 反应 / 判断 / 问 / **盲点** / 选边，择一。
2. **Show don't conclude** — Help 禁空夸；Filler 可 `looks good`。
3. **10–12 = 备选池** — 允许平、短、没说完。
4. **Ban List** — `genuinely` · `game changer` · `the real unlock` · `at scale` · `workflow`；≥2/条 → 重写。
5. **Scratchy ≠ 装饰 tbh** — §`human-voice-gate.md` 句法测试。
6. **Blind Spot 0–1** — Phase1 有候选则写 1 条；扫 `blind-spot-examples.md`（1 正+1 反）；**无则硬造**。

写前可选扫：`your-upvoted-samples.md`（1–2 条，看得赞原因）。

---

| 条件 | 必读 |
|------|------|
| `gallery_*` | `real-comments` 3 条 · `mk-thread-samples` 可选 |
| `help_*` | `human-voice-gate` · `blind-spot-examples`（Help 购买/对比） |
| `info_thin` | `op-info-gate` |
| 具名 SKU | `product-recommendation-playbook` §0–2 · 行尾 `核实:` |

---

## Phase 3 · 批检

1. **`dedup-gate.md`**
2. **`batch-rhythm-gate.md`** — 节奏自检 + **实发倾向**
3. **`human-voice-gate.md`**

备选池仅 **3 项**（`quality-checklist` §备选池）。

---

## Phase 4 · 实发

1. 按 **实发倾向** + dedup 选 1 条  
2. **`quality-checklist` §实发** — 5 Rules  
3. **`batch-output-template.md`** → `C:\Users\a\Desktop\评论\`

---

## 输出必填字段

```markdown
**OP合同：** …
**info_density：** sufficient | thin
**盲点候选：** … | 无
**thread_mode：** …
**楼里顶评摘录：** …
**核实来源：** …
**节奏自检：** … ✓
**实发倾向：**
- 盲点/信息：#…
- 共鸣：#…
- 首选实发：#…
```

---

## On-demand

| 文件 | 何时 |
|------|------|
| `quality-comment-examples.md` | 陌生帖型一节 |
| `comment-style-guide.md` | 完整版 |
| `real-comments.md` | 短句；**按类型非按得赞** — 优先金样/盲点例 |
| `regression-2026-05-28.md` | 改技能自测 |

*路径：`reddit-keyboard-comments/references/execution-runbook.md`*
