# Project Objective

Extract all Agentic AI blog posts from Notion workspace for static publishing (GitHub Pages ready format).

# Data Source

- Notion workspace: Agentic AI related blog contents
- Approximately 8 pages under "Agentic AI" section
- Access via MCP server plugin connection

# Required Output Structure

- Output root directory: `/Users/jeff/blog/Sehyeogkim.github.io/blog_data/Agentic_AI`
- Create one directory per post under category directories
- Directory naming:
  - Use category-based naming: `theory-definition-agentic-ai`, `theory-structure-agentic-ai`, etc.
  - Follow kebab-case naming convention
- Inside each post directory, create:
  - `content.txt`: full page content in original order
  - `images/`: all images used in that post

# content.txt Rules

- Keep text blocks in the same order as the original Notion page
- For each image position in the page, insert a marker line at the exact location:
  - `[IMAGE: images/<saved-file-name>]`
- Do not move all image references to the end; keep them inline where they appeared
- Include minimal metadata header at the top:
  - `Title: ...`
  - `URL: ...`
  - `PageID: ...`
  - `Date: ...` (if available)
  - `Category: Agentic AI`

# Image Rules

- Download original image sources when accessible from Notion
- Save into each post's local `images/` directory only
- Use deterministic names in appearance order:
  - `img-001.<ext>`, `img-002.<ext>`, ...
- Match `content.txt` marker paths exactly

# Execution Behavior

- Do not start bulk extraction until user explicitly says to start
- Before running extraction, confirm output root directory once
- Make the process resumable:
  - Skip already completed posts unless user asks to re-run
  - Avoid duplicate image downloads when files already exist
- Never store credentials in files or commit history

# Quality Checks (per run)

- Verify each processed post has:
  - `content.txt`
  - at least zero or more image files in `images/`
  - all `[IMAGE: ...]` markers pointing to existing files
- Report summary:
  - number of posts processed
  - number skipped
  - number failed (with page URLs)

# Content Categories

Based on roadmap from plan.txt:
- Theory:
  - Definition of Agentic AI (comparison with Generative AI and LLMs)
  - Structure of Agentic AI (LLM, Memory, Tools, Skills, MCP, Subagents)
- Applications:
  - CLI tools (Codex, Claude Code, Gemini)
  - Desktop applications (Codex, Claude Code + Cowork)
  - Web applications (ChatGPT, Claude, Gemini)
  - IDE integrations (Cursor, VS Code, Anti-gravity)