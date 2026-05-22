# 2026-05-21 Product Hunt 评论草稿（5 产品 × 10 条 · v2）

> 产品：AutoSubtitles · CatchAll · Framed Mockup Studio · Attention Insight · Mixpanel  
> **v2 改动：** 按实发反馈降「写作感」、每条尽量 **只问一个问题**、弱化批量身份标签  
> **实发：每产品只发 1 条**（见文末「定稿实发」）；发前扫评论区避免撞车  
> **说明：** 2026-05-21 Firecrawl 已测 `autosubtitles`（hunted.space 有 9 条 highlights）；发前仍建议再抓一次。SOP：`references/firecrawl-sop.md`

---

## 写作原则（v2 · 比 v1 更重要）

| 要做 | 避免 |
|------|------|
| 一个真实痛点/观察 + **一个** 明确问题 | 一条里堆 2–3 个问题 |
| 像刷 PH 时随手打的两句 | 完整段落、顾问腔、每条都带身份标签 |
| 首发：maker 好答的产品/定位问题 | 首发：Whisper benchmark、accuracy 防御型追问 |
| Mixpanel：「在评估 / 对比 PostHog」 | 装老用户、销售话术、没看清产品就夸 heatmaps |
| 确认当天 launch 再写 Congrats | `Congrats if today's the day` |
| 技术深问放 **第 2 条**（隔几天） | 首评就上专业 benchmark |

**身份标签：** 偶尔可用（small app、short clips），不要五个产品全是 indie podcaster / freelancer / one-person biz。

---

## 定稿实发（复制粘贴 · 每产品 1 条）

| 产品 | 英文（实发） | 中文 |
|------|-------------|------|
| **AutoSubtitles** | The local video processing part is the main thing that would make me try this for client clips. Does only the audio get uploaded for transcription? | 本地处理视频是我会试的原因；转写时是不是只上传音频？ |
| **CatchAll** | Missed calls are a real problem for small service businesses. When the AI is unsure, does it warm-transfer to a human or just take a message? | 小企业漏接电话确实是痛点；AI 不确定时会暖转人工还是只留言？ |
| **Framed Mockup Studio** | Updating App Store screenshots every release is one of those chores I keep avoiding. Can this export all required iPhone sizes in one batch? | 每次发版更新商店截图是我一直拖的事；能一次批量导出全部 iPhone 尺寸吗？ |
| **Attention Insight** | I'd use this before shipping a landing page, especially when the team is arguing over CTA placement. Can it compare two Figma variants side by side? | 上线前会用，尤其团队争 CTA 放哪时；能并排对比两个 Figma 稿吗？ |
| **Mixpanel** | we still export csvs for the weekly metrics review. does headless replace that or is it mostly for folks who live in python daily? | 周会还在导 csv；Headless 能替代还是只适合天天写 Python 的人？ |

**实发顺序（maker 回复概率 + 自然度）：** CatchAll → Framed → AutoSubtitles → **Mixpanel（先 Firecrawl 确认当天 launch 主题）** → Attention Insight

**Mixpanel 注意（2026-05-21 Firecrawl）：** `/products/mixpanel` 当天是 **Mixpanel Headless**，不是 Events 2.0；勿发 PostHog / 1M free / funnel→replay

**节奏：** 单日最多 2 个产品 · 间隔 2h+

---

## 一、AutoSubtitles

**链接：** https://www.producthunt.com/products/autosubtitles · https://autosubtitles.com/

**发前搜：** local processing、audio upload、CapCut、watermark、SRT

**Firecrawl 已有评论（2026-05-21 · 勿撞车）：** animated captions 省时、**TikTok bottom UI**（勿发）、vs **Descript**、**FFmpeg.wasm 导出**、local audio only（定稿「只传音频」仍可发但别复述 maker FAQ 原话）

---

**评论草稿（10 条）：**

1. **【定稿实发】** The local video processing part is the main thing that would make me try this for client clips. Does only the audio get uploaded for transcription? | 本地处理是我会试的原因；转写是否只传音频 | 🟢 首发

2. **【备选实发】** Been using CapCut captions for short clips. Does AutoSubtitles support word-by-word highlights, or is it mainly static burned-in captions? | 短 clip 一直用 CapCut；有逐词高亮还是 mainly 静态烧录 | 🟢 首发

3. No signup on first export is nice. Is Pro basically just removing the watermark? | 不注册就能导出挺好；Pro 是不是 mainly 去水印 | 🟢

