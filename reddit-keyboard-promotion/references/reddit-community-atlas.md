# Reddit 社区图谱（跨版发帖 · 评论 · 养号）

> **常用社区优先读** `communities.md`（本质 + 如何评/如何发）。本 atlas = 20+ sub 扩展与七种原型。  
> **Ask 专册** `askreddit-post-playbook.md` · **NSQ** `subreddit-nsq-guide.md` + `subreddit-nsq-post-karma-research.md`。

---

## 0. Agent 路由（先读这张表）

| 用户意图 | 先读 | 再读 |
|----------|------|------|
| r/AskReddit 标题 / flop | `askreddit-post-playbook.md` | 本文件 §4.1 |
| r/NoStupidQuestions 评/发 | `subreddit-nsq-guide.md` | 本文件 §5.1 · NSQ 发帖调研 |
| 新鲜标题、多社区选题 | 本文件 §2 · §6–§9 | `reddit-search-sop.md` 验重 |
| 帖 3 赞 3 评复盘 | 本文件 §12 + 对应专册 §flop | `account-building-guide.md` CQS |
| **Ask + NSQ 发帖都凉** | **`posting-strategy-recalibration.md`** | 14 天停发帖；勿连推新标题 |
| 键盘买/修/晒 | `subreddit-context.md` · `account-phase-routing.md` | `2026-05-22-large-subs-playbook.md` |
| **抢首评**（NSQ/ELI5/Ask/LPT/pcmr/keyboards/MK） | **`first-comment-playbook.md`** | `communities.md` · `workspace/comments/2026-05-23-first-comment-7-subs.md` |
| 只刷 karma / CQS、补位小版 | **`easy-karma-small-subs.md`** | 小流量易赞清单 §2–§6 |
| 要小流量易赞 | **`easy-karma-small-subs.md`** | 本文件 §3 |

**默认建议（全站）：** 新号 &lt;50 karma → **70% 评论 · 20% 小版 · 10% 发帖**；发帖期望值远低于评论。

---

## 1. 七种社区原型（第一性原理）

Reddit 不是一坨「论坛」，是 **独立法制的小国**。先判 **原型**，再套规则。

| 原型 | 产品是什么 | 发帖难度 | 评论难度 | 新号主战场 |
|------|------------|----------|----------|------------|
| **A 故事舞台** | 标题许可 + 评论树故事 | 高（竞争+验重） | 中（早评/梗） | 评论 `/rising` |
| **B 真诚求知** | 可验证答案 / 机制解释 | 中（R2 搜重） | 中（须真答） | **评论** `/new` 0–8 |
| **C 事实胶囊** | 标题塞满事实 + 可靠来源 | **很高**（源+repost 表） | 低 | 一般 **不发帖** |
| **D 建议法庭** | OP 叙事 + 评判/建议 | 中–高（版规严） | 高（易踩线） | 新号 **慎入** |
| **E 观点擂台** | 争议立场 + 论证 | 高（删帖/踩） | 高 | 阶段 B+ |
| **F 爱好技术** | 图/规格/故障/清单 | 中（flair/karma） | 中（事实） | 小版 + 0–8 评 Help |
| **G 元/Support** | 问 Reddit 怎么用 | 低–中 | 低 | 新号友好 |

**权限结构（跨原型）：** 和 AskReddit 一样，高表现帖往往给评论者 **「讲自己的故事」** 或 **「低摩擦站队」** 的许可；*you've seen someone…* 类见证问法在 **A/B** 都偏弱（见 `askreddit-post-playbook.md` §10）。

---

## 2. 社区速查表（按原型）

| Sub | 原型 | 规模级 | 发帖 | 评论 | 专册/章节 |
|-----|------|--------|------|------|-----------|
| r/AskReddit | A | 4700万+ | 彩票 | `/rising` 短评 | `askreddit-post-playbook.md` |
| r/CasualConversation | A | 大型 | 可；禁 AI/引流 | 共鸣 3–20 词 | §4.2 |
| r/tifu | A | 大型 | 须 **TIFU** 前缀+故事 | 接梗/共鸣 | §4.3 |
| r/offmychest | A | 大型 | 倾诉；版规严 | 少建议多倾听 | §4.4 |
| r/NoStupidQuestions | B | 610万+ | 50+ karma 再试 | **养号主战场** | NSQ 全套 |
| r/explainlikeimfive | B | 2300万+ | 问题+细节；禁 Yes/No | 类比+一句机制 | §5.2 |
| r/OutOfTheLoop | B | 大型 | 须 **URL/梗上下文** | `answer:` 格式 | §5.3 |
| r/TooAfraidToAsk | B | 大型 | 敏感；spam 时限新号 | 友善真答 | §5.4 |
| r/todayilearned | C | 2500万+ | **源+repost 表** | 补来源/纠错 | §6.1 |
| r/LifeProTips | E→技巧 | 大型 | **LPT:** 格式；禁 AI | 少 | §7.2 |
| r/unpopularopinion | E | 大型 | 真·少数观点+论证 | 易战 | §7.3 |
| r/NewToReddit | G | 中型 | 欢迎 | 极短帮助 | §8.1 |
| r/relationship_advice | D | 1100万+ | 叙事+细节 | **新号勿评** 除非用户坚持 | §7.1 |
| r/AmItheAsshole | D | 超大 | 格式极严 | 新号 **暂缓** | §7.1 |
| r/pcmasterrace | F | 超大 | Tech 周二等 | Question 0–8 评 | large-subs playbook |
| r/buildapc | F | 超大 | 整机规则 | 外设段单线 | 同上 |
| r/keyboards / r/MechanicalKeyboards | F | 大 | karma/flair | Help 0–8 | `subreddit-context.md` |

