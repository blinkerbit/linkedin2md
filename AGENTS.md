# AGENTS.md — Coding Standards for linkedin2md

## How to Use

When working on this project:

1. Read the **Skill Index** below
2. Identify which skill files apply to the task at hand
3. Load and follow the relevant skill file(s)
4. Multiple skills can apply simultaneously

---

## Skill Index

| Trigger | Skill | Path |
|---------|-------|------|
| `*.py` source files | Language | [`.claude/skills/code/SKILL.md`](.claude/skills/code/SKILL.md) |
| `tests/`, `*test*.py` | Testing | [`.claude/skills/testing/SKILL.md`](.claude/skills/testing/SKILL.md) |
| git commits, PRs | Commits | [`.claude/skills/commits/SKILL.md`](.claude/skills/commits/SKILL.md) |

---

## Universal Rules (all files)

REJECT if:
- Hardcoded secrets or credentials
- Silent error handling (empty `except: pass`, empty `catch {}` blocks)
- `TODO` or `FIXME` without a linked issue number

REQUIRE:
- Descriptive variable and function names
- Error messages that help debugging