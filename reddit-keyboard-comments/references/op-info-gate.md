# OP Info Gate（Phase 1 · 与 thread-router 并行）

> 回答「能不能写顾问句」、**OP 处于哪一阶段**、**有没有盲点可写**。  
> 配对：`thread-router.md` · `blind-spot-gate.md` · `execution-runbook.md`

---

## 判定 `info_density`

**`thin`（任一触发）：**

- 购买/对比帖但 OP **硬约束 <2 项**（如只有「full size + wired」，无预算/用途/平台）
- 对比 A vs B 但 **未说看重什么**（性能/手感/价/外观）
- OP 自述信息极少且楼 **0–2 评**、无补充事实可引用
- 故障帖 **无型号/无症状细节/无已试步骤**

**`sufficient`：** 以上皆否，或楼里顶评已补足关键缺口（OP合同 注明「楼补：…」）。

> **`info_thin` ≠ `OP阶段=探索`**：thin 的比较帖仍可能是 `比较` 期。

---

## 判定 `OP阶段`（Phase 1 必标）

| 阶段 | 判定 |
|------|------|
| **`探索`** | 无具体型号 / 仅品类+硬约束（「全尺寸有线+独立媒体键」）· 在问「有没有」 |
| **`比较`** | **2+ 具名候选** 或 A vs B · OP 在选边 |
| **`已购/故障`** | 已到手 / 症状 / 维修 / 「我的键盘…」 |

**`thread_mode` 叠加：** `gallery_*` · `saturated_*` 不套下表实发优先（见 `thread-router.md`）。

---

## 盲点扫描（Phase 1 · 产出 `盲点候选`）

写 **盲点候选**（0–1 条英文草稿或「无」）：

| 扫描 | 问 |
|------|-----|
| 硬约束误区 | OP 假设是否常错？（「独立媒体键」= 真独立行 vs Fn+旋钮） |
| 用途漏变量 | 会改变**需求方向**的未写字段？（desk footprint、Mac、numpad 习惯） |
| 品类结构 | **可核实**的坑 · 非「本来就难找」 |

**无则写 `无`。** 禁止把 OP 已说的困境改写成「观察」当盲点。

**与 `OP阶段`：** 探索期优先 **改方向** 盲点；**买了才踩** 的坑（驱动/HID/售后）→ 可进池 · **默认不实发**（见 `blind-spot-gate.md`）。

---

## `info_thin` 批量配比

| 类型 | 条数 |
|------|------|
| 短问 OP | **4+** |
| Scratchy + 纯废话 + **共鸣** | **2+** |
| **Blind Spot** | **0–1**（候选≠无 且可核实 · 探索期多为池内不实发） |
| Pick-side | **0–1** |
| Tradeoff | **0** |
| 具名 SKU **推荐** | **0** |

**硬禁：** Tradeoff · 总结陈词 · spec 表式推荐

**实发：** 见 `human-voice-gate.md` · **`OP阶段` 优先于** 全局「盲点>共鸣」

---

## 锚帖

| 帖 | info | OP阶段 | 盲点候选 · 实发 |
|----|------|--------|-----------------|
| [1tpru8p fullsize media](https://www.reddit.com/r/keyboards/comments/1tpru8p/) | thin | **探索** | Fn 层/ listing 误导 · 非事后 software 实发 |
| [1tpt963 IROK vs Real67](https://www.reddit.com/r/keyboards/comments/1tpt963/) | sufficient | **比较** | layout/software not fps · 可实发推翻/盲点 |

*路径：`reddit-keyboard-comments/references/op-info-gate.md`*
