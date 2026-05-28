# Blind Spot Gate（盲点 · Phase 1 候选 → Phase 2 写 0–1 条）

> **赞量最稳的来源：** OP/楼**没提**、会**改变结论**的可核实事实。  
> 随口说出，不是顾问清单。配对：`op-info-gate.md` · `blind-spot-examples.md`

---

## 触发前问自己（`OP阶段`）

| OP阶段 | 盲点须满足 | 典型 ✅ | 典型 ❌ 作实发 |
|--------|------------|---------|----------------|
| **探索**（无型号） | **改需求方向** · 买之前就应知道 | listing 写 media keys 仍可能在 Fn 层；全尺寸 desk footprint 难回头 | 装驱动后旋钮才管用（**买了才踩**） |
| **比较**（2+ 候选） | 改选型或**比较轴错了** | 8k 一样比的是 layout/软件；某盘缺关键布局 | 复述 OP 已知难找 |
| **已购/故障** | → 用 **Diagnostic** 为主，非购买盲点 | 先换 USB 口再 desolder | 推荐买另一把 |

---

## 定义

| 是 Blind Spot | 不是 |
|---------------|------|
| OP 正文**未写**的变量 | OP 已在抱怨的（「难找」→「很稀有」= 观察） |
| **可核实**事实 | 推测、`probably`、`I'd guess` |
| **陈述/提醒**一句 | `you should consider X` · 三条 spec 清单 |
| **探索期：** 改方向 | **探索期实发：** 仅事后坑（软件/HID） |

---

## 写法

```text
✅ 探索： a lot of full sizes still hide play/pause on fn even when they show a volume knob
✅ 比较： both wired 8k — you're picking layout and software, not raw speed
✅ 已购： before you desolder, try a different USB port — some hubs drop media keys
```

```text
❌ dedicated media row is kinda rare now          （观察）
❌ worth checking if volume knob needs software     （探索期：池内可留 · 默认不实发）
❌ I'd look at Das 4 for the media row             （推荐）
```

**具名 SKU：** 行尾 `| 核实: URL`；`info_thin` **允许** 0–1 条盲点进池 · **禁**无核实具名推荐。

**句式：** 连续两帖禁同开 `worth checking if` → `execution-runbook.md` 跨批去重。

---

## 与 Observation / Diagnostic 分界

| 类型 | 问句 |
|------|------|
| **Blind Spot** | 会改选型或比较轴？ |
| **Observation** | 夸图/键帽/价？ |
| **Diagnostic** | 故障：先查什么？ |

---

## Phase 2

- 候选 **有** → 池 **0–1** 条 · 标 `类型: Blind Spot` · 标 **改方向 / 事后坑**
- 候选 **无** → **不硬造**
- **实发** → `human-voice-gate.md` · **`OP阶段` 表**

*路径：`reddit-keyboard-comments/references/blind-spot-gate.md`*