4. Ten minute limit on free is fine for what I do. Can you export SRT without burning captions into the video? | 免费 10 分钟对我够用；能导出 SRT 且不烧录进视频吗 | 🟡 第 2 条

5. Wrong language auto-detect happens to me a lot. Can you fix the language without re-uploading the whole file? | 自动识别语言常错；能否不改传整文件 | 🟡

6. If I upgrade after editing, can I re-export the same subtitles without running transcription again? | 编辑完再升级能否同份字幕重导出 | 🟢 第 2 条

7. ~~Indie podcaster here — …~~（v1 删：身份标签过重）→ 见 #4

8. Accents and multiple speakers is where cheap tools fail for me. Did you benchmark against Whisper locally or a hosted model? | 口音+多人说话廉价工具常挂；对标本地 Whisper 还是托管 | 🟡 **勿首发** · 技术深

9. Portrait captions — do any presets keep text above the TikTok bottom UI, or is it manual every time? | 竖屏字幕预设会避开 TikTok 底部 UI 吗 | 🟡 第 2 条

10. Solid when you already have the final cut and just need captions fast. | 已有成片只想快速加字幕时够用 | 🟢 仅观察无问题 · 备选无问版

**v1→v2：** #1 去掉 `what I'd actually trust`；#6 Whisper 降为非首发；删堆叠问句

---

## 二、CatchAll

**链接：** https://www.producthunt.com/products/catchall · http://catchall.polsia.app/

**发前搜：** warm transfer、follow-up frequency、Spanish、form leads

---

**评论草稿（10 条）：**

1. **【定稿实发】** Missed calls are a real problem for small service businesses. When the AI is unsure, does it warm-transfer to a human or just take a message? | 小企业漏接是痛点；不确定时暖转人工还是留言 | 🟢 首发

2. **【备选实发】** Follow-up until someone books or clearly says no is the part I'd care about most. Can you control how often it follows up? | 跟进到预约或明确拒绝最重要；跟进频率能控吗 | 🟢 首发

3. ~~I run a one-person service biz…~~（v1 删：非真实身份勿装）→ 见 #1 泛化痛点

4. Quote emails at night — does it read the full thread or each email on its own? | 半夜报价邮件会读完整线程吗 | 🟡 第 2 条

5. Phone support in Spanish for US shops, or English only for now? | 电话是否支持西语还是暂仅英语 | 🟢 第 2 条

6. Daily briefing — email or just inside the dashboard? | 每日简报是邮件还是只在后台 | 🟢 第 2 条

7. Can you trial it on a call-forwarding number before putting it on the main line? | 能否先用呼叫转移试再绑主线 | 🟡

8. ~~feels more like ops than reception~~（v1 删：抽象 · 勿首发）

9. Caller wants a manager — does it ring your phone or stay in the AI loop? | 要经理时会打你手机还是 AI 继续接 | 🟡 第 2 条

10. Web form leads — do those feed the same follow-up queue as phone and email? | 网页表单线索能和电话邮件同一跟进队列吗 | 🟡 第 2 条

**v1→v2：** #1+#2 合并为定稿；删 one-person biz；#3 加 follow-up 频率一问

---

## 三、Framed Mockup Studio

**链接：** https://www.producthunt.com/products/framed-mockup-studio

**发前搜：** iPhone sizes batch、Xcode simulator、Mockuuups

**注意：** 产品细节少 · 只问已确认品类常见能力 · 勿写未验证功能

---

**评论草稿（10 条）：**

1. **【定稿实发】** Updating App Store screenshots every release is one of those chores I keep avoiding. Can this export all required iPhone sizes in one batch? | 发版更新截图一直拖；能一次批量导出全部 iPhone 尺寸吗 | 🟢 首发

2. **【备选实发】** Does it pull screenshots directly from Xcode Simulator, or do you upload PNGs manually? | 直接从模拟器拉还是手动传 PNG | 🟢 首发

3. Been on Mockuuups for a while. What's actually different here? | 用 Mockuuups 久了；这里实际差在哪 | 🟡 第 2 条 · 一问

4. ~~Indie dev with no designer…~~（v1 删）→ 换 locale：Can you swap headline text per locale without redoing the whole layout? | 换语言只改标题要不要重做整张 | 🟡