---

## 3. 账号阶段 × 社区（扩充 routing）

与 `account-phase-routing.md` 一致，此处强调 **发帖**。

| 阶段 | 评论主战场 | 可尝试发帖 | 暂缓发帖 |
|------|------------|------------|----------|
| **A 0–50** | NSQ、Casual、NewToReddit、BudgetKeebs 周帖 | NewToReddit（真问题） | AskReddit 彩票、TIL、LPT、AITA、relationship |
| **B 50–150** | + ELI5、pcmr 每日串、keyboards Help | NSQ（验重）、Casual 生活帖 | TIL、unpopularopinion |
| **C 150+** | 大版 `/new` 早评 | 按专册验重后试 A/C/E | 仍避重复梗、无来源 TIL |

**CQS > karma：** 大版 5 票 ≠ 成功；被滤 &gt; 不评（`account-building-guide.md`）。

---

## 4. 原型 A — 故事 / 社交 / 叙事

### 4.1 r/AskReddit

- **本质：** 故事采掘；标题 = 舞台（`askreddit-post-playbook.md`）  
- **发帖：** 五公式、50–200 字符、美东白天、首 30 分钟定生死  
- **饱和：** 省钱变亏子集、*seen someone*、*stopped buying 2026*、神帖公式  
- **Flop 样本：** `expensive mistake … you've seen someone … save money` → §10 专册  

### 4.2 r/CasualConversation

| 项 | 要点 |
|----|------|
| **气质** | 暖、闲聊、共鸣；**不是** NSQ 那种顶层必须百科答 |
| **评论** | 3–20 词 Filler/Me-too/接梗；**无链接、无产品、无 AI 腔** |
| **发帖** | 生活小事、情绪、轻幽默；版规常禁 **AI 生成**（2025–2026 mod 战 slop） |
| **与 NSQ 分工** | 要梗/情绪 → Casual；要机制答案 → NSQ |
| **新号** | 阶段 A **评论** 为主；发帖非必须 |
| **Flop** | 长文说教、像 therapist、复制粘贴励志 |

**标题例（发前搜 sub）：**  
`What's a small thing that made your week better for no good reason?`  
→ 偏泛，须验重；更好：**具体场景**（通勤/室友/宠物）。

### 4.3 r/tifu

| 项 | 要点 |
|----|------|
| **格式** | 标题 **必须以 `TIFU` 开头**；正文讲故事 |
| **内容** | 真实感失误叙事；按版规选 S/M/L flair（读当前 wiki） |
| **评论** | 共鸣、幽默、一句「how are you still alive」类 |
| **新号** | 可发但需 **好故事**；低 effort 秒删 |
| **勿** | 无后果的抱怨、政治、纯钓鱼 |

### 4.4 r/offmychest / r/TrueOffMyChest

- **发帖：** 倾诉向；**非** 求键盘/求方案  
- **评论：** 倾听 &gt; 说教；**新号慎**（敏感+易踩）  
- **推广/技能：** 默认 **不生成** 除非用户明确要求（`reddit-platform-guide.md` Type I）

---

## 5. 原型 B — 解释 / 求知

### 5.1 r/NoStupidQuestions

- **评论：** 阶段 A **首选**；12–35 词、顶层真答、禁 google it  
- **发帖：** 见 `subreddit-nsq-post-karma-research.md` — **长尾彩票**，稳定涨分靠评论  
- **相近分流：**  

| 问题类型 | 去哪 |
|----------|------|
| 不好意思问的 everyday why/how | NSQ |
| 要 5 岁类比 | r/explainlikeimfive |
| 梗/新闻背景 | r/OutOfTheLoop |
| 羞耻/敏感 | r/TooAfraidToAsk（更严） |

