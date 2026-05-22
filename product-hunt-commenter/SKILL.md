---
name: product-hunt-commenter
description: >-
  根据用户提供的 Product Hunt 产品链接生成高质量英文评论草稿，注重账号安全与真实感。
  CQS 提升优先于评论质量。不用于批量灌水、伪造使用经历或规避平台规则。
  遇到陌生产品类别必须先搜索。Use when the user shares Product Hunt links,
  launch pages, maker threads, or asks for PH comment drafts.
---

# Product Hunt Commenter — 大幅更新版

_基于 100+ 条真实 PH 评论的深度分析重写_

---

## PH 评论的本质（最重要）

**PH 评论区本质上是 maker 和早期用户之间的公开对话，不是留言板。**

高质量评论的共同特征：**让 maker 有话可接，让其他读者觉得"这个人真的用过/想过这个产品"。**

---

## 核心发现：真实评论的 DNA

真实 PH 评论有三个维度，缺一不可：

### 1. Personal Context（个人情境）
真实用户会提到**自己的具体情况**，而不只是泛泛的"great tool"。

```
✅ 真实: "I have 4000 subscribers, should I switch from Mailchimp?"
❌ AI感: "This is a great newsletter tool!"

✅ 真实: "I am coaching at a hackathon for college students"
❌ AI感: "Perfect for students!"

✅ 真实: "I'm a very heavy Roam user but have followed Logseq closely"
❌ AI感: "Great alternative to other note apps!"
```

### 2. Specific Observation（具体观察）
真实用户会提到**产品的某个具体细节**，通常是架构、设计决策、或某个功能。

```
✅ 真实: "The 3AM memory consolidation is the most interesting architectural decision here"
❌ AI感: "Great memory feature!"

✅ 真实: "Most local agents treat memory as a simple append log (which means context gets bloated fast)"
❌ AI感: "Good memory management!"

✅ 真实: "Love it. Most local agents treat memory as a simple append log"
```

### 3. Natural Ending（自然结尾）
真实评论**没有一个标准结尾**。很多人：
- 直接停，没有结尾
- 问一个实际问题
- 分享自己的使用计划
- 留一个 open-ended 的想法

```
✅ 真实结尾: "not sure how this compares to X"
✅ 真实结尾: "can't wait to try this"
✅ 真实结尾: "would love to hear your feedback"
✅ 真实结尾: (直接停，什么都没有)
❌ AI感结尾: "Upvoted 👍" (每条都加)
```

---

## 改进后的 Comment Types

### Type 1: Insight (观察性)

**核心特征：** 指出产品某个具体细节 + 个人解读

```
模板结构：
[个人背景/情况]。[对产品某个具体设计的观察]。[这个设计为什么好/可能的问题]。

真实示例（来自 Logseq 评论）：
"I am a very heavy Roam user but have followed the early developments of Logseq 
and have been impressed by the development. I like the Roam-like functionality 
with the privacy of local files that you get with Obsidian."

真实示例（来自 CraftBot 评论）：
"The shift from reactive to proactive is a much harder design problem than most 
agent products acknowledge. Reactive agents fail silently. Proactive agents fail loudly, 
wrong actions on your behalf..."

真实示例（来自 Napkin 评论）：
"Creating mockups in PS can be really annoying. And you never have the 'real' size 
view and feeling of how it will work in the mobile phone's screen, so this could 
definitely be practical."

真实示例（来自 Logseq 评论）：
"Most local agents treat memory as a simple append log (which means the context gets 
bloated or stale fast). This one is different."
```

**何时用：** 对产品有真实理解，有具体观点要说
**风险等级：** 🟡 中等（观点明确，但不激进）
**频率：** 每篇 1-2 条

---

### Type 2: Question to Maker（向 Maker 提问）

**核心特征：** 基于对产品的真实理解，问一个具体问题

```
模板结构：
[观察到一个具体点]。[关于这点的实际问题是？]

真实示例：
"Most local agents treat memory as a simple append log — does it have a way to 
auto-prune old events?"

"@maker quick question on the 'Build from scratch' flow — how does it handle 
complex API integrations? if i want my UI to pull data from multiple third-party 
tools, can it set up those connections too?"

"Is it mainly one agent doing everything, or do you use multiple agents with 
different roles that work together in some kind of orchestration?"

"what happens if local machine runs out of storage for logs/memory?"

"Any Android devs wanna help?"

"Anyone know how they created that auto-playing demo video? Is there some tool 
that makes that easy to do?"

真实示例（简单问题）：
"is there a free tier?"
"does this work with Gmail only?"
"how hard is setup?"
"any plans for Windows?"
```

