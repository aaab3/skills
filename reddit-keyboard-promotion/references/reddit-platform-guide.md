# Reddit 平台评论指南（跨版块调研）

> 本技能的核心是 **在 Reddit 上评论**，不是「评论键盘」。键盘是默认垂直场景；本文件适用于任意 sub。
> 调研来源：r/MechanicalKeyboards、r/keyboards、r/explainlikeimfive、r/CasualConversation、r/AskReddit 类样本及评论排序/账号安全文献（2025–2026）。

---

## 1. Reddit 评论是什么

Reddit 不是「写得好」的平台，是 **在对的线程、对的时机、用对的语气占一个角度** 的平台。

| 维度 | 真人常态 | 容易像 bot/营销 |
|------|----------|-----------------|
| 单位 | **一条评论 = 一个贡献** | 一条里科普+夸赞+三问+推荐 |
| 长度 | 多数 **8–25 词**；故事/ELI5 长评是例外 | 30+ 词均匀高密度 |
| 证据 | 一个具体细节（OP 原话/图里一物/一句经历） | 「great」「solid」「premium」 |
| 结构 | 半句、lol、断句、偶尔错拼 | 完整段落、列表、小结 |
| 目标 | 接梗、接话、补一刀、问一事 | 显得比 OP 更懂 |

**Best 排序**（默认）偏向 **高同意率** 而非纯票多——极端争议句在多数 sub 不如「具体+顺眼」。

**早评优势**：同质量下，早 1–2 小时的评论曝光可差一个数量级；但 **不要为了早而空发**——低 karma 空评更易被滤。

**新号勿拼神评长度**：楼里若已有键鼠长清单（型号+价+latency），&lt;50 karma 应 **跳过或只补一个未覆盖角度** → `account-phase-routing.md`。

---

## 2. 动笔前必做：读线程（非可选）

### 2.1 拉取

| 场景 | 数据源 |
|------|--------|
| 新帖 | Reddit JSON：`.../comments/{id}.json?limit=200` |
| 旧帖/要多评 | PullPush（见 `pullpush-api.md`） |

### 2.2 必须弄清的四件事

1. **OP 要什么**：炫耀 / 求助 / 吐槽 / 讨论 / 促销？
2. **高赞已说什么**：避免同义重复（重复角度 = 隐形 downvote）
3. **缺什么角度**：还没人接的梗、细节、反问、轻度异议？
4. **能不能评**：锁帖、全 Meta、版规禁止（医疗/法律/拉群）？

### 2.3 回复位置

| 位置 | 何时用 |
|------|--------|
| **Top-level** | 新角度、接 OP 主叙事 |
| **Reply 高赞** | 接梗、延展笑话、Me-too（曝光更高） |
| **Reply OP** | 追问规格、补一句实用信息 |

**不要**在无人回复的 bot 楼（automod、QMK 许可证 bot）下抢楼，除非刻意参与该话题。

---

## 3. 通用帖子类型 → 真人常评什么

### Type A — 展示 / 照片 / Gallery（build、宠物、饭、键帽）

**真人高频：**

- **单点观察**：一个键帽图案、一种配色、一处改装（「脚垫对齐」「arrow keys are the key part」）
- **梗 / 情绪**：短、可接 OP 幽默密度
- **Me-too + 一细节**：「I have one too」+ 一个声音/手感词
- **单问**：`what board` / `what set`（仅当帖里没写）

**少评或不评：**

- 泛泛「beautiful build」
- 未读帖就推荐购买清单
- 连问 plate/switch/foam

**Filler 比例：** 硬核 hobby sub **低（~10–20%）**；meme/趣味 sub **高**。

---

### Type B — 故事 / 生活（CasualConversation、TIFU、offmychest 类）

**真人高频：**

- **接梗延展**（「Women in STEM」「grape blind」→ 科学方法笑话链）
- **共鸣一句**：「same」「this sent me」「I try lol」
- **分享平行小事**（一句，不抢 OP 叙事）
- **夸叙事**：「good storyteller」针对 **写法** 而非道德评判

**少评：**

- 未读全文就给人生建议
- 质疑真假（除非 sub 明确要 skeptic）
- 太长心理咨询