5. Android Play sizes in the same batch export? | 同一批导出含 Google Play 尺寸吗 | 🟡 第 2 条

6. ~~Congrats on the launch if today's the day~~（**禁用**）

7. Scroll-style App Store previews, or single-screen frames only? | 支持横向滚动预览还是仅单屏 | 🟡

8. Dark mode — separate template or one design with a light/dark toggle? | 深色模式单独模板还是一套切换 | 🟡 第 2 条

9. Export ZIP only, or any direct upload to App Store Connect? | 只导出 ZIP 还是能直连 ASC | 🟡

10. Clay frames vs photo-real devices — which do you use more for App Store shots? | 粘土框 vs 真机框商店图更常用哪种 | 🟡 第 2 条

**v1→v2：** 删 #7 Congrats；定稿用 `one of those chores I keep avoiding`

---

## 四、Attention Insight

**链接：** https://www.producthunt.com/products/attention-insight

**发前搜：** Figma compare、Hotjar、side by side、CTA

**注意：** 少代理/顾问味 · 首发勿逼 maker 证 accuracy

---

**评论草稿（10 条）：**

1. **【定稿实发】** I'd use this before shipping a landing page, especially when the team is arguing over CTA placement. Can it compare two Figma variants side by side? | 上线前用，争 CTA 时；能并排对比两个 Figma 稿吗 | 🟢 首发

2. **【备选实发】** We already use Hotjar after launch. Is Attention Insight mainly for pre-launch mockups, or do people also use it on live pages? | 上线后用 Hotjar；主要做上线前稿还是也用于线上 | 🟢 首发

3. ~~Running a Figma review without waiting…~~（v1 略完整）→ 已定稿 #1

4. How close are predictions to real eye-tracking studies you've run? | 预测和真实眼动研究差多少 | 🟡 **勿首发** · 易触发防御

5. ~~freelancer with ~8 client projects~~（v1 删）→ Per seat or per export for occasional client work? | 偶尔做客户项目按席位还是按导出 | 🟡 第 2 条

6. Clarity vs Focus score — which do you show when two hero layouts compete? | 两个 hero 争时用 Clarity 还是 Focus | 🟡 第 2 条

7. Figma plugin — does analysis work on mobile-sized frames too? | 分析支持手机尺寸画板吗 | 🟡

8. AI tips on the heatmap — suggestions you edit, or does it change the layout? | AI 提示可编辑还是自动改版式 | 🟡 第 2 条

9. ~~smallest canvas that still gives reliable results~~（v1 删：过专业 · 勿首发）

10. Paste a live URL or PNG export only? | 能贴 live URL 还是只能 PNG | 🟡 第 2 条

**v1→v2：** 定稿加 Figma 并排一问；#2 accuracy 降为第 2 批

---

## 五、Mixpanel

**链接（今天评论发这里）：** https://www.producthunt.com/products/mixpanel  
**当天 launch（Firecrawl 2026-05-21）：** **Mixpanel Headless** — Python SDK，plain language → code，「durable code」  
**抓取：** `workspace/scrapes/mixpanel-hunted.md` · `mixpanel-ph.md`

**已有评论（Headless · 勿撞车）：**
- 「durable code」 framing、每周可重跑脚本
- 早上 10 分钟例行：decode errors + activation funnel + watchlist
- **Python SDK vs MCP server**（已问，勿重复）
- maker 长评：gap between question and dashboard（勿复述）

**发前搜：** headless、MCP、python SDK、durable code

**v1 稿为何模板味重（你贴的 #1–#10）：**
- 问的是 **Events 2.0 / PostHog / replay**，但产品页今天是 **Headless** → 像没打开页面
- 句式：`what caught my attention` + `deciding between` + `where strongest` = 选型博客三连
- 真人帖（Events 旧帖）是：`@abraibrai` + **自己具体数字**（1.5m events、5 saved reports、10 chart limit）

---

### A. Mixpanel Headless — 今天 `/products/mixpanel`（10 条 · 用这个）

1. **【定稿实发】** we still export csvs for the weekly metrics review. does headless replace that or is it mostly for folks who live in python daily? | 周会还在导 csv；Headless 能替代还是只适合天天写 Python | 🟢

2. **【备选实发】** monday retention question gets rebuilt in a spreadsheet every week. once headless generates the query, can you save it and rerun it? | 每周留存问题都在表格里重做；生成代码后能保存再跑吗 | 🟢

