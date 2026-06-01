---
name: find-skills
description: Discover, evaluate, and install OpenCode agent skills from the internet. Use when the user wants to find a skill for a specific task, browse the opencode ecosystem, or get installation instructions for a known skill.
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: discovery
---

## What I do

- Search the internet for OpenCode agent skills (SKILL.md definitions) relevant to a task
- Surface candidates from the official ecosystem, GitHub, awesome-opencode, and opencode.cafe
- Summarize what each candidate does, its source, and trust signals
- Provide copy-paste installation steps for the chosen skill
- Verify the candidate's `name` follows OpenCode naming rules before recommending it

## When to use me

Use this when the user:
- Asks "is there a skill for X?" or "find me a skill that does Y"
- Wants to browse the opencode ecosystem for available skills
- Asks how to install a specific skill by name
- Mentions a third-party skill repo and wants help evaluating and installing it

Ask a clarifying question if the user's goal is ambiguous (e.g. they say "find a skill" without describing the task).

## Discovery workflow

1. Clarify the task
   - Ask the user what problem they want the skill to solve and any constraints (language, offline-only, etc.).

2. Search the internet
   - Use `websearch` with queries like:
     - `opencode skill <task>` site:github.com
     - `awesome-opencode skills`
     - `SKILL.md <task>` opencode
     - `opencode.cafe skills <task>`
   - Prefer results from these primary sources, in order:
     1. `https://opencode.ai/docs/skills/` (official spec)
     2. `https://opencode.ai/docs/ecosystem/` (official ecosystem)
     3. `https://github.com/awesome-opencode/awesome-opencode`
     4. `https://opencode.cafe`
     5. Individual GitHub repos whose READMEs reference `SKILL.md`

3. For each candidate, fetch the page with `webfetch` and extract:
   - Skill name and description (from frontmatter)
   - Repository URL and current stars/last-commit signal
   - Required frontmatter fields (`name`, `description`)
   - Any permissions the skill needs

4. Validate the candidate
   - Confirm `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$` and is 1-64 chars
   - Confirm `name` equals the directory containing `SKILL.md`
   - Confirm `description` is 1-1024 chars
   - Reject skills that fail any rule; report why and suggest a fix

5. Present 1-3 ranked options
   - Show name, one-line description, source URL, install path
   - Let the user pick, or proceed with the top match if they said "just pick one"

6. Install
   - Create the directory under one of the discovery paths (prefer project-local `.opencode/skills/<name>/`):
     - `.opencode/skills/<name>/SKILL.md`
     - `.claude/skills/<name>/SKILL.md`
     - `.agents/skills/<name>/SKILL.md`
     - `~/.config/opencode/skills/<name>/SKILL.md` (global)
   - Write the file with the verified frontmatter
   - If pulling from a git URL, `curl` or `wget` the raw `SKILL.md` rather than copy-pasting manually

7. Verify load
   - List the parent `skills/` directory to confirm the file is in place
   - Remind the user to restart opencode or rescan skills if the new entry does not appear in the `skill` tool description

## Output format

For each candidate, return:

```
- name: <skill-name>
  description: <one line>
  source: <url>
  install: .opencode/skills/<skill-name>/SKILL.md
  trust: <official | community | unverified>
```

## Guardrails

- Never invent a skill that does not exist. If the search returns nothing, say so and suggest writing a custom SKILL.md from scratch.
- Do not install skills from untrusted sources without flagging the trust level.
- Do not overwrite an existing skill at a given path without confirming with the user.
- Do not bypass the frontmatter rules. Skills missing `name` or `description` will not load.
