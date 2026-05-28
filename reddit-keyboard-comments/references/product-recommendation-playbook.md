# Product Recommendation Playbook（键盘 · Type D）

> **何时必读：** 评论里会出现 **≥1 个具体品牌/型号/SKU**，或 OP 问 buying / wireless / like X brand / alternatives / gift / budget pick。  
> **与语气规则并行：** `comment-style-guide.md`（反 AI）+ 本文件（**贴题 + 规格正确**）。  
> **调研：** `research-protocol.md` — 列型号前必须核实 connectivity。

---

## Named Product Gate（`SKILL.md` · 写具名型号前）

点名 **品牌+型号/SKU** 前，每项必须核实；**任一项未知 → 不点名该型号**。

| 必核 | 示例 |
|------|------|
| **connection** | wired only / 2.4G+BT / tri-mode |
| **layout** | 75% / ISO / Mac 键位 |
| **switch type**（若 OP 在乎轴/HE） | magnetic HE vs 机械 |
| **software/firmware**（若 OP 问 VIA/QMK） | VIA vs 私有云 |
| **matches OP 合同** | wireless 硬需求 ≠ 推 Air **HE** |

允许：**一条 lane** + `check wireless on the exact SKU` — 禁止假装已核实子型号。

---

## 0. Agent 硬顺序（不可跳步）

须在 **`SKILL.md` § Evidence Gate** 通过后再执行：

```
1. OP 合同（一句话：OP 在买什么维度？）
2. 楼里已有（高赞 3 点 — 不重复）
3. 产品轴分叉（§2 — Mode 审美 ≠ HE 游戏）
4. Named Product Gate + §4 搜索/官网（每个具名 SKU）
5. 写 1 条 local move：≤2 lane + ≤1 踩坑 + 禁清单
6. quality-checklist.md § Named Product Gate + § Type D Product Facts
```

**禁止：** 未做 3–4 就写 `Keychron … / NuPhy … / Lemokey …` 三连。  
**禁止：** 用 `-ish`（`wireless-ish`、`premium-ish`）搭配具名型号 — 像不确定导购。  
**Gate #3 弱或重复楼里 → 不 draft**（只输出 不建议发）。

---

## 1. OP 合同（先读懂再推荐）

在英文评论前先填（可对用户用中文输出）：

| 字段 | 示例 |
|------|------|
| **参照物** | like Mode Keyboards / Wooting / Keychron V / 无 |
| **硬约束** | must be wireless / must be quiet / budget $X / ISO / Mac |
| **主诉求** | aesthetic desk / competitive FPS / office typing / gift |
| **帖型** | MK 日帖嵌套问 / Help 主帖 / pcmr [Question] |
| **楼里已有** | vendor list only / 已列 5 个 SKU / 无 |

**合同错 = 整条废。** 典型错配：

| OP 合同 | 错误答法 |
|---------|----------|
| like **Mode** + **wireless** | 推 Q **HE**、Lemokey **HE**、NuPhy **Air HE** |
| need **2.4G** for desk | 只写 Bluetooth 够用（未确认型号支持 2.4G） |
| **gift**, no specs | 列 5 个购买链接式清单 |
| 楼里已有 **alexotos vendor list** | 再贴同义链接墙；应 **shortlist 2 lane + 一个踩坑** |

---

## 2. 产品轴分叉（本质层）

Reddit 推荐帖的高票答案，是在 **正确的轴** 上给 **边际信息**，不是「知道几个牌子」。

| 轴 | OP 信号 | 对口方向 | 默认勿塞 |
|----|---------|----------|----------|
| **A · Premium prebuilt 审美** | Mode, Sonnet, heavy case, thock, desk setup | Keychron **Q Max / Q Ultra**；NuPhy **Halo/Air V2/V3**（无线款）；QK/Neo **tri-mode kit** | Q **HE**, Lemokey **HE**, Wooting（除非 OP 要 RT） |
| **B · Wireless 硬需求** | wireless, 2.4G, Bluetooth, tri-mode, no cable | 仅列 **官网写明** 2.4G/BT/wired 的型号 | 一切 **HE Air** 线（见 §3） |
| **C · HE / 磁轴 / 竞技** | rapid trigger, 8K, magnetic, valo/cs2 | Wooting, Q HE, Lemokey HE, NuPhy Air **HE** | 说成「像 Mode 的无线替代品」 |
| **D · Budget 值** | under $X, first board | Aula, Leobog, Keychron V, BudgetKeebs 共识 | 一上来 Sonnet/Mode 价位 |
| **E · 故障 / 软件** | VIA won't, double typing, rattle | P4/P5 诊断（`professional-upvoted-comments.md`） | 无关购买清单 |

**Mode + wireless** 几乎总是 **A + B**，不是 C。

开场模板（P1 + P3）：

```text
Depends what you like about Mode. If it's the aluminum/custom-ish feel but you need wireless, ...
```

---

## 3. 易混型号表（发前必核对）

> 电商标题常把 HE 和 V2/V3 写乱。**以品牌官网 Connection / 规格为准。**

### NuPhy

| 系列 | 连接 | 轴/定位 | OP 要 wireless 时 |
|------|------|---------|-------------------|
| **Air75/Air60 HE** | **Wired only**（官方） | 低剖面磁轴 / 8K 游戏 | ❌ 不可推荐为无线 |
| **Air75 V2 / V3** | 2.4G + BT + wired | 低剖面机械，QMK/VIA（V2） | ✅ 可提 |
| **Halo75 V2** 等 | 查官网 tri-mode | 非 HE 游戏线 | ✅ 常作 wireless prebuilt |