**何时用：** 对产品有真实好奇，不是为了问而问
**风险等级：** 🟢 安全（提问永远不会错）
**频率：** 每篇 1-2 条

---

### Type 3: Filler（废话，纯情绪混入）

**核心特征：** 3-15 词，纯情绪，不给任何具体信息

```
真实 PH Filler 示例（从真实评论中提取）：
```
"Ooh This One, Obsessed with This"
"Need This so Bad Rn"
"This Is Exactly What I Was Looking For"
"Finally Someone Gets It, Saving This"
"Immediately Saved, This Goes Hard"
"Noted, Cant Wait to Try This"
"Obsessed with the Concept"
"This + Conference Season = Im Set"
"Not Sure Why but I Genuinely Love This"
"This Is So Satisfying"
```

注意真实用户的 Filler 特点：
- 缩写: "Im Set", "Ngl", "Rn", "Cant"
- 首字母大写（大多数）
- emoji 实际很少出现（CraftBot 100+ 评论仅 1 个 emoji）
- 非常口语化
- 不需要 emoji 也能表达情绪
```

**为什么安全：** 没说任何具体 claims，永远不可能错
**频率：** 纯 Filler（Ooh/Noted/Saving This）禁止；如需 Filler 用 Personal Experience 代替

**注意：** 真实 PH 社区对纯情绪无内容的评论反应冷淡，甚至被认为是刷存在感。

---

### Type 4: Short Praise + Reason（简短夸赞+理由）

**核心特征：** 1-2 句话，夸赞 + 具体理由（不是泛泛的"great!"）

```
模板：
[评价]。[具体理由 OR 具体使用场景]。

真实示例：
"Napkin is sweet! The interface is really easy to use after a bit of poking around. 
Just made this in a few minutes."

"Impressive, all around. Great job, and congrats on the launch!"

"Make is an amazing theme. Perfect balance of existing infrastructure and 
customization."

"Wow, what a great job! I could not find any info on pricing."

"Solid launch. I like that it runs on your own infra."
```

**注意：** 不要每次都加 "Upvoted 👍"

---

### Type 5: Problem Validation（验证问题确实存在）

**核心特征：** 提到一个真实的痛点，验证 maker 说的问题是真的

```
真实示例：
"The number of message sources and contacts can become a trouble."

"Creating mockups in PS can be really annoying."

"Today, most software, when you need a new feature, you email the developer. 
If you are lucky, it ships six months later. If not, you may never hear back."

"I wasn't aware of any similar competitors when I started building..."
```

---

### Type 6: Personal Use Case / Sharing（分享个人使用场景）

**核心特征：** 提到自己或别人会怎么用这个产品

```
真实示例：
"We use Surfkey to grow VEED.LIVE, jumping into every relevant convo and 
providing value, and plugging our page where relevant."

"We use it to go straight from lo-fidelity sketches to high-fidelity prototypes 
without touching code."

"I am thinking about connecting it to some existing Notion databases to make 
use of it as internal dashboards."

"I have been using Logseq for a few months. The pace of development is 
incredibly fast, so much is improving every month."

"As someone who just spent three days trying to figure out Sendgrid to send a 
single e-mail to our customers, I can really appreciate a much lighter touch."
```

---

## Ending 多样性（不再每条加 Upvoted）

```
**好的结尾（自然）：**
- (直接停，什么都没有)
- "not sure how this compares to X"
- "cant wait to try"
- "noted"
- "this goes hard"
- "immediately saved"
- "obsessed with this"
- "ooh"
- "following for updates"
- "checking the demo now"
- "will report back"
- "**Good luck with the launch!**" — Launch 日产品可用
- "**Congrats on the launch!**" — Launch 日产品开场白

**避免的结尾：**
- "Upvoted 👍" （每条都加 = bot 感）
- "Great product! 🚀" （太泛）
- "Bookmarked!" （太正式，"saving this" 更真实）
```

---

## 真实评论格式多样性（核心规则）

**问题诊断：** 如果每条评论结构完全相同 = AI 感 100%

真实 PH 评论的格式是**随机的、不一致的**：

