---
name: reddit-engagement
description: >-
  Reddit 版规与评/发写法。评论必先过 Evidence Gate（先证据后写稿；#3 弱则不 draft）与
  Local Comment Rule。主攻抢首评：NSQ、ELI5、Ask(rising)、LPT、pcmr、keyboards、MK。
  具名型号触发 Named Product Gate + product-recommendation-playbook.md。输出结论前置
  （可发/改后可发/不建议发）。不替用户决定何时评/发。不用于自动发布、灌水、伪造经历。
  用户给 Reddit 链接、评论稿、发帖稿、抢首评、选题或 flop 时使用。
---

# Reddit：评论与发帖

## 技能是什么

各 **常用 sub 的版规 + 在该版内怎么写评论/怎么写帖**（调查结论），外加 **通用评/发方法**。

| 层 | 文件 |
|----|------|
| 机制（可选） | `references/00-reddit-essence.md` |
| 怎么写评论 | `references/how-to-comment.md` |
| 怎么写发帖 | `references/how-to-post.md` |
| **社区规则** | `references/communities.md` |
| **抢首评（七社区）** | `references/first-comment-playbook.md` |
| **推荐帖（具名型号）** | `references/product-recommendation-playbook.md` |
| **符号/引号** | `references/reddit-comment-symbols.md` |

**何时评论、何时发帖：用户自定。** Agent 不默认安排日程；用户蹲评/抢首评时按 `first-comment-playbook.md` 筛帖与配额。

---

## Evidence Gate（评论工作流第一步 · 未过不准写稿）

动笔前只列三项（可对用户用中文）：

1. **OP facts** — OP 原文/标题里说了什么（一句合同）  
2. **Existing comments already covered** — 高赞已覆盖什么（3–5 点；未读全楼标 ⚠️ 不完整）  
3. **Safe claim I can add** — 本帖还能安全补的 **一个** local move（见下）

**若 #3 弱、与楼里重复、或无法核实 → 不生成英文评论。** 只输出「不建议发」+ 依据。禁止先写一版再优化语气绕过闸门。

**终稿只允许：**

- OP 直接陈述的事实  
- 当前可见评论里直接出现的内容  
- 官网/厂商页核实过的规格（Type D 见 Named Product Gate）  
- 诊断类猜测 — 必须带不确定性（`sounds like` / `I'd check`）

其余一律删除。

---

## Local Comment Rule

好评论 = **本 thread 里的一个动作**，不是通用说明书。

允许：纠正一个误解 · 补一个 caveat · 给第一步排查 · 问一个有用的变量 · 压一个不切实际的预期 · **推荐一条 lane**（不是购物清单）

**若换 20 个同类帖仍成立 → 重写或 skip。** 故事帖（Ask）= 一个叙事切片，不是型号清单。

---

## Named Product Gate（条件触发）

评论将出现 **≥1 具名品牌+型号** 时，在写稿前核实：**connection · layout · switch type（若相关）· firmware/software（若相关）· 是否匹配 OP 合同**。

**任一项未知 → 不点名该型号**（可说 lane + `check the exact SKU`）。细则 → `product-recommendation-playbook.md` §0–§4。

---

## 默认输出（评论 · 结论前置）

```
结论：可发 / 改后可发 / 不建议发

依据：
- OP 明确说：
- 楼里已覆盖：
- 我能安全补的点：（一个 local move）

删掉/改弱：
- （无则写「无」）

建议实发：（仅「可发」或「改后可发」时给英文；附简短中文释义 + 🟢🟡🔴）
```

抢首评可追加：适配 S/A/B/C · 当前评数。Type D 可追加：规格核对表（每 SKU 一行）。**Gate 判不建议发时不得附「建议实发」。**

细节 → `how-to-comment.md` §1、§7 · `quality-checklist.md` § Evidence Gate · § Claim Wording

---

## 工作流