**注意：** r/CasualConversation 等明确 **No AI**、禁引流；语气偏暖、勿抬杠。

---

### Type C — 解释 / 求知（ELI5、NoStupidQuestions、技术 why）

**真人高频：**

- **分层解释**：类比 + 一句机制（ELI5 要 E，不是只答 Yes/No）
- **接话跑偏成故事**：「I remember playing Myst…」（仍围绕主题）
- **轻度幽默修正**：「I'm still setting it brighter than you intended」
- **补充边缘事实**：一个 counterexample

**少评：**

- 「hope this helps」
- 维基百科整段粘贴
- 争论政治化（ELI5 禁 argue POV）

**长度：** 可比 build 帖长，但仍 **一个主论点**；超长评靠分段/幽默撑。

---

### Type D — 购买 / 送礼 / 「该买哪个」（help、recommendation）

> **Agent 专册：** `product-recommendation-playbook.md`（OP 合同、产品轴、HE/无线核实、禁 SKU 清单）。发前 + `quality-checklist.md` § Type D Product Facts。

**真人高频：**

- **反问变量**（预算、尺寸、静音、Mac/Win）— 常是首条
- **礼品卡 / 别硬猜** 共识
- **一个 tradeoff + 一个锚点价**（「prebuilt hotswap > custom for gifts」「~$170」）
- **Me-too 场景**（「I bought wrong layout once」）

**少评：**

- 列 5 个 SKU
-  affiliate / 购买链接
- 「depends on many factors」无结论

---

### Type E — 故障 / 求助（troubleshooting）

**真人高频：**

- **Diagnostic 链**：最可能原因 → 第一步检查 → 结果意味什么
- **隔离法**：「if only spacebar, check wire」
- **反过度**：「before more lube, check bent wire」

**少评：**

- 未问清就断言主板坏了
- 嘲讽新手

---

### Type F — 观点 / 讨论 / 吐槽（discussion、meta、对比）

**真人高频：**

- **一句立场 + 理由**
- **轻度 disagreement**（「works but battery overrated」）
- **具体 counterexample**

**少评：**

- 人身攻击
- 「actually…」长篇居高临下

---

### Type G — 促销 / 自研 / IC（Promotional、vendor）

**真人高频：**

- **技术具体问题**（功耗、开源、兼容性）
- **场景**（「ortho split would eat this」）
- **延展唯一高赞技术点**（不重复）

**少评：**

- 「shut up and take my money」
- 托儿式连夸
- 与 automod/QMK  bot 混战（除非 intentional）

---

### Type H — AMA / 深度帖

**真人高频：** 一个高质量问题（真好奇）  
**少评：** 泛泛「thanks for doing this」

---

### Type I — 争议 / AITA / 政治（高风险）

**默认：** 本技能 **不主动生成** 除非用户明确要求；易引战、伤 CQS。

---

## 4. Sub 文化三层（叠加在帖子类型上）

```
Reddit 全站（禁 spam、vote manipulation、harassment）
    ↓
Sub 规则（flair、No AI、无链接、促销披露）
    ↓
Thread 时刻（梗帖 vs 严肃帖、高流量帖 mod 更严）
```

### Sub 原型（决定语气与 filler）

| 原型 | 代表 | 评论风格 | Filler |
|------|------|----------|--------|
| **硬核 hobby** | r/MechanicalKeyboards | 具体、少空夸 | 低 |
| **友好入门** | r/keyboards, r/NewToReddit | 实用、略暖 | 中 |
| **故事社交** | r/CasualConversation, r/AskReddit | 共鸣、梗、短 | 高 |
| **解释型** | r/explainlikeimfive | 清晰、可幽默 | 低–中 |
| **求助型** | r/techsupport, help flairs | 诊断、步骤 | 低 |

键盘垂直细则 → `subreddit-context.md` + `keyboard-domain-guide.md`。

---

## 5. 评论贡献类型（全站通用）

与 `comment-patterns.md` 一致，**每条评论只选一种**：

1. **Specific Observation** — 展示帖、梗图、「你觉得这个怎样」
2. **Tradeoff** — 购买、对比、值不值
3. **Diagnostic** — 故障、异常、是否正常
4. **Reaction / Me-too / Filler** — 社交、低门槛账号（Filler 无信息）
5. **Correction** — 事实纠正（带依据或软化）
6. **Quick fix** — 一步可操作（不是教程）

