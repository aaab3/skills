# Execution Runbook（唯一执行入口）

> 写评论时 **只跟本文件 + Phase 内列出的子文件**。输出缺必填字段 = 未完成。

---

## Phase 1 · 读帖

1. **`fetch-playbook.md`** — old.reddit `?sort=top`
2. **`thread-router.md`** — `thread_mode`
3. **`op-info-gate.md`** — `info_density` + **盲点扫描**
4. **OP合同** 一句（中文可对用户）

**产出：** `thread_mode` · `info_density` · **`OP阶段`** · **`盲点候选`**（0–1 或 `无`）· `OP合同`

**`OP阶段`（必标 · 见 `op-info-gate.md`）：** `探索` | `比较` | `已购/故障`

---

## Phase 2 · 写池（10–12 条）

### 跨批去重（写池前必做）

1. **`Glob`** `C:\Users\a\Desktop\评论\*.md` · 读最近 **2–3** 份同 sub 草稿的 **实发建议** 与 **首选实发** 英文句。
2. 本批禁止复读近期已用**开头/骨架**（换信息可，换说法）：

| 若上批实发/盲点用过 | 本批 |
|---------------------|------|
| `worth checking if` | 换：`a lot of listings…` / `before you hunt models…` / 半句 scratchy |
| `why is … still this hard` | 换角度：接 OP 具体讨厌点（junk keys / giant font） |
| `both … 8k … layout not speed` | 同帖可保留；**连续第二帖**换推翻轴 |
| `some boards need their software` | 探索期可进池 · **禁连续两帖实发** |

3. **同 URL 多版本**（v2/v2.2）：与上版英文句 **<30% 逐条相同**；否则重写。

---

### 写前核心原则

1. **One action** — 反应 / 判断 / 问 / **盲点** / 选边，择一。
2. **Show don't conclude** — Help 禁空夸；Filler 可 `looks good`。
3. **10–12 = 备选池** — 允许平、短、没说完。
4. **Ban List** — `genuinely` · `game changer` · `the real unlock` · `at scale` · `workflow`；≥2/条 → 重写。
5. **Scratchy ≠ 装饰 tbh** — §`human-voice-gate.md` 句法测试。
6. **Blind Spot 0–1** — 见 `blind-spot-gate.md`（**OP阶段** 决定是否实发）；扫 `blind-spot-examples.md`（1 正+1 反）；候选=无 → **不硬造**。

写前扫：`your-upvoted-samples.md`（1–2 条）或 `community-high-comments.md`（2–3 条 · 看得赞原因）。**比较帖** 加扫 `quality-comment-examples.md` **§11**。

**探索期实发：** ≤18 词或一句半 · 见 `human-voice-gate.md`

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
**OP阶段：** 探索 | 比较 | 已购/故障
**盲点候选：** … | 无
**跨批禁复用：** 已扫 Desktop 最近稿 · 本批避开 …
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
| `quality-comment-examples.md` | 陌生帖型一节 · **比较帖 → §11** |
| `comment-style-guide.md` | 完整版 |
| `real-comments.md` | 短句；**按类型非按得赞** — 优先金样/盲点例 |
| `regression-2026-05-28.md` | 改技能自测 |

*路径：`reddit-keyboard-comments/references/execution-runbook.md`*
