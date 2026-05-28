# OP Info Gate（Phase 1 · 与 thread-router 并行）

> 回答「能不能写顾问句」比「帖型是什么」更早。  
> 配对：`thread-router.md` · `execution-runbook.md`

---

## 判定 `info_density`

**`thin`（任一触发）：**

- 购买/对比帖但 OP **硬约束 <2 项**（如只有「full size + wired」，无预算/用途/平台/已有候选）
- 对比 A vs B 但 **未说看重什么**（性能/手感/价/外观）
- OP 自述信息极少且楼 **0–2 评**、无补充事实可引用
- 故障帖 **无型号/无症状细节/无已试步骤**

**`sufficient`：** 以上皆否，或楼里顶评已补足关键缺口（须在 OP合同 注明「楼补：…」）。

---

## `info_thin` 批量配比（覆盖 help_fresh 默认）

| 类型 | 条数 |
|------|------|
| 短问 OP（≤8 词） | **4+** |
| Scratchy + 纯废话 | **2+** |
| Pick-side | **0–1** |
| Tradeoff | **0** |
| 具名 SKU | **0** |

**硬禁：** Tradeoff · 具名型号推荐 · 总结陈词（`basically X or Y, everything else Z`）· 规格表式一条堆 3+ spec

**实发优先：** 问 OP 一句 · 纯废话/Scratchy · **不建议发**（比假顾问好）

---

## 锚帖

| 帖 | 判定 | 好实发 |
|----|------|--------|
| [1tpru8p fullsize media](https://www.reddit.com/r/keyboards/comments/1tpru8p/) | `thin` | `what's your budget?` · `why is this still hard to find in 2026` |
| [1tpt963 IROK vs Real67](https://www.reddit.com/r/keyboards/comments/1tpt963/) | `sufficient`（有两款+竞技用途） | 选边/问游戏 · 非 depends 三连 |

---

## 与 thread-router 叠加

```
Phase1: thread_mode + info_density
若 info_thin → 即使 help_fresh 也禁 Tradeoff/具名 SKU
若 gallery_* → info_thin 少见；仍以 Filler 为主
```

*路径：`reddit-keyboard-comments/references/op-info-gate.md`*
