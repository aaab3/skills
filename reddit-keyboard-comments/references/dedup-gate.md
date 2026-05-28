# Dedup Gate（写稿后 · 交付前）

> 避免备稿与 **顶评原文** 撞车。写 10–12 条不等于 10–12 条都能发。  
> **跨帖句式复读** → `execution-runbook.md` 跨批去重 · `batch-rhythm-gate.md` §C（非本文件）。

---

## 步骤

1. 输出 **楼里顶评摘录** 3–8 条（原文，非摘要；去 AutoModerator）
2. 每条备稿与顶评比对：
   - **逐字相同** → 标 `撞车` · 禁作实发建议
   - **≥6 连续词相同** → 标 `撞车-近` · 降优先级
3. `saturated_*`：维修/纠正向备稿若与顶评 **同义** → 删或标不建议发

---

## 输出字段（写入桌面 md）

```markdown
**thread_mode：** saturated_meme
**楼里顶评摘录：**
- Understandable.
- Warm the safety pin so it can embed in the stem and can be pulled
…
**撞车：** #2 与顶评逐字相同 · #5 与 #3 顶评近义
```

---

## 优先级（撞车后）

```
无撞车 🟢 > 无撞车 🟡 > 撞车-近 > 撞车（禁实发）
```

安全度 > 贴 thread_mode > 多样性。

*路径：`reddit-keyboard-comments/references/dedup-gate.md`*