```
✅ 有的加粗关键词（吸引眼球）
✅ 有的不加粗（纯口语）
✅ 有的用破折号
✅ 有的用句号断成多句
✅ 有的只有半句话
✅ 有的很长有的很短
✅ 有的小写开头
✅ 有的全大写强调
✅ 有的问句结尾
✅ 有的直接没结尾
```

**模板化评论示例（必须避免）：**
```
❌ "**voice → structured summary → task → report** — that's a real workflow, not just transcription"
❌ "**the fact that it turns voice into finished work** — not just notes — is the differentiator here"
❌ "**context-aware + local + proactive** — thats the trifecta"
```

**多样化格式示例（学习这种）：**
```
✅ "The 3AM Memory Consolidation Is the Most Interesting Architectural Decision Here"
✅ "Love It. Most Local Agents Treat Memory as a Simple Append Log"
✅ "Wait What — This Actually Works on Localhost?"
✅ "Saving This. Need to Try Tonight"
✅ "Most Local Agents Treat Memory as a Simple Append Log (Which Means Context Gets Bloated). This One Is Different."
✅ "Not Sure How This Compares to X but Going to Try Anyway"
✅ "Ooh"
✅ "I've Been Waiting for Something Like This for Months"
✅ "Obsessed with the Concept"
✅ "[@ProductName](link)'s Living UI Pushes This in a Useful Direction"
✅ "The Agent Era Is Reshaping the Interface. TUI Is One Direction..."
```

**@mention 风格示例（来自真实 CraftBot 评论）：**
```
✅ "[@CraftBot](link)'s Living UI pushes this in a useful direction. The interface is no longer a fixed app you buy and adapt to."
✅ "[@maker](link) What Happens if Local Machine Runs Out of Storage for Logs/Memory?"
✅ "Not Sure How This Compares to X but Going to Try Anyway"
```

**长评论格式示例（来自真实 CraftBot/Logseq 评论）：**
```
✅ "The Shift from Reactive to Proactive Is a Much Harder Design Problem Than Most Agent Products Acknowledge. Reactive Agents Fail Silently, You Just Don't Get a Good Answer. Proactive Agents Fail Loudly, Wrong Actions on Your Behalf..."
✅ "The Agent Era Is Reshaping the Interface. TUI Is One Direction, and It Makes More Sense for Devs. But I Don't Think Agents Remove the Need for UI. Visual Interfaces Are Still One of the Best Ways to Compress State, Context, and Actions into Something Humans Can Understand Quickly."
```

**格式多样性检查表：**

| 检查项 | 要求 | 常见错误 |
|--------|------|---------|
| 长度差异 | 3词/8词/15词/25词/40+词混合 | 全在15-20词区间 |
| 加粗使用 | 不要每条都加粗 | 每条都有 `**`** |
| 断句方式 | 句号/破折号/无标点混合 | 全用破折号 |
| 开头大小写 | 大多数首字母大写 | 过度追求小写开头 |
| 结尾方式 | 问句/无结尾/短词/省略号混合 | 全部完整句结尾 |

**真实评论还发现的新模式：**

| 新发现 | 示例 | 说明 |
|--------|------|------|
| @mention 产品/maker | `[@CraftBot](link)'s Living UI...` | 提及产品是真实讨论的标志 |
| 评论可以很长 | Zac Zuo 的评论超过 80 词 | 深度分析型评论很受欢迎 |
| Maker 回复很长 | Korivi 的 maker 回复是完整工程解释 | 有观点的评论 maker 会深入回复 |
| 可包含外部链接 | `...reshaping the [interface](https://x.com/...)` | 引用外部资源增加可信度 |
| 负面/质疑可以很长 | Tyler Wriston 质疑 60+ 词 | 深度质疑比简单负评更有价值 |
| 问题非常具体 | `does it have a way to auto-prune old events?` | 越具体的问题越显得真实 |
| 少用 emoji | 真实评论 emoji 很少 | 多用文字表达情绪 |

**长度控制参考：**
- 3-8词：纯情绪 Filler
- 8-15词：短句
- 15-25词：标准评论（推荐区间）
- 25-40词：长评论（可接受，不要超过5条/篇）
- 40+词：超长评论（每篇最多1-2条）

---

## Anti-AI Pattern Ban List（更新版）

**绝对禁止（出现 2 个以上 → 重写）：**

