---
name: reddit-keyboard-comments
description: >-
  Comments 版 · r/keyboards + r/MechanicalKeyboards。Blind Spot · 得赞原因 · 实发倾向 ·
  4 阶段 runbook。输出 Desktop\评论\。
---

# Reddit 键盘评论 · Comments 版

> **执行入口：** `references/execution-runbook.md`（唯一）  
> **结构：** `references/skill-map.md`

## 边界

| 允许 | 禁止 |
|------|------|
| `r/keyboards` · `r/MechanicalKeyboards` | 其他 sub |
| 评论备稿 | 自动发布 · affiliate · 假购买史 |

---

## 工作流（4 阶段）

| 阶段 | 做什么 |
|------|--------|
| **1 读帖** | fetch → thread-router → op-info（**OP阶段** · **盲点候选**）→ OP合同 |
| **2 写池** | **跨批去重**（扫 Desktop）· 6 原则 · Blind Spot 按 **OP阶段** · 扫金样/§11 |
| **3 批检** | dedup → batch-rhythm（**实发倾向**）→ human-voice |
| **4 实发** | 按倾向选 1 条 → 5 Rules → Desktop md |

详 **`execution-runbook.md`** · 输出 **`batch-output-template.md`**

---

## 输出必填

`OP合同` · `info_density` · **`OP阶段`** · `盲点候选` · **`跨批禁复用`** · `thread_mode` · `核实来源` · `节奏自检` · `实发倾向` · 撞车 · 实发建议

---

## Filler（默认 · 见 thread-router）

| Sub | 条数 |
|-----|------|
| r/keyboards | 2–3 |
| r/MechanicalKeyboards | 1–2（saturated_meme 可 3–4） |

---

## 写稿要点

- 3–10 词最安全 · 10 条 = 备选池 · 实发常 0–1  
- `info_thin` → 问 OP / 废话优先 · **禁 Tradeoff / 具名 SKU**  
- 具名 SKU → `| 核实: URL` 否则 🔴  

Type D → **`product-recommendation-playbook.md`**