3. @tiffany_chen6 does the free tier project work with headless or do you need growth? | 免费档项目能用 Headless 吗 | 🟢 · 真人常 @maker

4. plain language → code is cool. what stops the agent from writing a query that scans way too much data? | 自然语言生成代码很酷；怎么防止查询扫太多数据 | 🟡 第 2 条

5. our pm will still live in the ui — headless is eng-only or they can use it too? | PM 还用 UI 吗还是只有工程 | 🟡

6. ~~The first 1M events free… PostHog…~~（**错 launch · 禁用**）

7. ~~Session replay funnel drop-off~~（**错 launch · 禁用**）

8. not on mixpanel yet but the “durable code” line makes sense. is there a read-only token setup for agents? | 还没用 MP；durable code 说得通；agent 有只读 token 吗 | 🟡

9. tried the docs — runs local only or needs mixpanel cloud for every query? | 看了文档；纯本地跑还是每次都要连云端 | 🟡

10. nice. been wanting to script funnels without clicking through the ui for ages | 早就想不点 UI 跑漏斗了（短、无问号 · 备选） | 🟢 极短

**Headless 勿首发：** MCP（楼里已有）· 长段 morning routine 仿写（已有 Indie iOS founder 帖）

---

### B. Events 2.0 旧帖 — 仅评论 `p/mixpanel` 定价串时用（10 条 · 非今天产品页）

> https://www.producthunt.com/p/mixpanel/mixpanel-events-2-0 · 1yr ago · 真人风格：短、@abraibrai、带自己数字

1. @abraibrai we're on a small plan and only get 5 saved reports — does "make the switch" unlock unlimited? | 小计划只有 5 个报告；切换 growth 能无限吗 | 🟢

2. @abraibrai ~800k events a month — still $0 on growth or do you hit a wall before 1m? | 每月约 80 万事件 growth 还免费吗 | 🟢

3. @abraibrai existing account — is migration literally just the pricing page button or do eng need to change sdk? | 老账号迁移只点定价页还是要改 SDK | 🟡

4. long time user, happy about pricing. does free tier still cap charts at 10? | 老用户；免费档还限 10 个图吗 | 🟡 · 仿 Jun Shen 但不照抄

5. Great for discovery... i have 1.5m events, growth shows $0 but i pay $140? what am i missing | 有 1.5m 事件账单看不懂（仿 David 具体算账风） | 🟡 · 仅你真在用 MP 时发

6. ~~deciding between Mixpanel and PostHog where strongest~~（模板 · 禁用）

7. ~~Analytics plus replay stitching vendors~~（禁用）

8. autocapture included on growth — can you turn it off if we already track events manually? | growth 含 autocapture 能关吗我们已手埋点 | 🟡

9. 20k session replays on growth — is that enough for a b2b saas with low traffic? | 2 万条 replay 对低流量 B2B 够吗 | 🟡

10. thanks for simplifying pricing. congrats | 谢简化定价（短恭喜 · 可选） | 🟢 极短

**B 区 v1 定稿 #1 #2：** 只适合旧帖，**不要**贴在今天 Headless launch 下

---

## v1 复盘（结合你的 8/10 反馈）

| 维度 | v1 问题 | v2 改法 |
|------|---------|---------|
| 语气 | 句子太完整、像润色过 | 更短、更口语；`would make me try` 替代 `trust for client work` |
| 身份 | 每产品一个精致 persona | 多数用泛场景；仅保留 small app / short clips 等轻标签 |
| 问题数 | 一条多问 | 定稿一律 **观察 + 一问** |
| 首发深度 | Whisper、accuracy、smallest canvas | 标「勿首发」进池子第 2 条 |
| Launch | `if today's the day` | 禁用；确认 launch 日再单独写 Congrats |
| Mixpanel | heatmaps 可能不准 | 改 replay + roadmap；强调 evaluating vs PostHog |
| 实发顺序 | AutoSubtitles 优先 | 改为 Mixpanel → CatchAll → Framed → AutoSubtitles → Attention Insight |

**评分：** v1 稿约 **8/10**（结构、原则、可接话度已优于普通 PH 评论）；v2 目标 **9/10** 靠「少写作、单问、定稿表可直接粘贴」。

---

## 实发记录

| 日期 | 产品 | 链接 | 正文摘要 | 可见？ | Maker 回复？ |
|------|------|------|----------|--------|--------------|
| | | | | | |