| 禁止词/短语 | 真实用户会说 |
|------------|-------------|
| the real unlock | _(从不说)_ |
| a game changer | _(从不说)_ |
| next-level | _(从不说)_ |
| says a lot about | _(从不说)_ |
| mature ecosystem | _(从不说)_ |
| the key differentiator | _(从不说)_ |
| genuine _(ly)_ | 真的不说 |
| excels at | _(从不说)_ |
| the sweet spot | _(从不说)_ |
| the finer details | _(从不说)_ |
| **workflow (noun)** | **用动词形式 "workflowing" 或换说法** |
| at scale | _(从不说)_ |
| adoption flywheel | _(从不说)_ |
| edge over | _(从话说)_ |
| fragmented like | _(从不说)_ |
| it's all about | _(从不说)_ |
| Killer feature | _(几乎不说)_ |
| game changer | _(几乎不说)_ |

**更可靠的检测：** 如果每条评论的结构都一模一样 = 肯定像 AI

---

## 评论价值分层（必须遵守）

### 第一梯队：有具体细节的问题
让 maker 觉得你是真的理解了产品才能问出这种问题。

❌ 泛泛的: "Does it support other editors?"
✅ 真实的: "Does it work with VS Code and Cursor both?"
✅ 真实的: "Windsurf or other newer editors?"
✅ 真实的: "存档文件夹是固定路径还是可以配置的？"
✅ 真实的: "未来会支持 GBA 以外的模拟平台吗？"

**技术问题要显示"深度用户"视角，不是围观者：**
❌ "Does it support other editors?" — 围观者在问功能
✅ "Does it work with Windsurf? I switched last month and still finding what works" — 深度用户在寻求对标

### 第二梯队：有个人经验的短句
不是赞美产品，而是说你自己的场景，带具体情绪。

❌ 泛泛的: "This is so clever"
❌ 泛泛的: "Game Boy aesthetic is perfect" — 夸美学风格但没说为什么
✅ 真实的: "I wait for Claude Code to run and never know what to do"
✅ 真实的: "Funny watching the little guy work" — 具体情绪，有画面
✅ 真实的: "I'd actually leave this running in the background"

**Personal Experience 的标杆：**
> "Funny watching the little guy work"
比所有 "so clever" 都真实，因为有具体情绪和画面。

### 第三梯队：对产品决策的具体反应
为什么这个决策对你重要，而不只是夸 maker。

❌ 泛泛的: "No telemetry is great, you have integrity"
❌ 太 slogan 化的: "No telemetry is the right call — privacy matters" — 像写 tagline
✅ 真实的: "No telemetry is the right call for a dev tool"

**Short Praise 也要有具体内容：**
❌ "X is perfect" / "X is great" — 没内容
✅ 要说为什么，不能只下结论

### 第四梯队：产品最有趣的工程决策（最容易引发对话）

**这是最容易引发 maker 回复的点：** 产品里最有趣的工程决策，但目前很少有人评论。

例如 Standboy 的自动唤醒/收起机制：
> "The auto wake/sleep mechanism is the most interesting part — you don't have to remember to switch it on/off"

这个机制让 Standboy 和普通 side project 不同，因为它意味着你不需要手动管理状态。这个细节比"Game Boy in your sidebar"更有意思，但目前没有任何评论提到它。

---
### 无用/有害的评论类型（必须删除）

**纯 Filler：**
- "Ooh" / "Noted" / "Saving This" — 完全没有信息，maker 无法回应，读的人也没收获
- 活跃社区里这类评论会被忽略，甚至被认为是刷存在感

**重复 maker 原话再夸：**
- maker 说了什么，你复述一遍然后说"这是我读过最诚实的描述"
- 这不是评论，这是表演

**分析产品营销的评论：**
- 站在产品之外评价它的策略，读起来像顾问而不是用户
- PH 社区对这种 tone 非常敏感

**撞车已有评论：**
- 发之前必须先看已有评论
- launch 日前几小时流量最集中，撞车概率最高

---

## Personal Perspective 句式（参考，不是模板）

这些是**句式参考**，不是每条都要用完的检查清单。真实评论往往是几句话的随机组合，不是填充模板。

**Personal Struggle 引出（真实评论最常见的开头）：**
```
✅ "Been struggling with [problem] — good to see someone addressing this"
✅ "I've been using [competitor] but [complaint] — this looks different"
✅ "Finally someone building [specific feature] instead of just [generic thing]"
✅ "Been looking for something like this for [time]"
```

