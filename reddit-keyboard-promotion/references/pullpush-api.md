# PullPush 归档 API（帖子 / 评论上下文）

> **用途：** 拉取帖子已有评论、同 subreddit 相似讨论，用于模仿语气、避免重复角度、判断 thread 氛围。  
> **不用于：** 自动发帖、批量爬取、绕过 Reddit 速率限制做 spam。  
> **禁止用于：** 把归档搜索结果里的旧帖 ID 写入 `workspace/comments/*` 当「今日待发」—— 须用户浏览器可打开且 OP 仍可读。

**官方文档：** https://pullpush.io/  
**Base URL：** `https://api.pullpush.io`

## 已知限制（必读）

| 情况 | 建议 |
|------|------|
| **新帖 / 几小时内** | PullPush 常有 **数小时～1 天+ 延迟**，归档里可能没有最新评论 | 先用 **Reddit JSON**（见下） |
| **热帖评论很多** | Reddit 单页 JSON 会截断深层回复 | PullPush `link_id` 补全 + 多页 `size=100` |
| **归档截止日** | 第三方索引未必覆盖「此刻」全站 | 规格/价格仍走 `research-protocol.md` 搜索 |
| **删除帖** | 归档可能仍保留旧数据 | 以 OP 当前可见内容为准写回复 |
| **待发清单** | 索引延迟 + 旧帖仍显示 0 评论 | **不得**仅凭 PullPush 生成主推；无 Reddit JSON 时要求用户贴 **OP 原文** 或跳过 |
| **2025 及更早 ID** | 常已 archived | 默认 **不写入** workspace 待发 |

## 从链接解析参数

Reddit 帖子 URL 形态：

```text
https://www.reddit.com/r/{subreddit}/comments/{post_id}/{slug}/
```

提取：

- `subreddit` → `MechanicalKeyboards`（**不要**带 `r/`）
- `post_id` → `1s1wm39`
- `link_id` → `t3_{post_id}` → `t3_1s1wm39`

评论直链（若用户给的是 comment URL）：

```text
.../comments/{post_id}/.../{comment_id}/
```

- `comment_id` → PullPush `ids` 参数（base36，如 `lq3abc`）

## 端点速查

| 端点 | 作用 |
|------|------|
| `GET /reddit/search/comment/` | 搜评论（按帖、sub、关键词、作者等） |
| `GET /reddit/search/submission/` | 搜帖子（标题/正文、sub、分数等） |

返回 JSON：`data` 为结果数组，`metadata` 含 `total_results`、`execution_time_milliseconds` 等。

### 评论搜索常用参数

| 参数 | 说明 | 示例 |
|------|------|------|
| `link_id` | 限定某一帖下的评论 | `t3_1s1wm39` |
| `subreddit` | 限定 sub（与 `link_id` 联用更稳） | `MechanicalKeyboards` |
| `q` | 正文关键词（不区分大小写） | `"hall effect"` |
| `ids` | 按评论 id 批量取 | `c0nn9iq,c0nn5ux` |
| `author` | 某用户历史评论 | `username` |
| `size` | 条数，默认 100，**最大 100** | `100` |
| `sort` | `asc` / `desc` | `desc` |
| `sort_type` | `created_utc` / `score` / `num_comments` | `score` |
| `after` / `before` | epoch 或 `7d`、`30d` 等 | `after=7d` |

### 帖子搜索常用参数

除与评论类似的 `q`、`subreddit`、`author`、`size`、`sort` 外：

- `title` / `selftext` — 只搜标题或正文
- `score` — 如 `score=>50`
- `num_comments` — 如 `num_comments=>20`

## 推荐调用顺序（生成评论前）

对每个用户链接执行：

### 1. 新帖 / 需要当前 top 评论 → Reddit JSON（优先）

```text
https://www.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=200&sort=confidence
```

或：

```text
https://old.reddit.com/r/{subreddit}/comments/{post_id}.json?limit=200
```

从 `[0].data.children[0].data` 取：`title`、`selftext`、`link_flair_text`、`score`、`num_comments`。  
从 `[1].data.children` 遍历顶层评论：`body`、`score`、`author`、`created_utc`。

**用途：** OP 原文、当前高赞回复、是否已有「正确答案」、是否适合 Filler-only。

### 2. 同帖全量 / 高分评论语气 → PullPush

**按帖子拉评论（已测可用）：**

```text
https://api.pullpush.io/reddit/search/comment?link_id=t3_{post_id}&subreddit={subreddit}&size=100&sort=desc&sort_type=score
```

需要更多条时：用 `sort_type=created_utc` + `before`/`after` 分页，或换 `sort_type=score` 再取一批（注意去重 id）。

**只取帖子元数据：**

```text
https://api.pullpush.io/reddit/search/submission?ids=t3_{post_id}
```

### 3. 扩展语境（可选）→ PullPush 关键词 + sub

当型号陌生或需社区口径：

```text
https://api.pullpush.io/reddit/search/comment?q="Keychron Q1"&subreddit=MechanicalKeyboards&size=50&sort=desc&sort_type=score
https://api.pullpush.io/reddit/search/submission?q="Keychron Q1"&subreddit=keyboards&size=25&sort=desc&sort_type=score
```

仍不够再按 `research-protocol.md` 做 web 搜索。

## 从 API 结果提取什么

写入「帖子背景」和选题时，只记对写评论有用的字段：

| 字段 | 用途 |
|------|------|
| `body`（OP / 高赞评） | 实体、预算、情绪、是否已解决 |
| `score` | 社区倾向；避免与 top 评论完全重复 |
| 重复主题 | 若已有 3+ 人推荐同一板子，换角度或 Me-too |
| 语气 | 短句 / 梗 / 技术深度 → 匹配 `comment-style-guide.md` |
| `subreddit` | Filler 比例、是否硬核（见 SKILL 表） |

**不要**把 API 返回的长评论抄进草稿；只吸收结构与用词密度。

## Shell / 工具示例

```bash
# 单帖高分评论（归档）
curl -s "https://api.pullpush.io/reddit/search/comment?link_id=t3_1s1wm39&subreddit=MechanicalKeyboards&size=50&sort=desc&sort_type=score"

# 新帖实时（浏览器或 curl 需 User-Agent，部分环境会 403）
curl -s -A "research-bot/1.0" "https://www.reddit.com/r/MechanicalKeyboards/comments/1s1wm39.json?limit=100"
```

PowerShell：

```powershell
Invoke-RestMethod "https://api.pullpush.io/reddit/search/comment?link_id=t3_1s1wm39&subreddit=MechanicalKeyboards&size=20&sort=desc&sort_type=score"
```

若 Reddit JSON 返回 403/429：改用 PullPush + 用户粘贴的 OP/评论截图；在输出「风险提示」注明上下文可能不完整。

## 与评论草稿流程的衔接

1. 解析链接 → `subreddit`、`post_id`、`link_id`
2. **Reddit JSON**（新）或 **PullPush**（旧帖 / JSON 失败）→ 填 **帖子背景**
3. 标出已被 top 评论覆盖的点 → 生成的 10–12 条里 **避开复读**
4. 事实性 claims（型号、轴体、价格）仍遵守 `research-protocol.md`，API 不能替代验证
