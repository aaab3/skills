# Firecrawl 抓取 SOP（Product Hunt 评论调研）

> **密钥：** 只放环境变量 `FIRECRAWL_API_KEY`，**禁止**写进 SKILL、脚本默认值或 git。  
> 密钥若曾在聊天里暴露，请到 [firecrawl.dev](https://www.firecrawl.dev) 轮换。  
> **MCP：** 见 `web-research-mcp` 技能 + `%USERPROFILE%\.cursor\FIRECRAWL-MCP-SETUP.md`。无 MCP 时用下方 PowerShell。

---

## 能增强什么

| 之前 | 用 Firecrawl 之后 |
|------|------------------|
| `WebFetch` / old.reddit 对 PH **403** | `v2/scrape` 可拿到产品页 markdown |
| 评论「发前扫一眼」靠手点 | 可抓 **hunted.space** 的 Comment highlights，列已有角度防撞车 |
| 不知道是否 launch 当天 | 产品页可见 `Launching today`、launch 名（如 AutoSubtitles 2.0） |
| 纯 WebSearch 猜功能 | 直接读 maker 首评、FAQ 里的 **client-side / audio only** 等细节 |

**仍做不到：** 未登录时 PH 讨论区全文常停在 `Login to comment`；要全文评论仍需浏览器登录或 hunted 摘要。

---

## 推荐 URL 策略

| 目的 | URL 模板 | 说明 |
|------|----------|------|
| 产品 + 当前 launch | `https://www.producthunt.com/products/{slug}` | `onlyMainContent: true`，`waitFor` 5–8s |
| 已有评论摘要（优先） | `https://hunted.space/product/{slug}` | 含 Top comment、Comment highlights、票数 |
| 官网细节 | maker 站 / `?ref=producthunt` | 补定价、技术栈 |
| 慎用 | `/posts/{name}` 单独帖 | 旧文档说 JS 重，优先 `/products/` |

**slug 示例：** `autosubtitles`、`catchall`、`framed-mockup-studio`、`attention-insight`、`mixpanel`

---

## v2 Scrape 参数（实测 2026-05-21）

```json
{
  "url": "https://www.producthunt.com/products/autosubtitles",
  "formats": ["markdown"],
  "waitFor": 8000,
  "timeout": 90000,
  "onlyMainContent": true
}
```

- `onlyMainContent: false` → 26k 字符多为导航/页脚，**噪音大**
- `onlyMainContent: true` → ~11k，含 launch、maker、`Login to comment`
- 需要代理时（本机有 clash 等）：curl 加 `--proxy http://127.0.0.1:7890`（可选）

**成功标志（PH 产品页）：** markdown 含产品名、`Launching today` 或 launch 标题、`What do you think`

**成功标志（hunted.space）：** 含 `Comment highlights`、`Upvotes`、`comments`

---

## PowerShell 一键抓（读环境变量）

```powershell
# 一次性设置（当前用户）：
# [Environment]::SetEnvironmentVariable("FIRECRAWL_API_KEY", "fc-你的key", "User")

$slug = "autosubtitles"
$key = $env:FIRECRAWL_API_KEY
if (-not $key) { throw "Set FIRECRAWL_API_KEY first" }

$body = @{
  url = "https://hunted.space/product/$slug"
  formats = @("markdown")
  waitFor = 5000
  timeout = 60000
  onlyMainContent = $false
} | ConvertTo-Json

$md = (Invoke-RestMethod -Uri "https://api.firecrawl.dev/v2/scrape" -Method POST `
  -Headers @{ Authorization = "Bearer $key"; "Content-Type" = "application/json" } `
  -Body $body -TimeoutSec 90).data.markdown

$out = "$env:USERPROFILE\.cursor\ph-scrape-$slug.md"
$md | Out-File $out -Encoding utf8
Write-Host "Saved: $out ($($md.Length) chars)"
```

脚本版：`../scripts/scrape-ph.ps1 -Slug autosubtitles -Source hunted`

---

## Bash（Git Bash / WSL）

```bash
export FIRECRAWL_API_KEY="fc-xxx"
SLUG=autosubtitles
curl -s -X POST "https://api.firecrawl.dev/v2/scrape" \
  -H "Authorization: Bearer $FIRECRAWL_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\":\"https://hunted.space/product/${SLUG}\",\"formats\":[\"markdown\"],\"waitFor\":5000,\"timeout\":60000}"
```

---

## 写入 PH 评论工作流（生成草稿前）

1. **Firecrawl** `hunted.space/product/{slug}` → 保存 markdown  
2. 从 **Comment highlights** 列出 3–5 条已有角度（写入草稿「已有评论」）  
3. 从 **Top comment / 产品描述** 提取 maker 强调点（避免复述当评论）  
4. 定稿实发避开已出现的问法（例：AutoSubtitles 已有 *TikTok bottom UI*、*audio only*、*Descript*、*FFmpeg.wasm*）  
5. 确认 launch 状态后再决定是否写 Congrats  

---

## 其它端点（按需）

| 端点 | 用途 |
|------|------|
| `POST /v2/scrape` | 单页，日常够用 |
| `POST /v2/batch/scrape` | 5 个 PH 链接一次抓 |
| `POST /v2/scrape/{id}/interact` | 需点击「Load more comments」时用（耗额度） |

文档索引：https://docs.firecrawl.dev/llms.txt

---

## 错误码

| 码 | 处理 |
|----|------|
| 402 | 额度用尽，充值或换 key |
| 429 | 降速，间隔 30s+ 再抓 |
| 5xx | 重试，`waitFor` 加大 |

---

## 与 Reddit / NSQ 技能

- **PH 评论：** 本 SOP + `product-hunt-commenter/SKILL.md`  
- **Reddit：** 仍用 PullPush / 浏览器；Firecrawl 仅当 `old.reddit` 403 时补网页（非首选）
