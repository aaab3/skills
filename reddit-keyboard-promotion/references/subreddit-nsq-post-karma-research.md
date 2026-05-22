# r/NoStupidQuestions 发帖获 Karma 调研（2026-05）

> **数据源：** old.reddit `top?t=year|week|month`（75+ 标题）；**正文采样** 4 帖（通胀 14.6k、图书馆 2.3k、菠萝 5.7k、西语问候 10.2k）；对比低票帖 `1tjbn73`（2 票）。  
> PullPush 全量 API 未用作中位数统计。发策略前请在浏览器再核对 `/top` 与 sub 内搜索。

---

## 1. 核心结论（先看这个）

| 目标 | 更稳的路径 | 发帖路径 |
|------|------------|----------|
| **稳定涨 karma、抬 CQS** | ✅ **评论** `/new` 0–8 评帖，短答补缺位 | ⚠️ 次要 |
| **单帖爆发 post karma** | ❌ 不可复制 | 彩票：时事 + 共鸣 + r/all |
| **新号（&lt;50 karma）** | 阶段 A：**先评论 2–3 周** | **暂缓发帖**；硬发易 0 票/删帖/伤 CQS |

**NSQ 发帖拿「大量 karma」在统计上属于长尾分布：** 年榜 Top25 全部 **1.7万–2.9万** 票，但周榜第 25 名已降到 **~1900**，而 `/new` 常见帖 **0–5 票**。多数发帖者的期望值接近 **个位数**，不是年榜中位数。

---

## 2. 历史数据快照

### 2.1 年 Top（past year）— 票区 **17.4k–28.8k**

| 票 | 标题类型（缩写） |
|----|------------------|
| 28.8k | 被 A 公司开除后 B 公司与 A 合并，我会怎样 |
| 28.5k | 美国人是否因费用不敢叫救护车 |
| 26.0k | 警察脸像拇指 / Gen Z stare |
| 25.7k | Epstein 文件会被 bury 吗 |
| 24.1k | Luigi Mangione 为何可能死刑 |
| 22.9k | 女性 going commando 怎么做到 |
| 22.8k | 29 岁肺癌临终（Answered） |
| 22.6k | 朋友误发 18 万工资去赌博 |
| 22.2k | 麻醉后没人接亲人 |
| 21.1k | Steam/Kindle 库能否遗嘱继承 |
| 20.2k | 普京去阿拉斯加美国是否必须逮捕 |
| … | 日常好奇（锁门、虾尾、企鹅抱团、富人用不用普通牙膏） |

### 2.2 周 Top（past week）— 票区 **1.9k–14.6k**

| 票 | 标题类型 |
|----|----------|
| 14.6k | 通胀继续怎么买得起东西 |
| 8.0k | 越南人为何不对美国怀恨 |
| 7.1k | 美国餐车十年变贵 |
| 4.9k | Tom Holland 伞舞为何吸引直女 |
| 4.9k | 手铐聋人是否剥夺言论自由 |
| 4.8k | Musk 衰落何时开始 |
| 4.6k | 中国人问：美国嘲 nerd 又负债读大学 |
| 3.6k | 直女朋友「教育」男同 homophobic |
| 3.5k | 男口要 low-maintenance 却追 high-maintenance |
| 2.8k | 政府发现地下黄金归国家、毒品却归我 |
| 2.4k | 图书馆能否坐着读书 |
| 2.3k | 石器时代幼儿怎么活 |

### 2.3 与「普通帖」的差距

你近期抓的 live 帖（`/new` 同批）：**0–5 评、0–2 post score** 为主。  
→ **年榜帖 ≠ 典型发帖结果**；用年榜标题仿写不等于能复制票数。

---

## 3. 高票帖结构分析（可观察，非官方规则）

### 3.1 七类高频爆款基因

1. **制度/金钱震惊（美区权重高）** — 医保、工资误发、数字遗产、国债  
2. **「刚听说一件事」+ 道德不适** — 麻醉无人接、临终坦白  
3. **跨文化真诚发问** — 「Chinese asks here…」「How come Vietnamese…」  
4. **性别/关系/身体（好 faith，非医疗）** — 约会、吸引力、社交规范  
5. **时事名人钩子** — Musk、Epstein、Chappelle（易触 R9，锁帖风险）  
6. **荒诞具象 hypothetical** — 企鹅、管子穿身体、南极  
7. **全民日常 + 小反常** — 鸡蛋、罐头三文鱼、闻雨、图书馆  

