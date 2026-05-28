# Batch Rhythm Gate（Phase 3 · 整批）

> **只读 10–12 条英文原文**（不看中文、类型标签）。在 dedup 之后、选实发之前。

---

## 必达

| 检查 | 标准 |
|------|------|
| 超短 | **≥2 条** ≤5 词 |
| 长短参差 | **≥1 条** ≥18 词 **或** 半句未完（`...` / 缺谓语） |
| 口吻多样 | Pick-side / Casual / Scratchy / 纯问 OP 至少 **3 类** 出现 |
| 骨架 | **禁止** 连续 3 条同骨架（depends · if you X then Y · good for X but Y） |

---

## 读感测试（必填输出一行）

```markdown
**节奏自检：** 像同一人不同时间写的 ✓
```

若读起来像 **同一次生成的表格** → 标 `✗`，Phase 3 **必须** 打散后重写该行：

**打散法（改 2–3 条即可）：**
- 加 1 条 ≤3 词
- 把 1 条改成半句断掉
- 删或降级 1 条 Tradeoff（`info_thin` 应已为 0）

---

## 失败 vs 通过示例

**✗ 表格感：** 12 条全是 12–22 词 · 每条完整句 · 3 条 depends 骨架  
**✓ 参差感：** `budget?` · `Das 4, actual volume knob and everything` · `fn media on most full sizes tbh` · `why still hard lol`

*路径：`reddit-keyboard-comments/references/batch-rhythm-gate.md`*
