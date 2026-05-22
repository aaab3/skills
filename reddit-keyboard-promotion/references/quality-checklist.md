# Quality Checklist

Run this **after** `SKILL.md` § Evidence Gate passes. If Gate #3 is empty, **do not run tone checks on a draft** — output 不建议发 only.

## Evidence Gate（与 SKILL.md 一致 · 先发后检）

- [ ] **OP facts** listed in one sentence before any English draft
- [ ] **Existing comments** listed (or marked incomplete if thread not fully read)
- [ ] **Safe claim I can add** is exactly **one** local move tied to this thread
- [ ] If #3 is weak, repeated, or unverified → **stop** (不建议发; no 建议实发)
- [ ] Draft uses only: OP facts · visible comments · verified vendor specs · uncertain diagnostics (worded as guess)
- [ ] **Local Comment test:** comment would **not** still work on 20 similar threads unchanged

## The 5 Rules (Non-Negotiable)

1. **One contribution type**: Tradeoff OR Diagnostic OR Specific Observation. Not two. Not a summary of everything.
2. **One concrete detail from OP**: model, switch, budget, symptom, layout, use case — at least one.
3. **One judgment + one reason**: say what you think and why, not just "it depends".
4. **Zero or one question**: never more than one.
5. **No invented facts**: anything uncertain must be marked or caveated (see § Claim Wording).

## Claim Wording（每条事实标类型）

| Type | Rule | Example |
|------|------|---------|
| **OP fact** | State plainly from OP | `Since the whole row is dead…` |
| **Verified spec** | Only after search/official page | `That line is wired-only.` |
| **Unverified spec** | **Do not include** in 建议实发 | — |
| **Diagnosis** | Never as fact | `Sounds like…` / `Usually points to…` / `I'd check…` |
| **Community opinion** | Only if recently verified; no `everyone says` / `widely regarded` / `best` | `Some people prefer X for Y, but it depends on…` |
| **Personal experience** | **Only if true**; never for tone | No fake `I had mine for 3 weeks` |

- [ ] Every factual sentence in 建议实发 maps to one row above
- [ ] No unverified SKU specs (Type D → § Type D Product Facts)

## AI Voice Detection (Run only if Gate passed)

Check your draft for these triggers:

- [ ] **Banned phrases**: Does the comment contain "the real unlock", "the actual killer feature", "the real moat", "the right differentiator", "genuinely", "at scale", "workflow" (noun), "adoption flywheel", "context freshness", "the finer details", "edge over", "excels at", "it's all about", "the sweet spot"?
  - If yes: rewrite without them
- [ ] **Too many architectural questions**: Does every draft end with a smart technical question? Mix in simple user questions.
- [ ] **Same structure every time**: opening认可 → 指出价值 → 抛问题 → (Upvoted 👍). Shake it up.
- [ ] **Upvoted pattern**: On Product Hunt, is every comment ending with "Upvoted 👍"? Reduce to 20-30%.
- [ ] **Length**: Match post type (see `reddit-platform-guide.md` §6.3). Build/showcase: ~5–25 words; ELI5/help may be longer but still one main point.
- [ ] **Solution tone**: Does the fix sound like "pretty sure you can..." not "you should navigate to..."?

## Thread Competition (Reddit — Run for Help/Buy posts)

- [ ] Did you list what **OP asked** in one sentence before drafting?
- [ ] Did you read **top comments** and note what is already covered?
- [ ] If a top comment already gives a long model+price list, is your draft **one new angle** (not a shorter copy)?
- [ ] For **&lt;50 karma**, is the draft **≤40 words** and avoiding buildapc/peripheral megathread pile-ons?

## Symbols & quotes (`reddit-comment-symbols.md`)

- [ ] Short comment (NSQ/Casual/Ask): **default no `"`** unless quoting OP's word or one scare-quote term
- [ ] No Smart Quotes `“”` — use straight `"` if needed
- [ ] No accidental Markdown: line-start `-` / `1.` lists, stray `^` superscript, `**bold**` blocks in NSQ short answers
- [ ] Not stacking multiple scare quotes like `"best"` + `"worth it"` unless keyboard Help tone fits the thread