### 3.2 标题共性

- **完整问句**，对象具体  
- 常带 **个人立场或经历**（「I just learned」「My friend」「Chinese asks here」）  
- 让人想 **站队/讲故事/科普** → 评论数高 → 帖热度续命  
- **不是**百科作业腔（「Explain quantum」无钩子）

### 3.3 低票/删帖风险（FAQ + 版规）

- FAQ 已覆盖：karma 机制、cake day、username、垃圾扔太空 等 → **R2 重复**  
- R4 医疗、R6 性侵认定、R8 违法、R5 纯梗  
- R9 伪装 rant、引战、议程（年榜里也有踩线仍爆的，**新号模仿=高风险**）

---

## 4. Post karma vs Comment karma（机制）

- **发帖爆火：** OP 得 **post karma**（一次性的帖票）；评论再多不直接给 OP comment karma。  
- **评论养号：** 每条 **comment karma**，可日复利；与 NSQ R1「认真答」文化一致。  
- 年榜帖评论往往 **数百–数千** → 真正「吃满」的是 **早评高赞评论者**，不是只会发帖的 OP。  
- **策略含义：** 若目标是「大量总 karma」，只发帖不评别人 = 放弃一半战场。

---

## 5. 若坚持在 NSQ 发帖：可操作清单

### 5.1 发帖前（必做）