**可用句式（选1-2个混入评论中，不要每条都用）：**
```
✅ I'd probably use this for [specific use case]
✅ my first concern would be [specific question]
✅ not sure how hard this is technically, but [observation]
✅ I could see this being really useful if [condition]
✅ Fair point. [honest concern or question]
✅ I'm curious about [specific technical aspect]
✅ I'm a [category] user and [specific experience]
✅ Been using [competitor] for [time], curious how this compares
✅ Haven't tried this yet but [reason to try / concern]
✅ The [specific feature] is what caught my attention
✅ The [architectural decision / design choice] is interesting
```

**Launch 日特殊句式：**
```
✅ "Congrats on the launch!"
✅ "Good luck with the launch!"
```

**最自然的评论往往是：**
```
✅ "Been struggling with AI notetakers' output being isolated — good to see someone consolidating it with persistent memory"
✅ "The memory feature stood out to me — it's useful when AI tools can connect discussions across meetings"
✅ "Congrats on the launch! Curious whether it would sort recordings into related piles automatically"
```

**技术人员评论的独特模式（来自真实 Vanshvardhan 评论分析）：**

这条真实评论拿到了 maker 回复，说明它被认可为真实用户：
> "Finally, a proper debugger for the agent era. Bridging traces over to other agents via MCP is such a smart architectural move. I love the focus on local-first—it makes iterating on sensitive agent logic much more viable."

**技术人员评论特征：**
```
✅ "such a smart [architectural/design choice]" — 明确的价值判断
✅ "I love the focus on [specific technical point]" — 带具体技术点的热情
✅ "makes [X] much more viable" — 暗示有对比基准，用过类似产品
✅ "Does [product] support [very specific technical detail]?" — 问题具体到工具调用层
```

**vs 我生成的版本：**
```
❌ "First local debugger for agents — finally someone building for the tool-call layer where bugs actually live"
```

**差距分析：**
- 我的版本：太喜欢用破折号，"Finally someone building..."太模板化
- 真实版本：一口气长句，第一人称"I love"，技术细节"MCP"，洞察"makes X more viable"
- maker 回复了这条并追问，说明觉得这条值得深入讨论

**教训：** 技术类产品的真实用户评论可以有热情，但热情是建立在具体技术理解上的。

---

## 深入理解产品的工作流

**用户给链接后，必须做：**

1. **先搜索产品信息**（Tavily），了解：
   - 产品解决什么问题
   - 目标用户是谁
   - 和同类产品有什么不同
   - maker 是谁/什么背景

2. **生成评论前问自己：**
   - 我（作为用户）对这个产品有什么**真实好奇**？
   - 产品哪个**具体设计**引起了我的注意？
   - 我自己的**具体情况**能怎么关联到这个产品？
   - 如果我要提问，会问什么**具体问题**？

3. **评论长度控制：**
   - Filler: 3-15 词
   - Short Praise: 1-3 句
   - Question: 1-3 句
   - Insight: 2-5 句
   - Personal Use Case: 2-5 句
   - **不要超过 5 句**

4. **每篇产品生成 8-10 条**（不是越多越好，宁少勿滥），其中：
   - 2-3 条 Personal Experience（个人场景短句）
   - 2-3 条 Specific Question（具体问题）
   - 2-3 条 Short Praise + Reason（短评价+理由）
   - 1-2 条 Insight（个人洞察）
   - **禁止：纯 Filler（Ooh/Noted/Saving This）**

5. **生成前必做：先完整读所有已有评论**
   - [ ] 确认没有和已有评论撞车
   - [ ] 识别真实评论风格，提取真实用户说了什么

6. **生成后自检（必须执行）：**
   - [ ] 数量是否控制在 8-10 条？（不要凑数）
   - [ ] 有没有纯 filler？（删除 Ooh/Noted/Saving This）
   - [ ] 有没有撞车已有评论？（对比真实评论列表）
   - [ ] 有没有 maker 原话复述？（删除"这是最诚实的描述"类）
   - [ ] 有没有过于 meta 的分析？（删除评价产品营销策略类）
   - [ ] Anti-AI Ban List 检查（尤其："the workflow" 禁止）
   - [ ] 不要生成格式完全相同的"姐妹评论"

---

## 输出格式模板（精简版）

