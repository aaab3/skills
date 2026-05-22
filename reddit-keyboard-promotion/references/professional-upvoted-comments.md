# 专业高赞评论 Playbook（Expert Brief）

> **与 `high-engagement-comment-playbook.md` 的关系**  
> - **H1–H6**：展示/梗/社交帖——靠短、接梗、单锚点拿赞和回复。  
> - **P1–P8（本文件）**：解释/购买/故障/产品讨论帖——在**有大量可核实事实**时，靠**纠正误解 + 一条机制 + 可操作建议**拿赞。  
> 调研样本：r/keyboards 预算帖、r/AskReddit 科学事实帖、r/explainlikeimfive 高分评、r/cursor 用量讨论（2026-05）。

---

## 1. 什么时候用 P 型，什么时候仍用 H 型

| 信号 | 优先 |
|------|------|
| OP 问 why / how / is this normal / which one | **P 型** |
| 帖是图/gallery/build，无人问规格 | **H 型** |
| Thread 已有完整百科式 top 评 | **不要重复**；改 P8 补一刀或 reply 延展 |
| 你有官方文档/定价/论坛员工说明 | **必须**走 P1/P6/P2，禁止只写「可能吧」 |
| 新号、低 karma | P 型仍可用，但 **更短（25–50 词）**、少链接 |

**铁律：** 专业 ≠ 长。高赞专业评多数是 **一条新信息**，不是把 Wikipedia 贴进评论。

---

## 2. 真人专业评论如何拿赞（跨帖归纳）

### 2.1 高赞专业评的 8 个共同点

1. **第一句就纠正框架** — OP 以为「被清零」，你先说「不是 reset，是池子分母变大」。  
2. **只讲一个机制** — 因果链 ≤3 句；不要五个并列论点。  
3. **可核对细节** — 型号、$、版本号、设置路径、JSON 字段；**不**写「作为专家我认为」。  
4. **条件分叉 ≤2 条** — 「若主要写代码 → A；若竞技 FPS → B」；禁止「depends on many factors」无结论。  
5. **末尾一个动作** — dashboard 哪一栏、先查哪颗螺丝、VIA 里改哪个 ID。  
6. **争议处给出处** — 一条链接或「Colin on the forum said…」，不引战。  
7. **语气仍像 Reddit** — 小写、缩写、可一句 lol；**忌** hope this helps / great question / game changer。  
8. **占缺口，不撞 top** — 高赞已列 15 个键盘型号，你再列 16 个 = 隐形 downvote；改 **「R65 的 VIA JSON Product ID 错了」** 这种 **没人说过** 的点。

### 2.2 高赞但 skill 不优先模仿的两种

| 模式 | 例 | 为何谨慎 |
|------|-----|----------|
| **Mega 清单** | 预算帖里「Under $50:」列 10+ 链 | 曝光高，但像 bot/affiliate；新号易滤；CQS 风险 |
| **长篇阵营战** | QMK vs Dygma 50 楼互怼 | 票多但伤号；除非用户明确要求 |

**默认策略：** 学 **窄而准** 的 top 评（诊断、纠正、条件建议），不学 **清单竞赛**。

---

## 3. P1–P8 八种专业钩子

每条评论 **只挂一个 P 钩子**（可与 `comment-patterns.md` 的 Tradeoff/Diagnostic 叠加标注）。