### 5.2 r/explainlikeimfive

| 项 | 要点 |
|----|------|
| **发帖** | 复杂概念 + 为什么不懂；**禁止** 简单 Yes/No、纯意见 |
| **评论** | **类比 first**，再 **一句** 机制；禁维基墙 |
| **饱和** | 常见科普（量子、加密货币入门）反复 |
| **新号** | 评论 Help 帖 &gt; 自己发帖 |
| **Flop** | 只答 Yes/No、无 E 的 L5 |

### 5.3 r/OutOfTheLoop

| 项 | 要点 |
|----|------|
| **发帖** | 标题 = 当前、中立、连贯问句；**正文须含上下文+链接**（梗/新闻从哪来） |
| **评论** | 顶楼以 `answer:` 或 `question:` 开头（读当前 rules） |
| **必做** | **先搜** 是否问过 |
| **场景** | 「这个 meme/名人/事件怎么回事」— 2026 时效帖窗口短 |

### 5.4 r/TooAfraidToAsk

- 比 NSQ **更敏感**；spam 期可能 **限新账号**  
- 新号：**只评论** 且只答你有把握的  
- 禁 troll、道德审判、医疗认定  

---

## 6. 原型 C — 事实 / TIL

### 6.1 r/todayilearned

**不适合新号「练发帖」** — 删帖率高、需研究源。

| 规则摘要 | 要求 |
|----------|------|
| R1 可验证 | 链接 **直接** 到可靠来源；支撑 **标题全部** 主张 |
| R2 | 无个人观点/轶事标题 |
| R3 | 无 **近 2 个月** 的新闻源 |
| R4 | 无近期政治/议程 |
| R6 标题 | 须 **TIL …**；标题 **standalone**（读者不点链接也能懂） |
| Repost | wiki **frequent TIL list** — 必查 |

**发帖工作流：**

1. 找 **冷门但有趣** 事实（非 wiki 已烂）  
2. 找 **BBC/学术/政府** 等源  
3. 标题：`TIL [complete fact in title]`  
4. 评论区预期：纠错、补 context — **发帖人不靠评论树涨票**

**Flop 原因：** 无源、repost list、标题需点开才懂、个人轶事 TIL。

---

## 7. 原型 D/E — 建议 / 观点 / 技巧

### 7.1 r/relationship_advice · r/AmItheAsshole

| 项 | 要点 |
|----|------|
| **历史** | AITA 等常由 AskReddit **拒帖** 分叉而来（First Monday 族谱研究） |
| **发帖** | 长叙事+细节+版规格式（AITA 有固定模板/flair） |
| **评论** | 评判/建议 — **易引战、伤 CQS** |
| **技能默认** | 新号 **不主动生成**；用户坚持才做，且只 **一条** 中立澄清 |

### 7.2 r/LifeProTips

| 项 | 要点 |
|----|------|
| **格式** | 标题 **`LPT`** 或 **`LPT Request`**（Request 常仅周五） |
| **正文** | 技巧 + 解决什么问题；须 **具体** |
| **禁** | 常识、礼貌、违法、医疗/驾驶/关系等禁题；**AI = ban** |
| **新号** | 非养号首选；易因「常识 tip」被删 |

### 7.3 r/unpopularopinion

- 须 **真·少数观点** + 正文论证；**非** 只是挑衅  
- 大量 **AgreeActually** 反杀 → flop  
- 阶段 B+ 再考虑；**先评论** 观察语气  

---

## 8. 原型 G — 元 / 新手

### 8.1 r/NewToReddit

| 项 | 要点 |
|----|------|
| **用途** | karma 冷启动、问版规、问 karma 机制 |
| **发帖/评** | 真诚新手问题；极短友善答 |
| **安全** | 低争议；**勿** 外链推广 |
| **注意** | 答案常指向 wiki；重复 FAQ 会被指 |

---

## 9. 原型 F — PC / 游戏 / 键盘（摘要）

细节见 `subreddit-context.md`、`workspace/comments/2026-05-22-large-subs-playbook.md`。

| Sub | 发帖 | 评论 |
|-----|------|------|
| r/MechanicalKeyboards | Gallery/IC 规则严；Question flair | 0–8 评 Help；忌空夸 |
| r/keyboards | Help 帖 | 单 tradeoff；避 HE 大战 15+ 评 |
| r/pcmasterrace | Tech 主题日 | `[Question]` 0–8 评 |
| r/buildapc | 整机格式 | **只答** 外设段 |

**新号勿：** Amazon 短链、一帖列 5 型号、buildapc 长评楼硬拼。

---

## 10. 全站发帖 mechanics（各原型共用）

