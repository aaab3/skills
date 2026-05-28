# Thread Router（写稿前必选）

> 抓帖后、写 10–12 条前，选定 **thread_mode**。决定配比与禁则。  
> 配对：`fetch-playbook.md` · `dedup-gate.md`

---

## 判定流程

```
0. op-info-gate.md → info_density（sufficient | thin）
1. comment_count（约）
2. 读顶评 5–8 条（去 bot）→ 梗为主 or 维修/购买为主 or 短夸
3. 帖型 flair：Gallery/Builds vs Help/Question vs Discussion
4. 选 thread_mode → 按配比写稿（info_thin 覆盖 help 配比）
```

---

## thread_mode 表

| thread_mode | 判定 | 10–12 条配比 | 实发 |
|-------------|------|--------------|------|
| `gallery_quiet` | Builds/Gallery · **<15 评** · 顶评短夸 | Filler/Reaction **6–8** · Observation **1–2** · Help **0–1** | 0–1 |
| `gallery_busy` | Gallery · 楼里已聊 **图/键帽/价** · 少聊 OP 轴/壳 | 同上 · **禁 OP 轴/壳/听感顾问** | 0–1 |
| `help_fresh` | Help/故障/购买 · **<30 评** · 顶评在答疑 | Quick fix/Judgment **5–7** · Filler **2–3** | 1–2 |
| `saturated_meme` | **≥100 评** · 顶评以 **梗/段子/单字符** 为主 | Filler/Reaction **7–9** · 维修/纠正 **0–1** | **0–1** |
| `saturated_help` | **≥100 评** · 维修/购买已刷屏 | **1 条** 🟡 新角度或 **不建议发** | 0–1 |

**灰区：** 30–99 评 → 按顶评链选 `gallery_*` 或 `help_fresh`，维修条 **≤3**。

---

## 硬规则（按 mode）

| mode | 禁 |
|------|-----|
| `gallery_*` | `curious which direction` · mango pudding 式听感攻略 · OP 正文轴/壳（楼未接时） |
| `saturated_meme` | 楼里已有句式的维修摘要（loctite / scroll lock / desolder 变体）· meta（`this thread went copypasta`） |
| `saturated_*` | 逐字复刻顶评 · 10 条各写不同维修角度 |
| 全部 | `tough` / `insane combo` hype · 假购买史 · 无图 `bugged me too` |

**情绪档：** 跟顶评（`looks good` / `lol` / `Das not good`），非 budgetkeebs 捡漏腔。

---

## Filler 条数（与 thread_mode 叠加）

| Sub | 默认 | saturated_meme |
|-----|------|----------------|
| r/MechanicalKeyboards | 1–2 | 可 **3–4**（仍 🟢 为主） |
| r/keyboards | 2–3 | 2–3 |

---

## 锚帖示例（实证）

| 帖 | mode |
|----|------|
| [1tp9bdh evo70](https://www.reddit.com/r/MechanicalKeyboards/comments/1tp9bdh/evo_70_r2/) | `gallery_quiet` |
| [1tpdwiw 等货](https://www.reddit.com/r/MechanicalKeyboards/comments/1tpdwiw/) | `gallery_busy`（楼聊键帽） |
| [1tnb6u9 Das 引号](https://www.reddit.com/r/MechanicalKeyboards/comments/1tnb6u9/) | `saturated_meme` |

*路径：`reddit-keyboard-comments/references/thread-router.md`*
