# Cursor Agent Skills

Personal [Cursor Agent Skills](https://cursor.com/docs/context/skills) for Reddit engagement, Product Hunt comments, web research MCP, novel-based teaching, and plan grilling.

**Repository:** https://github.com/aaab3/skills

**Push (any agent session):** from this folder run `.\push-to-github.ps1` (SSH deploy key; see `.deploy-keys/README.md` and Cursor rule `github-skills-sync`).

Install: symlink or copy each `*/SKILL.md` folder into `~/.cursor/skills/` (Windows: `%USERPROFILE%\.cursor\skills\`).

## Skills

| Folder | Purpose |
|--------|---------|
| **`reddit-keyboard-comments`** | **Comments 版** — 仅 `r/keyboards` + `r/MechanicalKeyboards`；thread_mode · Filler · human-voice-gate · 输出 `Desktop\评论\` |
| `reddit-keyboard-promotion` | Reddit 多社区（NSQ、ELI5、Ask、LPT、pcmr 等）；keyboards/MK 评论请用 **comments** 技能 |
| `product-hunt-commenter` | Product Hunt comment drafts (CQS-first) |
| `web-research-mcp` | Firecrawl / Tavily / MCP research routing |
| `grill-me` | Pre-implementation Socratic interview (盘问) |
| `novel-knowledge-teaching` | Teach technical concepts via narrative fiction |

## Backup convention

Replacing a skill folder: move the old tree to `_backup/{skill-name}-YYYY-MM-DD/` before committing the new version.

## Recent changes (2026-05-28)

- **reddit-keyboard-comments:** New Comments 版技能（从 promotion 拆出 keyboards/MK 专评）；含 `thread-router`, `dedup-gate`, `human-voice-gate`, `skill-map` 等 references。

## Recent changes (2026-05)

- **reddit-keyboard-promotion:** Added `references/product-recommendation-playbook.md`; wired into `SKILL.md`, `how-to-comment.md`, `quality-checklist.md` (Type D product facts).

## License

Per-skill; third-party adapters (e.g. grill-me from Matt Pocock) retain their original licenses where noted in each `SKILL.md`.