### 10.1 五种帖型

| 类型 | 适用 |
|------|------|
| Text | Ask、NSQ、Casual、TIFU、LPT、OOTL |
| Link | TIL、新闻型（多数大版限制新号 link） |
| Image | MK、battlestations |
| Poll | 多数讨论版限制；AskReddit 禁低质 poll |
| AMA | 特殊；非养号 |

### 10.2 早期速度（与 AskReddit 相同）

- **0–30 min：** ~5–10 upvote 否则难 Rising  
- **0–3 h：** 评论滚动决定寿命  
- 美东 **7:00–16:00** 发（泛版）  

### 10.3 Automod / CQS

- 各 sub **私有** karma/年龄阈值（不公开）  
- 新号 link 帖、多 sub 同文 → 高危  
- 见 `account-building-guide.md`、Reddit Poster Eligibility / CQS 文档  

---

## 11. 跨社区饱和地图（发帖选题）

除 `askreddit-post-playbook.md` §5 外，**全站慎发**：

| 话题簇 | 常见烂梗 | 更好角度 |
|--------|----------|----------|
| 省钱翻车 | save money cost more、frugal mistake、**seen someone** | 第一人称；立法假想；具体物件 |
| 2026 涨价 | stopped buying 2026 | 真实年费披露；订阅羞耻叙事 |
| 怀旧 | miss the 90s | 无红点/群聊死了等 **新机制** |
| 免费资源 | free things online | boring tool beats AI |
| 人生建议 | best advice / favorite | 反常识 **一条** rule you broke |
| TIL 百科 | 企鹅/可乐/常见 wiki | frequent list + 新源 |
| LPT | 常识 tip | 极具体 niche 场景 |

---

## 12. Flop 诊断（按原型）

| 现象 | A 故事 | B 求知 | C TIL |
|------|--------|--------|-------|
| 3 评 3 赞 | 题眼旧/见证他人/无 lurker hook | 重复 FAQ/google it/顶层笑话 | repost/无源/标题不 standalone |
| 帖被删 | 版规/引流/非开放问 | 医疗/引战/重复 | R1–R7 |
| 有评无票 | 正常；A 靠标题票 | NSQ 常 **评>帖** | 正常 |

**通用：** 首小时未起 → **别删重发**；改 **评论** 或 **换 sub 原型**。

---

## 13. Agent 输出：多社区选题 / 发帖建议

```markdown
## Reddit 社区发帖/选题

**账号阶段：** A | B | C

### 推荐路径（默认）
- **主攻：** [评论 @ sub1, sub2]
- **可选发帖：** [sub] — 原因
- **勿发：** [sub] — 原因

### 备稿（每条约 1 个原型）

#### 1. [r/Sub] — 原型 A/B/…
**标题（EN）：** …
**验重搜索词：** …
**结构分（若 A/Ask）：** __/32
**饱和风险：** 低/中/高 — 撞 §11 哪条
**OP 首评：** …
**发帖窗口：** 美东 …

### Flop 复盘（若用户提供）
- 原型：…
- 死因：§12 行…
- 改写/转评论：…
```

---

## 14. 链接索引（浏览器验规）

| Sub | Rules / Wiki |
|-----|----------------|
| AskReddit | https://www.reddit.com/r/AskReddit/wiki/index |
| NoStupidQuestions | https://www.reddit.com/r/NoStupidQuestions/about/rules |
| explainlikeimfive | https://www.reddit.com/r/explainlikeimfive/about/rules |
| todayilearned | https://www.reddit.com/r/todayilearned/wiki/index |
| CasualConversation | https://www.reddit.com/r/CasualConversation/about/rules |
| LifeProTips | https://www.reddit.com/r/LifeProTips/about/rules |
| OutOfTheLoop | https://www.reddit.com/r/OutOfTheLoop/about/rules |
| NewToReddit | https://www.reddit.com/r/NewToReddit/wiki/index |

**验重 SOP：** `reddit-search-sop.md`（sub 内搜索 · Past month · Sort new）。

---

## 15. 文档分工（技能内）

| 文件 | 职责 |
|------|------|
| **本文件** | 跨社区路由、原型、饱和、flop 总表 |
| `askreddit-post-playbook.md` | AskReddit 发帖深度 |
| `subreddit-nsq-*.md` | NSQ 评/发深度 |
| `account-phase-routing.md` | 阶段 × 去哪 **评** |
| `reddit-platform-guide.md` | 帖型 A–I、跨版语气 |
| `subreddit-context.md` | 键盘垂直 |
| `2026-05-22-large-subs-playbook.md` | 大版 **筛帖评**，非发帖 |

*路径：`reddit-keyboard-promotion/references/reddit-community-atlas.md`*