### 路由（先判断帖型）

| 信号 | 额外必读 |
|------|----------|
| OP 问买什么 / wireless / like {Brand} / alternatives / gift | **`product-recommendation-playbook.md`**（全文 §0–§5） |
| 评论将写 **≥1 个具体品牌+型号** | 同上 + `research-protocol.md` 核实 connectivity |
| 键盘 Help / MK Question / pcmr 外设 | `subreddit-context.md` + `keyboard-domain-guide.md` |
| NSQ / ELI5 / Ask 无产品名 | 不必开推荐专册 |

---

**抢首评 / 蹲 new / 七社区评论：**

1. **Evidence Gate**（上）→ 不过则不写稿  
2. `first-comment-playbook.md` → 优先级、筛帖、日配额、Ask 用 **rising**  
3. `communities.md` → 该 sub 版规 + 形态  
4. **若 Type D / 具名型号** → Named Product Gate + `product-recommendation-playbook.md` §0–§4  
5. Local move 定稿 → `comment-style-guide.md` § Explainer + `quality-checklist.md`  
6. **默认输出**（结论前置模板）

**有链接要评论（非抢首评）：**

1. **Evidence Gate**  
2. `communities.md` → 版规 + 形态  
3. **若推荐帖** → Named Product Gate + `product-recommendation-playbook.md`  
4. `reddit-comment-symbols.md` · `comment-style-guide.md` + `quality-checklist.md`  
5. **默认输出**（结论前置）

**要发帖 / 选题 / flop：**

1. `communities.md` → 该 sub **版规 + 发帖形态**  
2. `how-to-post.md` → 验重、形态、发后诊断  
3. Ask / NSQ 专册按需打开（见下）  

**键盘帖（非购买也可加载）：** `subreddit-context.md`、`keyboard-domain-guide.md`。

---

## 专册（按需）

| 文件 | 内容 |
|------|------|
| **`product-recommendation-playbook.md`** | **Type D：OP 合同、产品轴、HE/无线、MK 日帖 reply、禁清单** |
| `askreddit-post-playbook.md` | Ask 验重、公式、饱和、打分 |
| `subreddit-nsq-guide.md` 等 | NSQ 细则 |
| `reddit-community-atlas.md` | 更多 sub |
| `reddit-search-sop.md` | 验重 |
| `quality-checklist.md` | 自检（语气 + **型号事实**） |
| `comment-style-guide.md` | 反 AI（含 **§ Explainer**） |
| `reddit-comment-symbols.md` | 引号习惯、Markdown 误触 |
| `first-comment-playbook.md` | 七社区抢首评 |
| `research-protocol.md` | 列型号前搜索 |
| `professional-upvoted-comments.md` | P1–P8 专业钩（推荐帖常用 P1+P3） |
| `workspace/comments/2026-05-23-first-comment-7-subs.md` | Tab 链接与日流程 |

**扩展（按需）：** `easy-karma-small-subs.md`、`account-phase-routing.md`

**历史策略（非默认）：** `posting-strategy-recalibration.md`

---

## 硬禁止（平台 + 版规）

未读帖就写 · 删帖重发 · FreeKarma 子版 · affiliate/自动发布 · 伪造经历 · 违反该 sub 版规（Ask 正文非空、NSQ 顶层笑话等）

**推荐帖额外禁止：**

- 未核实 **wireless / HE** 就写具名 SKU  
- **Mode 审美题** 默认推 Q HE / NuPhy **Air HE** 当无线替代  
- `wireless-ish` / `premium-ish` 与品牌型号同句  
- 未读帖批量生成 workspace「待发」并标 ✅（须 **发前重读 OP+楼**）

---

## Workspace

`workspace/comments/`、`workspace/posts/` — **示例草稿，非技能规则**；可能过期。具名型号备稿须带 **规格核对** 或标 ❌ 勿发。见 `workspace/comments/README.md`。