| 钩子 | 机制 | 典型词数 | 模板骨架 |
|------|------|----------|----------|
| **P1 框架纠正** | 推翻 OP 错误前提 | 25–45 | `Not X — it's Y because Z.` |
| **P2 机制→后果** | 说清 why，一句 implication | 35–70 | `X works by … so if you … you'll see …` |
| **P3 条件建议** | ≤2 分支 + 各一句理由 | 30–60 | `If you need A, …; if B matters more, …` |
| **P4 诊断梯** | 症状→第一步→结果意味 | 35–80 | `Sounds like A. Check B first — if C, then …` |
| **P5 细节即信用** | 列具体型号/数字，不声称「我拥有」 | 25–55 | `R65 JSON has 0xe481 but the board reports 0xe508 — edit the file and …` |
| **P6 有据争议** | 一条出处 + 一句结论 | 40–90 | `Docs split Auto+Composer vs API … link` |
| **P7 可复现实验** | 读者能马上试 | 50–120 | `Shine light at 45° … wiggle 1cm … you should see …` |
| **P8 部分同意+修正** | 先认同再改一点 | 30–60 | `Yeah QMK is great, but for budget shoppers proprietary isn't always a dealbreaker if …` |

### 与 H1–H6 对照

| 场景 | 用 |
|------|-----|
| Qazikat 满 modifier 梗图 | H1 |
| Cursor 70%→7% 误解为月中清零 | **P1 + P6** |
| 预算键盘 + 要数字区 | **P3**（独立 numpad vs 一体） |
| VIA 认不出板子 | **P4/P5** |
| 冰河世纪冻肉 | H1/H5 或 **P7**（若认真教怎么观察） |

---

## 4. 真实样本（可复现链接 + 为何高赞）

### 4.1 r/keyboards — 预算键盘帖（讨论型 D）

帖：https://www.reddit.com/r/keyboards/comments/1q77x4g/budget_keyboards_that_you_think_are_actually_good/

| 评论形态 | 为何拿赞 | 对应钩子 |
|----------|----------|----------|
| `if you need a numpad … separate numpad would be better` | 直接答 OP「要数字区」；一条生活场景建议 | P3 |
| `This, 100%. QMK is feature rich …` | 短、立场鲜明；接上文原则，不另开战场 | P8 |
| `R65 … JSON … wrong Product ID … 0xe508 … edit` | **thread 唯一**的技术排错；可立即操作 | P5+P4 |
| `Casual gamers … HE … waste of money for a function we barely use` | 具体场景（cs2/dota）+ 明确结论 | P3 |
| 长清单 + 多链接 | 信息量大但 **skill 默认不生成** | （避免） |

**可改写模板（P3）：**

```text
if you need a numpad for occasional numbers, a separate pad keeps your TKL desk clean. aula f99/f108 or any cheap hotswap numpad is easier than replacing a board you already like.
```

**可改写模板（P5+P4）：**

```text
if via wont recognize the rk r65, check the json product id — rk ships 0xe481 in the file but some boards report 0xe508. edit that one field and reload, fixed mine in two minutes.
```

---

### 4.2 r/AskReddit — 科学事实帖（解释型 C）

帖：https://www.reddit.com/r/AskReddit/comments/ss2pkt/（科学事实类，高票区）

| 分数级 | 评论要点 | 对应钩子 |
|--------|----------|----------|
| ~6600 | 血管遮挡光 → 大脑填洞 → **教你怎么用侧光看见** → 配图 | P2+P7 |
| ~6070 | 冻土猛犸象/木乃伊 **具体案例** 列举，非抽象科普 | P2（叙事证据） |
| ~2986 | 接上一楼「尝过不好吃」— **一句幽默 payoff** | H2（子回复链） |

**P7 骨架（可迁移到任何「你怎么亲眼验证」主题）：**

```text
[mechanism in one sentence]. you can actually see it if you [one setup] — [distance/angle/dim]. [gentle motion] for about a second and [expected result]. [optional: diagram link]
```

---

### 4.3 r/explainlikeimfive — 高分评（PullPush 归档）

| 分数 | 模式 | 钩子 |
|------|------|------|
| ~4950 | `WiFi is literally light in the radio band` + 130 年广播史反证 | P2 |
| ~4590 | 列 EOD7/8/9/10 具体型号 + 多代试穿（**细节=可信度**） | P5 |
| ~3580 | 制造难、产线贵、人才稀缺（**供给链机制**） | P2 |

**ELI5 规则：** 先 **5 岁能懂的类比**，再 **一句** 真机制；不要先上公式。