**Question 不作为主类型**：最多 **半句一问**，嵌入 Observation 或 Tradeoff。

---

## 6. 真人 vs AI：跨版块观察

### 6.1 高赞常见

- 早 + **一个清晰角度**
- 接 OP **原词/原梗**（grape blind → STEM）
- 具体到 **不可迁移的细节**（deathadder 线、1mm 对齐）
- 自嘲、轻度跑题但 **可拉回主题**（Myst 亮度故事）
- 争议但有 **证据或经历锚点**

### 6.2 低赞 / 被删常见

- 复制 AI 赞美模板
- 与 thread 无关的 product pitch
- 新号链接、Discord、affiliate
- 同一用户短时间多帖相似句
- 问卷式连问
- 回复 automod 当正经讨论

### 6.3 长度再校准（按类型）

| 帖子类型 | 建议词数 |
|----------|----------|
| Build / 梗图 | 5–25 |
| 故事社交 | 3–20（梗可更短） |
| ELI5 / 技术解释 | 20–80（仍一个主论点） |
| 购买建议 | 15–40 |
| 故障 | 20–50 |

旧版 SKILL「一律 under 30」→ 改为 **按 Type 表**；build 帖仍偏短。

---

## 7. 账号与 CQS（平台层）

见 `account-building-guide.md`。平台层要点：

- **被滤比不评更伤** CQS
- 新号：故事/Ask 类 sub 养号 → 再进硬核 hobby
- **不要**同 thread 刷多条
- **不要**用归档 API 伪造「我买过」
- 假细节（`had mine 3 weeks`）仅 **极短、不可验证** 时使用；禁止长线伪造

---

## 8. 生成流程（Agent 检查清单）

1. 拉 thread（JSON / PullPush）
2. 标 **Type A–I** + **Sub 原型**
3. 列出高赞角度（3–5 条）→ **避开**
4. 列缺口角度（3–5 条）→ **优先草稿**
5. 按 karma 阶段筛类型（见 SKILL.md）
6. 写 **8–12 条备选**，用户实发 **1–2 条**
7. 跑 `quality-checklist.md`
8. 垂直事实不确定 → `research-protocol.md`（键盘）或 web 搜索

---

## 9. 调研样本索引（可复现）

| 帖 | Sub | 类型 | 评论特征 |
|----|-----|------|----------|
| pepe keycaps | MK | 梗图 | 箭头梗、what board、六套键帽八卦 |
| Bauer Lite 首把 | MK | build | keep going、Neo 推荐链、键帽追问 |
| Piggy60 | MK | 高端 build | 拥有经历、键帽名、6u/7u 深讨论 |
| 混凝土 numpad | MK | 搞怪 DIY | 声音梗链、材料幽默 |
| Snoopy build | MK | IP build | 具体 novelty、脚垫、office 共鸣 |
| Choc 单键 PCB | MK | promo | 技术延展、开源兴趣 |
| 送礼键盘 | keyboards | 购买 | 礼品卡、反问、一个价位 |
| Gamma ELI5 | ELI5 | 解释 | 设计师逻辑+个人故事跑偏 |
| grape blind | CasualConversation | 故事 | 梗链、STEM 笑话、平行怪癖 |
| budget keyboards good | keyboards | D | P3 分体 numpad；P5 VIA Product ID 排错；忌 mega 清单 |
| AskReddit scientific facts | AskReddit | C | P7 可复现实验+配图；具体案例非抽象 |
| cursor usage % drop | cursor | F | P1 池子分母非清零；P6 两池+定价链接 |

专业评细则 → `professional-upvoted-comments.md`。

---

## 10. 与旧版技能的关系

| 旧问题 | 现规则 |
|--------|--------|
| 偏键盘规格评论 | 先 Type + Sub，键盘知识仅作补充 |
| 「多夸赞」 | 删除；展示帖 **Specific Observation > 空夸** |
| 不读帖就写 | **禁止**；必须先读 thread |
| 10–12 条全发 | 备稿 8–12，**实发 1–2** |
| 一律 30 词 | 按 §6.3 分类型 |