## NSQ Voice (r/NoStupidQuestions only)

- [ ] **≤35 words, ≤2 sentences** unless thread top comments are all long essays
- [ ] **No sandwich**: answer + mechanism + caveat as three balanced paragraphs
- [ ] **No explainer voice:** no `Partly X… Partly Y…`; no `Your [feeling] is common/valid`; no `legit coping strategies` (see `comment-style-guide.md` § Explainer)
- [ ] Banned openers: `You're not imagining it`, `Great question`, `Hope this helps`, `It's important to note`, `Partly`, `Partially`
- [ ] **No fake casual openers:** do not start every comment with `Yeah` / `Honestly` / `tbh` for tone
- [ ] `yeah` / `honestly` / `tbh` only if the sentence still works **without** them (`comment-style-guide.md`)
- [ ] **No fake personal anchor:** do not invent `I still use…` / ownership for flavor; real experience only if true
- [ ] Prefer concrete detail over abstract nouns (engagement, accessibility, corporate)
- [ ] Fewer em dashes `—`; use periods or `and`
- [ ] Shorter than the longest existing top comment in that thread
- [ ] Read aloud: sounds like a **person typing**, not a **balanced essay**?
- [ ] Should this thread be marked **skip** (archived, locked, HE war, wrong facts risk)?

## Context Fit

- [ ] Did the comment answer the actual post?
- [ ] Did it use at least one concrete detail from OP?
- [ ] Is the reply angle appropriate for the post type?
- [ ] Would the comment still make sense if the OP never replies?
- [ ] Does it read like a Reddit reply, not a support ticket?

## Fact Safety

- [ ] Were unfamiliar models, switches, specs, prices, and community claims searched?
- [ ] Are uncertain facts marked per § Claim Wording (diagnosis vs verified spec)?
- [ ] Did the comment avoid inventing specs, ownership, or personal experience?
- [ ] Did the comment avoid overclaiming "best", "worst", or "everyone agrees"?

## Named Product Gate（具名品牌+型号时 · SKILL.md）

- [ ] **Connection** verified for each named SKU
- [ ] **Layout / switch / software** verified if relevant to OP's question
- [ ] Matches **OP 合同** (wireless / HE / aesthetic vs gaming axis)
- [ ] If any required field unknown → **that SKU removed** from 建议实发 (lane + `check SKU` OK)

## Type D Product Facts（推荐帖 — 具名型号时必跑）

> 流程：`product-recommendation-playbook.md` §0–§4。与 NSQ 语气检查 **并行**，不互相替代。

- [ ] **OP 合同** 已写一句：参照物（Mode/无）+ 硬约束（wireless/预算）+ 主诉求（审美/游戏/办公）
- [ ] **产品轴** 正确：Mode + wireless → **非** 默认 Q HE / Lemokey HE / NuPhy **Air HE** 无线
- [ ] 评论里 **每个具名 SKU**：官网/搜索核对 **Connection**（wired only / 2.4G+BT / tri-mode）→ 与 OP「要无线」一致？
- [ ] **NuPhy：** Air **HE** 线未当作无线推荐；无线只说 **Air/Halo V2/V3** 等核实过的款
- [ ] **Keychron：** Q **HE** 未当作 Mode 审美无线替代；无线 Mode-like 优先 **Q Max / Q Ultra**（或核实过的 V Ultra）
- [ ] 无 `wireless-ish` / `premium-ish` / `gaming-ish` 与 **具名型号** 同句
- [ ] ≤ **2 条 lane** + ≤ **1 个踩坑**；非 3+ SKU 清单
- [ ] MK 日帖：是 **Reply 嵌套问** 而非顶层另开？
- [ ] 楼里仅有 vendor list 时：补 shortlist/踩坑，**未** 重复「去 alexotos」同义句

## Reddit Tone

