# 如何评论（写法与流程）

> 各 sub **版规 + 评论形态** → `communities.md`。  
> **是否评论、评哪：用户决定。** 本文只写怎么读帖、怎么写一条合格评论。  
> **闸门总述：** `SKILL.md` § Evidence Gate · Local Comment · 默认输出。

---

## 1. Evidence Gate（动笔前 · 未过不准写稿）

与 `SKILL.md` 相同，Agent **必须先填** 再决定是否写英文：

| # | 字段 | 要求 |
|---|------|------|
| 1 | **OP facts** | 一句话合同（= OP 在问什么） |
| 2 | **Existing comments already covered** | 高赞 3–5 点；未读全楼写 `⚠️ 楼内未完整` |
| 3 | **Safe claim I can add** | **一个** local move（§2）；须能指到本帖 |

**停止条件：** #3 弱、与 #2 同义、或关键事实未核实 → **不 draft**；只输出「不建议发」+ 依据。

**允许进终稿的事实来源：**

- OP 直接写的  
- 当前线程可见评论里直接写的  
- 官网/厂商页核实（Type D：`research-protocol.md`）  
- 诊断猜测 — 仅 `sounds like` / `usually` / `I'd check`（见 `quality-checklist.md` § Claim Wording）

**额外路由（Gate 之后）：**

- 该 sub 版规 → `communities.md`  
- 抢首评 → `first-comment-playbook.md`  
- Type D / ≥1 具名型号 → `SKILL.md` Named Product Gate + `product-recommendation-playbook.md` §0–§4  

拉帖：Reddit JSON 优先；旧帖 PullPush 仅补评论（`pullpush-api.md`）。PullPush 不能代替「楼里已覆盖」。

**跳过帖：** archived、locked、已与顶楼神评完全同义、或 Gate #3 为空。

---

## 2. Local Comment Rule（一条评论 = 一个本地动作）

好评论是对 **当前 thread** 的一个小动作，不是换帖仍成立的说明书。

| Local move | 对应贡献类型 | 形态 |
|------------|--------------|------|
| 纠正一个误解 | 机制 / 纠正 | 1 句事实 |
| 补一个 caveat | Tradeoff | 一条件 + 一结论 |
| 给第一步排查 | Diagnostic | 先查 X |
| 问一个有用的变量 | 反问 | ≤1 问句 |
| 压一个不切实际的预期 | Tradeoff / 纠正 | 1 句 |
| 推荐 **一条 lane**（非清单） | Tradeoff | ≤2 系列名 + 1 踩坑；具名 SKU 走 playbook |
| Filler / 共鸣 / 接梗 | 故事、展示、梗 | 3–20 词 |

**失败测试：** 草稿套到 20 个同类帖仍成立 → 重写或 skip。

钩子参考 → `comment-patterns.md`、`high-engagement-comment-playbook.md`、`professional-upvoted-comments.md`。

---

## 3. 长度（按 sub 形态，非按 karma 阶段）

| 社区 | 参考词数 |
|------|----------|
| CasualConversation, NewToReddit | 3–25 |
| NoStupidQuestions | 12–35，1–2 句 |
| AskReddit | 5–25 |
| Ergo / BudgetKeebs / Help 类 | 15–40 |

长帖楼里已有全面长答时：**更短或换角度**，非硬性 karma 规则。

---

## 4. 符号与引号

- **引号 `""` 在短评里不多**；默认 **不用**，见 `reddit-comment-symbols.md` §1。  
- Markdown（`**`、`^`、列表）短评 **少用**，见同文件 §2。

---

## 5. 语气（反 AI）— Gate 通过后再跑

**主文件：** `comment-style-guide.md`（禁词 + **§ Explainer**）  
**自检：** `quality-checklist.md` §AI Voice · §Claim Wording · §NSQ Voice  

不伪造购买史（`research-protocol.md`）。

### Agent 出稿规则

1. **先一句答 OP**（或一个 local move）；默认 **不要第三句**。  
2. **禁止** `Partly … Partly …`、`*Your X is common*`、`*legit coping*`、三段平衡小结。  
3. **禁止为像人而加口语：** 不要每条用 `Yeah` / `Honestly` / `tbh` 开头。`honestly` / `tbh` / `yeah` **仅当去掉后句子仍成立** 时保留。  
4. **禁止** 为语气伪造 ownership、确定性或亲身经历。  
5. 中文释义可以长；**英文实发**按 sub 词数上限 + Claim Wording + checklist。  
6. 读一遍：是 **本帖的一个动作** 还是 **百科摘要**？后者必须重写或 skip。

---

## 6. 发前检查

- [ ] Evidence Gate 三项已填；#3 非空且为一个 local move  
- [ ] 符合该 sub **版规**  
- [ ] 不与最高票 **同角度**  
- [ ] 每条 claim 符合 `quality-checklist.md` § Claim Wording  
- [ ] 符号/引号 → `reddit-comment-symbols.md` §4  
- [ ] Type D：§ Type D Product Facts（若具名型号）

---

## 7. Agent 工作流与输出

```
拉线程 → Evidence Gate（不过则停）
  → communities.md
  → [Type D?] Named Product Gate + product-recommendation-playbook
  → 一个 local move 定稿 → quality-checklist
  → 默认输出（结论前置）
```

### 默认输出模板（必须）

```
结论：可发 / 改后可发 / 不建议发

依据：
- OP 明确说：
- 楼里已覆盖：
- 我能安全补的点：

删掉/改弱：
-

建议实发：
（仅可发/改后可发；英+简短中+🟢🟡🔴）
```

- **不建议发：** 无「建议实发」；可说明缺 OP/缺楼内/缺核实。  
- **Type D 追加：** 规格核对（每具名 SKU 一行：Connection / 是否贴 OP 合同）。  
- **抢首评追加：** 适配 S/A/B/C · 当前评数（`first-comment-playbook.md` §6）。

无链接时：只给 sub `/new` + 版规；**禁止** PullPush 归档当待发。

---

## 8. 禁止

未读帖就写 · Gate 未过仍出英文稿 · 同帖多条相似 · affiliate · FreeKarma · 伪造经历 · 违反 sub 版规

*路径：`reddit-keyboard-promotion/references/how-to-comment.md`*