```markdown
# 2026-05-15 评论草稿

## Product Hunt

### [产品名] — [一句话描述产品]

**产品背景：** [产品解决什么问题，目标用户，和竞品差异]
**来源：** [链接]

**真实评论已分析（避免重复）：**
- [已有评论1的关键点]
- [已有评论2的关键点]

---

**评论草稿（8-10条，禁止纯Filler）：**

1. **评论内容** | 中文：核心意思 | 类型：Personal Experience / Question / Short Praise / Insight

2. **评论内容** | 中文：核心意思 | 类型：Personal Experience / Question / Short Praise / Insight

3. **评论内容** | 中文：核心意思 | 类型：Personal Experience / Question / Short Praise / Insight

...（共8-10条）

**删除确认：**
- [x] 已删除纯 Filler（Ooh / Noted / Saving This）
- [x] 已检查无撞车
- [x] 已删除 maker 原话复述类
- [x] 已删除过于 meta 的分析

**发帖顺序建议：**
```
第1批（Personal Experience）：#X, #Y
第2批（Short Praise + Question）：#Z, #W, #V
第3批（Insight）：#U
```
```

**Filler 分布：** 5-6条（推荐区间内），混入均匀

**Insight 样例：**
> "The shift from reactive to proactive is a much harder design problem than most agent products acknowledge. Reactive agents fail silently. Proactive agents fail loudly, wrong actions on your behalf..."

**格式警告：**
- 本篇 #5 长度偏长，但内容质量高，可接受
- 避免连续3条以上无结尾评论

**优先级：** 1 > 3 > 4 > 6 > 11 > 9 > 8 > 2 > 7 > 12 > 10 > 5

**风险提示：**
- [5] 需注意：长句包含多个claims，但观点正向，高karma账号可用
- [7] 问免费层可能显得像在评估值不值，但可接受

**发帖顺序建议：**
```
第1批（安全Filler）：#1, #3, #4, #6, #11, #9
第2批（有观点）：#8, #2, #12
第3批（长/技术）：#7, #10, #5
```
```

---

## Firecrawl 抓取 PH（推荐 · 需环境变量）

**密钥：** 仅 `FIRECRAWL_API_KEY` 环境变量，禁止写入仓库。完整 SOP → `references/firecrawl-sop.md`  
**脚本：** `scripts/scrape-ph.ps1 -Slug autosubtitles -Source hunted`

**工作流（生成评论前必做）：**
1. 抓 `https://hunted.space/product/{slug}` → **Comment highlights** = 已有角度，防撞车  
2. 抓 `https://www.producthunt.com/products/{slug}`（`onlyMainContent: true`，`waitFor` 8000）→ launch 是否 **Launching today**、产品描述  
3. 将 highlights 写入草稿「已有评论」；避开已问的 TikTok UI / local audio / Descript 等  

**产品页成功标志：** markdown 含 `Login to comment`、launch 标题  
**hunted 成功标志：** 含 `Comment highlights`、`Upvotes`

**PowerShell 示例：**
```powershell
$env:FIRECRAWL_API_KEY = "fc-..."   # 勿提交 git
.\scripts\scrape-ph.ps1 -Slug mixpanel -Source both
```

**旧 v1 / onlyMainContent:false 全页：** 噪音大，已弃用；见 `references/firecrawl-sop.md`

---

## 真实评论数据分析总结

**分析了以下产品的真实评论：**
napkin, logseq, typly, coze, surfkey, buttondown, make, vercel, craftbot

**关键发现：**

1. **越具体的评论越真实：** 真实评论会提到产品的架构决策、设计选择、具体功能；AI 评论只会说"great tool"

2. **Personal context 不可伪造：** 真实用户会说"我有 X 个订阅者"、"我是 Y 的重度用户"、"我们在用 Z 做 X"；AI 评论没有个人情境

3. **结尾必须多样：** 真实评论的结尾各种各样；AI 评论结尾高度一致（Upvoted + emoji）

4. **Maker 回复是宝藏：** 分析 maker 的回复可以了解产品细节，也能学会怎么和用户互动

5. **Questions 永远安全：** 向 maker 提问是最安全的评论类型，因为它要求对话，而对话天然排斥水军

6. **Filler 看似无用实则关键：** 2-3 条纯情绪 Filler 能有效稀释有观点的评论，降低整体风险

7. **不要每次都 Upvoted：** 真实用户不是每条评论都 Upvoted（那样很累）；加几次就好