- [ ] Is it short enough? **Under 30 words.** If >30, it's too long.
- [ ] Lowercase is fine — don't force capitalization
- [ ] Half-sentences are okay — don't complete every thought
- [ ] Is there no more than one question?
- [ ] Does it avoid generic AI phrases: "Out of curiosity", "I hope this helps", "Great choice", "Hope this works for you"?
- [ ] Does it avoid cheerleading and forced engagement questions?
- [ ] Does it avoid the pattern: restate OP → overpraise → generic lesson → forced question?
- [ ] Does it sound like a person, not a template?
- [ ] **Polished comparison language?** ("ecosystem", "mature", "price-to-performance") — rewrite if used
- [ ] **Under 30 words?**
- [ ] **One casual opinion, no summary?**

## Contribution Type Check

Choose one:

- [ ] **Tradeoff**: "This is good for X, but if you care about Y, watch out for Z."
- [ ] **Diagnostic**: "This sounds like A. Check B first. If it's C, then do D."
- [ ] **Specific Observation**: Commenting on one specific detail of the build/post and why it works or might have a gotcha.

## Anti-AI Rewrite Triggers

Rewrite immediately if:

- [ ] The comment uses 2+ banned phrases from the ban list
- [ ] **`Partly` / `Partially` opens two parallel causes** (explainer taxonomy)
- [ ] **`Your X is common` / `Many people feel`** without a personal line
- [ ] **Three balanced clauses** (reason + motive + reassurance) in one comment
- [ ] Every draft follows the same structure (认可 → 价值 → 问题)
- [ ] It asks a "smart architectural" question when a simple user question would fit better
- [ ] It's >6 sentences for a casual Reddit post
- [ ] All Product Hunt comments end with "Upvoted 👍"
- [ ] It feels like a product launch analysis, not a human comment
- [ ] **Show, don't conclude**: Does the comment just say something is "great/solid/amazing", or does it prove it with specific evidence? Every positive claim needs a specific proof.
- [ ] **Ban phrase alert**: "says a lot about the board", "the finer details", "mature ecosystem" — these read like AI summaries. Rewrite.

## What Good Keyboard Comments Have

- They answer the actual post, not the general topic.
- They name one concrete thing: model, switch feel, budget, layout, symptom, or use case.
- They give one useful angle, not every possible angle.
- They include a caveat when the answer depends on the OP's needs.
- They do not invent personal ownership.
- They ask zero or one question — and sometimes that question is very ordinary.
- They occasionally sound like they belong to a slightly imperfect person, not a product analyst.

## Human Imperfection Markers

The comment should occasionally feel like a real person who is:
- willing to say "I could be wrong here"
- asking something they personally wonder, not demonstrating expertise
- NOT optimizing every sentence for maximum insight
- occasionally just reacting with a short, casual opinion

## 发帖（跨社区）

路由与原型 → `reddit-community-atlas.md` §0–§3。专册：AskReddit · NSQ · TIL · LPT 等见 atlas §2。

### 通用（所有发帖）

- [ ] 读过 **目标 sub 当前 rules**（链接见 atlas §14）
- [ ] Sub 内验重（`reddit-search-sop.md`）；撞 atlas §11 饱和 → 改角度或勿发
- [ ] 账号阶段匹配：&lt;50 karma 是否仍建议 **只评论**
- [ ] 美东 7:00–16:00（泛版）；首 30 分钟可在线
- [ ] 不删帖立刻同义重发；不 vote manipulation

### r/AskReddit（仅 title 帖）

完整流程 → `askreddit-post-playbook.md`。发前必跑：

- [ ] 标题英文、问号；**正文空白**；补充仅 **OP 首评**
- [ ] 在 r/AskReddit 搜 **4–6 关键词**；近 1–3 月同构热帖 → 改角度或勿发
- [ ] 未撞 §5 饱和（含 *stopped buying 2026*、省钱变亏子集、神帖公式）
- [ ] 非 *you've seen someone* 纯见证；优先 **第一人称** 或 **How would you feel**
- [ ] §7 结构打分 **≥24/32**（用户要发时 Agent 须填表）
- [ ] 50–200 字符；3 秒 lurker hook（可站队/笑/怒，非「又是 XX 翻车」）
- [ ] 美东 7:00–16:00；发后 30 分钟在线；**勿**删帖立刻重发
- [ ] flop 诊断走 playbook §9–§10，不怂恿同义重发
