# Product Hunt 评论质量分析报告
*基于 Firecrawl 抓取的 Product Hunt 官方讨论页面真实评论*

## 真实评论样本（2026-05-12 抓取）

### 样本1：Mariyan D.（CoThou 产品发布帖）

```
A few months ago, while I was working on another project, I found myself 
incredibly frustrated by wasting valuable time switching between platforms, 
managing multiple subscriptions, and working with fragmented data. I called 
this the Three-Fold Problem.

After discussing this with over 200 professionals from my personal network, 
it became clear that this was a significant problem that almost everyone 
I talked to was experiencing.

[此处列出具体SaaS工具：Superhuman, Slack, Notion, Dropbox, Zoom...]

For 20 people, this adds up to **$80,000+/year**...

That's why I built **Aiobis** – All-In-One Business Interaction Suite.

Your personal, super-intelligent AI assistant.
Upvote (2)
```

### 样本2：Nika 给 Mariyan 的格式反馈（官方建议）

```
[@martyd] Hey Mariyan :) I like how you narrate a story. Personally, 
I would create a short intro (5 lines at maximum) where you outline your 
motive for why the tool was created.

Then you could outline:
– What is the problem
– Who is it for
– Helpful Features (what it can do)
– Results/benefits from the tool

Do not be afraid to work with Bullet lists to make the text more 
readable and highlight some parts – Product Hunt gave us formatting tools, 
so feel free to use them to make comments more digestible. :)
```

### 样本3：Rahul 的排版批评

```
i dont feel its easy to read through big paragraphs. i feel it could 
be modified to make it straight forward, easy to read, and minimal

you could use AI for the better.

i pasted your comment in chat gpt and asked it to modify...
```

---

## 关键发现

### 1. PH 官方认可的评论结构（来自 Nika）
- 开头：动机/为什么做（5行以内）
- Body：问题 → 目标用户 → 功能 → 效果
- 格式：善用 bullet points 和 **bold**
- 长度：越短越容易读

### 2. 排版 > 文采
- 大段落 = 没人看
- bullet list + bold = 专业感
- PH 有原生格式工具（bold、bullet、quote）

### 3. 真实用户的语气特征
- 不用正式书面语
- 可以说 "I like" / "I feel" / "I'd"
- 批评要带解决方案
- 求 upvote 不丢人，但不要每条都求

### 4. 评论类型分布（观察）
- Filler：3-5词纯情绪 + 表情（"ooh this one"）
- Insight：观察性评论 + 具体理由（"这个方向有意思，因为..."）
- Question：问 maker 一个具体问题
- Feedback：带建设性意见的批评

### 5. 产品页 vs 论坛页
- 产品页（`/posts/xxx`）：评论需要 JS 渲染，Firecrawl 抓不到
- 论坛页（`/p/xxx`）：有真实评论内容，可以抓取分析

---

## 格式工具使用示例（来自真实评论）

```markdown
**$80,000+/year**  （金额 bold）

– Superhuman (email)  （bullet list）
– Slack (comms)

> Not just another tool — the **stack itself**.  （quote + bold）
```

---

## Firecrawl v1 API 正确用法

```bash
FIRECRAWL_KEY="fc-xxx"
curl -s "https://api.firecrawl.dev/v1/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.producthunt.com/posts/产品名"}'
```

注意：
- v0 已废弃
- v2 返回格式不同（`urls` 数组 + `pageOptions`），不兼容
- 产品页通常返回 `markdown: ""`（JS 渲染）
- 论坛页（`/p/xxx`）有真实内容