---

### 4.4 r/cursor — 用量百分比骤降（讨论型 F）

帖：https://www.reddit.com/r/cursor/comments/1ti2z4p/

| 错误写法 | 专业写法 |
|----------|----------|
| `Maybe they reset your usage` | `Not a mid-month reset — % is used divided by current pool size.` |
| `Composer 2.5 is fast` | `composer-2.5-fast draws Auto+Composer at $3/$15 per M vs $0.50/$2.50 on Standard — burning faster usually raises %, not drops it.` |
| 无出处 | `Two pools: Auto+Composer vs API, each resets on billing cycle — cursor.com/docs/account/pricing` |

**首选 P1+P6 合一评（约 70–90 词）：**

```text
Not a mid-month reset — Cursor shows % of your Auto+Composer pool used, and that pool likely got bigger when Composer 2.5 dropped (changelog mentions extra included usage the first week). If you used more tokens today but % went down, the denominator grew, not your meter zeroing. Fast is $3/$15 per M vs Standard $0.50/$2.50 on the same pool. Check dashboard for both Auto+Composer and API bars: cursor.com/docs/account/pricing
```

---

## 5. 生成流程（Agent 在步骤 4–6 之间插入）

```
读完 thread
  → 标 Type C/D/E/F？
      否 → 走 H1–H6（high-engagement playbook）
      是 → 列 top 已说的「专业点」3–5 条（避开）
          → 搜索/读文档直到有 ≥2 条可核实事实
          → 选 1 个 thread 缺口 + 1 个 P 钩子
          → 写 3–4 条 P 型 + 2–3 条 H/Me-too（备稿 8–12 仍满足）
          → 建议实发：P 型首选（除非 build 梗帖）
```

### 5.1 专业评自检（5 秒）

1. **第一句** 是否给了 OP 不知道的信息（不是重复标题）？  
2. **能否被证伪**？有数字/路径/型号/链接其一。  
3. **是否只一个主论点**？删掉第二、第三「顺便」。  
4. **top 是否已说过**？说过则改 P8 或换 P5 窄细节。  
5. **像不像 ChatGPT**？删 hope this helps / I'd be happy to / game changer / solid pick。

---

## 6. 备稿配比（Type C/D/E/F）

| 条数 | 类型 |
|------|------|
| 3–4 | P1–P8 专业（不同钩子） |
| 2–3 | H3/H5 短问或回调（拉 OP 回复） |
| 1–2 | Me-too + 一个数字/场景 |
| 0–1 | Filler |
| 0 | 与 top 同义的 P3 清单 |

**实发 1 条：** 有核实事实 → **P 型 > H 型**；无事实 → 诚实标 🟡 并只出 H/问句，不装专家。

---

## 7. 与现有文件索引

| 文件 | 分工 |
|------|------|
| `comment-patterns.md` | Tradeoff / Diagnostic / Observation 结构 |
| `quality-comment-examples.md` | 键盘垂直改写模板 |
| `high-engagement-comment-playbook.md` | H1–H6 梗/社交 |
| **本文件** | P1–P8 专业/有据 |
| `research-protocol.md` | 何时必须搜索再写 P 型 |
| `product-recommendation-playbook.md` | Type D：OP 合同、HE/无线、禁 SKU 清单 |

---

## 8. 调研帖索引（持续追加）

| 帖 | Sub | Type | 专业评特征 |
|----|-----|------|------------|
| budget keyboards good | keyboards | D | P3 分体 numpad；P5 VIA ID；避免 mega 清单 |
| scientific facts blow mind | AskReddit | C | P7 可复现实验；具体案例 |
| cursor usage mid-month reset | cursor | F | P1 池子分母；P6 定价文档 |
| is via/qmk worth it | keyboards | C | P3 条件「只有 remap 才值」 |
| spacebar stab rattle | MK | E | P4 诊断梯（见 quality-comment-examples） |
