---
name: reddit-engagement
description: >-
  Reddit 版规与评/发写法。主攻抢首评：NSQ、ELI5、Ask(rising)、LPT、pcmr、keyboards、MK
  — 先读 first-comment-playbook.md。推荐帖（具名型号/无线/like X 品牌）必读
  product-recommendation-playbook.md。不替用户决定何时评/发。不用于自动发布、灌水、伪造经历。
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

1. `first-comment-playbook.md` → 优先级、筛帖、日配额、Ask 用 **rising**  
2. `communities.md` → 该 sub 版规 + 形态  
3. `how-to-comment.md` → 缺口、一条一贡献  
4. **若 Type D / 具名型号** → `product-recommendation-playbook.md` §0–§4（合同 → 轴 → 核实 → 再写）  
5. `comment-style-guide.md` § Explainer + `quality-checklist.md`（含 **§ Type D Product Facts**）  
6. 输出：+ **抢首评适配**、当前评数、是否建议发；推荐帖 + **OP 合同 / 规格核对**

**有链接要评论（非抢首评）：**

1. `communities.md` → 该 sub **版规 + 评论形态**  
2. `how-to-comment.md` → 读帖、缺口、一条一贡献  
3. **若推荐帖** → `product-recommendation-playbook.md`  
4. `reddit-comment-symbols.md` → 短评默认少引号、少 Markdown  
5. `comment-style-guide.md` + `quality-checklist.md`  
6. 输出：版规 relevant · OP 在问什么 · 楼里已覆盖 · 主推 1 条（推荐帖含规格核对表）

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