**踩坑句（可复用）：** `don't grab the Air HE line if wireless is the point — those are wired only.`

### Keychron

| 系列 | 连接 | 更贴 OP |
|------|------|---------|
| **Q HE / K HE** 等 | 多为 HE 游戏向；**≠** Mode 审美替代 | OP 要 RT/磁轴 |
| **Q Max** | 铝壳 + 2.4G/BT/wired + QMK | Mode-like + wireless（较稳） |
| **Q Ultra** | 铝壳 + 2.4G/BT/wired + ZMK，8K 无线档 | 同上，偏新旗舰 |
| **V Max / V Ultra** | 无线预装，价位低于 Q 线 | budget wireless |

### 其他

| 误区 | 纠正 |
|------|------|
| 「便宜 premium wireless」→ 堆 **HE 三线** | HE 是 C 轴；Mode 是 A 轴 |
| Lemokey L5 **HE** 当 Mode 无线替代 | 先确认 OP 是否要磁轴；否则换 Q Max/Neo |
| **万能 Keychron** 一句 | `first-comment-playbook` 已禁；须贴合同 |

---

## 4. 调研协议（列名以前）

触发 **必须** web 或官网核对（`research-protocol.md`）：

- 评论出现 **具体型号**（含 HE / V2 / Max / Ultra 后缀）
- OP 写 **wireless / 2.4G / Bluetooth**
- 「like {Brand}」— 先弄清该品牌卖什么轴/连接

**每条具名 SKU 记录一行：**

```text
Model: NuPhy Air75 HE → Connection: Wired only (nuphy.com) → OK for this OP? No (needs wireless)
```

**查询模板：**

```text
"{MODEL}" site:nuphy.com OR site:keychron.com connection wireless
site:reddit.com/r/MechanicalKeyboards "{MODEL}" wireless
```

不确定 → **不写该型号**，或只写系列 + `check if yours is HE or V2`.

---

## 5. 写法（Reddit Type D）

### 5.1 结构

| 元素 | 规则 |
|------|------|
| 开场 | `Depends what you like about {参照物}.` 或 `If wireless is the main thing,` |
| Lane A | **一条** prebuilt 路线（1–2 系列名，非 5 SKU） |
| Lane B | **一条** kit/custom 路线（可选） |
| 踩坑 | **一个** thread 里可能没人提的事实（如 HE wired only） |
| 长度 | keyboards/MK Help **15–50 词**；日帖 reply 可更短 |
| 结尾 | 可 `still check layout/budget` — 禁 `hope this helps` |

### 5.2 禁止

- ❌ ≥3 个并列型号 + 价格 + 链接（mega 清单 → downvote/CQS）
- ❌ `wireless-ish` / `premium-ish` / `gaming-ish` 与具名 SKU 同句
- ❌ `Partly … Partly …`、`*Your frustration is valid*`
- ❌ 未读楼就推与 top 评同义的 Keychron/NuPhy 句
- ❌ 把 **HE** 线推荐给 **Mode + wireless** OP

### 5.3 金样（Mode + wireless · MK 日帖 reply）

**✅ 建议实发：**

```text
Depends what you like about Mode. If it's the aluminum/custom-ish feel but you need wireless, I'd start with Keychron Q Ultra/Q Max or QK/Neo boards with tri-mode PCBs.

NuPhy Halo/Air V2 are fine if you want a wireless prebuilt, but don't grab the Air HE if wireless is the point — the HE Air boards are wired only.
```

**❌ 勿发（事实+合同双错）：**

```text
Keychron Q HE / Lemokey L5 HE and Nuphy Air HE V2 are the usual wireless-ish premium-ish lane below Mode pricing — still check if you need full wireless 2.4G or just Bluetooth for desk use.
```

### 5.4 MK「Ask any keyboard question」日帖

| 规则 | 说明 |
|------|------|
| **Reply 嵌套问** | 找到 `Anyone got recommendations…` 那条，**挂 reply**，不要另开顶层 |
| 楼里仅 vendor list | 补 **shortlist + 一个踩坑**，勿重复「去 alexotos」 |
| 配额 | 键盘垂直 **≤1 条/天**（与 keyboards 二选一） |

---

## 6. Agent 输出模板（推荐帖）

```markdown
**帖型：** Type D · Product recommendation
**OP 合同：** （一句）
**产品轴：** A / B / C …
**楼里已有：** …
**规格核对：** Model → Connection → OK? …
**主推 1 条（EN）：** …
**可靠性：** 🟢 / 🟡 / 🔴
**是否建议发：** ✅ / ⚠️ / ❌
```

---

## 7. 相关文件

| 文件 | 分工 |
|------|------|
| `reddit-platform-guide.md` § Type D | 真人高频/少评 |
| `professional-upvoted-comments.md` | P1 框架纠正、P3 条件分叉 |
| `keyboard-domain-guide.md` | 决策因子 + 核实清单 |
| `quality-checklist.md` § Type D Product Facts | 发前勾选 |
| `first-comment-playbook.md` | MK 日帖、键盘配额 |
| `quality-comment-examples.md` §2–3, HE | 改写模板（非照抄 SKU 清单） |

*路径：`reddit-keyboard-comments/references/product-recommendation-playbook.md`*