1. [FAQ 搜索](https://old.reddit.com/r/NoStupidQuestions/wiki/index/faq) + sub 内 `search?q=你的关键词&restrict_sr=1`  
2. 确认 **真心不懂**，不是抄年榜标题  
3. 正文 **2–4 句**：你为什么问 + 已查过什么  

### 5.2 标题公式（偏稳，非爆款保证）

```
[个人场景] + [具体困惑] + ?
```

例（风格，勿照抄）：`I just found out X — is that normal or am I missing something?`

### 5.3 较适合「略高票」的选题（新号相对安全）

- 跨国文化差异（真诚、无贬损）  
- 日常生活「我一直以为…结果发现…」  
- 轻量 how/why（食物、语言、习惯），**非** FAQ 烂题  
- 轻哲学（「人是否能理解某些真相」类）— 周榜有，但评论要控长度  

### 5.4 不建议为 karma 刻意发

- 政治引战、种族攻击式提问（R9）  
- 医疗症状、用药（R4）  
- 复制周榜争议标题（易锁帖 + 踩）  
- 「How does karma work」类 FAQ 题  
- AI 写的工整长文帖（R1 文化反感的延伸）

### 5.5 时间与时事

- 周榜 **14.6k 通胀帖** 说明 **当下公共焦虑** 可放大；需 **真实疑问**，非煽动。  
- 美国晚间发帖略有利（未严格验证）；**无法替代内容质量**。  
- r/all 推送 **不可控** — 年榜帖多数有跨版扩散。

---

## 6. 对你当前养号阶段的建议（~29 karma）

| 做法 | 理由 |
|------|------|
| **主刷评论** | 期望值稳定；符合 `account-phase-routing` 阶段 A |
| **NSQ 发帖每周 ≤0–1** | 且仅当你有 **真实、搜不到** 的问题 |
| **不追年榜仿写** | 易 R9/重复/0 票；伤 CQS |
| **要 post karma 爆发** | 接受 **彩票**；别用新号 all-in |

**数量级预期（诚实）：**

- 普通发帖：**0–20 post karma** 常见  
- 周榜级：**2k+** 需话题+运气+可能 r/all  
- 年榜级：**15k+** 不可规划  

---

## 7. 怎样才能有 Upvote？（机制拆解）

Reddit **不公开** NSQ 内排序公式。下面是从高票帖 **可观测特征** 反推的「票从哪来」——用于写帖自检，不是保证上榜。

### 7.1 票 ≈ 早期互动速度 × 共鸣 × 争议度（可控部分）

```mermaid
flowchart LR
  A[标题 + 正文钩子] --> B[前 1–3 小时评论数]
  B --> C[/r/NoStupidQuestions 热榜或 rising]
  C --> D[可选 r/all 外溢]
  D --> E[post score 暴涨]
```

| 因素 | 高票帖表现 | 低票帖表现 |
|------|------------|------------|
| **评论数** | 月 Top 多为 **200–500+** 可见评（通胀帖显示 top 200 / show 500） | 如「进门忘事」21 分钟 **1 评**、**2 post score** |
| **upvote 比例** | 采样帖 **~94%**（通胀、图书馆） | 新帖常 50–100% 但基数极小 |
| **标题** | 一眼能答/能吵/能笑 | 像 FAQ 或课本题 |
| **正文** | 具体场景 + 情绪或细节数字 | 过短且无个人锚点 |

**要点：** 在 NSQ，**评论引擎** 往往比「标题多完美」更重要——没人回复的帖很难进 rising。

### 7.2 四类高票 OP 正文（实帖原文特征）

#### 类型 A — 个人叙事 + 具体数字（通胀 14.6k）

- 标题：公共焦虑（通胀 + afford）  
- 正文：**$6.47/加仑**、**$7/天** 送孩子、panic attack、中产节俭仍扛不住  
- 效果：评论区变成 **集体倾诉**（裁员、养不起孩子），数百条故事 → 算法持续推  
- 风险：贴近 R9 rant，但 **好 faith + 具体事实** 仍过线；**新号仿写易像煽动**

#### 类型 B — 害羞/基础生活（图书馆 2.3k）

- 标题：`Can I just sit and read in a library?` — **极具体、略「傻」但真诚**  
- 正文：1 小时空闲、英国、没卡、不确定有没有座位（**3–4 句**）  
- 效果：评里「这就是图书馆用途」+ 玩梗 *today's lucky 10,000*；**低攻击性，高回复欲**  
- 适合：**新号相对安全** 的爆款形态（仍靠运气）

#### 类型 C — 身体/感官 + 口语（菠萝 5.7k）

- 标题：短、怪、`tingly`  
- 正文：只能吃 4 片、像辣味但没辣味；有错拼 `toe at`；**Edit:** 发现过敏 — 二次传播  
- 效果：科普 bromelain + 一堆「你也是过敏」→ **双轨评论**（科学 + 个人经历）

#### 类型 D — 文化错位 + 自我身份（西语 10.2k）

- 正文仅 **2 句**：白男、同事、每次说 `hola! que onda?` 被笑  
- 效果：最高评类比 *lemme holla at you wassup playa* — **幽默回答占满**，易刷评  

**对比低票** `1tjbn73`（进门忘事，2 票）：

- 标题 OK，正文也真诚（frustrating + 科学名 + 是否记忆力差）  
- 但 topic **偏常见科普**、钩子弱、发布 21 分钟仅 1 条梗评 → **没点燃评论链**

### 7.3 标题：让人想点进来的 5 种句式

| 句式 | 例（月 Top） | 评论 bait |
|------|--------------|-----------|
| **经济/生存** | How is anyone going to afford anything if inflation continues? | 讲故事、骂制度 |
| **规则悖论** | Why drunk can't consent but other drunk decisions count? | 法条/道德辩论 |
| **文化真心问** | Why do Spanish speakers laugh when I say que onda? | 类比、搞笑 |
| **身体/量化的怀疑** | How much blood do I ACTUALLY lose during period… not 2-4 Tbsp | 女性经历、纠正数据 |
| **极简害羞** | Can I just sit and read in a library? | 温暖、略调侃 |

**弱标题：** 无场景、无张力 — `Why do we forget things?`（太宽，像课堂）

### 7.4 正文长度：不是越长越好

| 长度 | 何时有效 |
|------|----------|
| **1–3 句**（50–120 词） | 文化/社交/害羞类（西语、图书馆） |
| **4–8 句 + 数字/情绪** | 经济、关系、职场（通胀） |
| **0 正文仅标题** | 偶尔行，但月 Top 多数 **有正文**；正文负责 **锚定场景** |

**写作要求（像真人，非 AI）：**

- 有错拼/口语可接受（`every`、`id say`）  
- **一个**具体场景，不要百科定义段  
- 可加 `Edit:` 后续（菠萝帖）— 显示真人后续  

### 7.5 「评论 bait」自检表（发帖前打勾）

满分 10，**≥6 再发**（不保证火，但过滤 0 票体）：

| # | 问题 | 1 分 |
|---|------|------|
| 1 | 标题是否是 **完整问句** 且对象具体？ | |
| 2 | 读者能否在 **3 秒** 内知道你在问什么？ | |
| 3 | 正文是否有 **至少 1 个** 个人/地域/职业锚点？ | |
| 4 | 是否有 **具体细节**（数字、原话、国家、身体部位）？ | |
| 5 | FAQ / sub 搜索 **无** 同名帖？ | |
| 6 | 是否让人想 **讲自己的经历**（而不只是查 Wikipedia）？ | |
| 7 | 是否避开 R4 医疗 / R9 引战 / R5 纯梗？ | |
| 8 | 你是否愿意 **2 小时内回复** 前 5 条评论？ | |
| 9 | 正文是否 **≤120 词**（除非你有真实长故事）？ | |
| 10 | 读起来是否像 **手机打出来的**，而非作文？ | |

### 7.6 发布后 0–3 小时（唯一能「操作」的阶段）

1. **发帖后 15–30 分钟** 自己看 `/new` 里帖是否可见（防过滤）。  
2. **尽快认真回复** 前几条顶楼（长Story帖 OP 常不下场；**害羞/文化帖 OP 回复更自然**）。  
3. 若 **2 小时 <5 评**：该帖大概率止步个位数票，**不要删重发**（伤账号）。  
4. **不要** 求 upvote、跨 sub 拉票（R7）。  

### 7.7 月 Top 额外样本（补充题型）

| 票 | 标题 | upvote 驱动力 |
|----|------|----------------|
| 13.7k | Why haven't hackers deleted student loans? | 幻想解法 + 美债/教育愤怒 |
| 12.2k | Denied proposal…what next? | 情感故事续集 |
| 11.8k | Is prison safe if you mind your business? | 恐惧 + 经验帖 |
| 11.1k | Black pepper next to salt — why honor? | 日常厨房全民懂 |
| 10.8k | Japan bosses make you stay doing nothing | 奇闻 + 打工人共鸣 |
| 8.3k | Gluten intolerance vs bread history | 健康迷思辩论 |

### 7.8 新号求 upvote 的诚实优先级

1. **评论** 月 Top 帖的 **rising 子帖**（0–20 评）→ comment karma，风险最低  
2. **发类型 B/C 帖**（害羞生活 / 文化错位）→ 偶尔 100–2k，非稳定  
3. **发类型 A 政治经济长 rant** → 票可能高，但 **R9/踩/滤** 风险最大，**不推荐养号**  

---

## 8. 发帖模板（英文，按类型；须改成你的真实经历）

**B 害羞生活（图书馆型）**

```text
Title: Can I [basic thing] without [fear]?

Body: I have [time/situation]. I'm in [country/city]. I don't have [credential] and I'm not sure if [specific worry]. Is that okay or would I be bothering someone?
```

**D 文化错位（西语型）**

```text
Title: Why do [group] react [way] when I [specific thing I do]?

Body: I'm [honest identity/context]. I work with [who]. Every time I [exact phrase/action] people [reaction]. Am I saying it wrong or is it just funny?
```

**C 感官（菠萝型）**

```text
Title: Why does [food/body thing] feel [weird sensation]?

Body: [how much] before I have to stop. Feels like [analogy]. Not sure if normal or I'm dumb. (optional: mild typo ok)
```

**勿用新号抄 A 通胀长文** — 除非那是你真实刚发生的经历。

---

## 9. 与技能其它文件

| 文件 | 用途 |
|------|------|
| `subreddit-nsq-guide.md` §四 | 发帖基础版规 |
| `subreddit-nsq-comment-playbook.md` | **评论**养号（主路径） |
| `account-phase-routing.md` | 阶段 A 暂缓发帖 |
| `account-building-guide.md` | 过滤/shadowban |

---

*调研日：2026-05-21（§7–8 二轮：正文采样）· 复验：浏览器打开 `/top` + 发帖前 sub 搜索*
