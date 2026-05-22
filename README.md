# Cursor Agent Skills

Personal [Cursor Agent Skills](https://cursor.com/docs/context/skills) for Reddit engagement, Product Hunt comments, web research MCP, novel-based teaching, and plan grilling.

**Repository:** https://github.com/aaab3/skills

**Push (any agent session):** from this folder run `.\push-to-github.ps1` (SSH deploy key; see `.deploy-keys/README.md` and Cursor rule `github-skills-sync`).

Install: symlink or copy each `*/SKILL.md` folder into `~/.cursor/skills/` (Windows: `%USERPROFILE%\.cursor\skills\`).

## Skills

| Folder | Purpose |
|--------|---------|
| `reddit-keyboard-promotion` | Reddit comment/post playbooks (NSQ, ELI5, Ask, keyboards, MK, …); includes **product-recommendation-playbook** (Type D facts) |
| `product-hunt-commenter` | Product Hunt comment drafts (CQS-first) |
| `web-research-mcp` | Firecrawl / Tavily / MCP research routing |
| `grill-me` | Pre-implementation Socratic interview (盘问) |
| `novel-knowledge-teaching` | Teach technical concepts via narrative fiction |

## Recent changes (2026-05)

- **reddit-keyboard-promotion:** Added `references/product-recommendation-playbook.md`; wired into `SKILL.md`, `how-to-comment.md`, `quality-checklist.md` (Type D product facts); fixed Mode/wireless/NuPhy HE draft in workspace.

## License

Per-skill; third-party adapters (e.g. grill-me from Matt Pocock) retain their original licenses where noted in each `SKILL.md`.
