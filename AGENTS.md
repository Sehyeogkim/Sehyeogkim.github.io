# AGENTS: Project Operating Guide

## Mission
- Primary goal: build a structured blog series about Agentic AI and commit progress to GitHub continuously.
- The blog must capture both process and knowledge, not just final conclusions.
- Every major post should include practical artifacts: command snippets, code blocks, and images (PNG or screenshots).

## Content Roadmap (from `plan.txt`)
- Large Topic 1: `Theory`
- Large Topic 2: `Applications`

### Theory
- `1a`: Definition of Agentic AI, with explicit comparison against Generative AI and LLMs.
- `1b`: Structure of Agentic AI:
  - LLM
  - Memory
  - Tools
  - Skills
  - MCP
  - Subagents

### Applications
- `2a` Command Line Interface (CLI):
  - Codex
  - Claude Code
  - Gemini
- `2b` Desktop:
  - Codex
  - Claude Code (+ Cowork)
- `2c` Web Application:
  - ChatGPT
  - Claude
  - Gemini
- `2d` Integrated Development Environment (IDE):
  - Cursor
  - VS Code
  - Anti-gravity

## Repository Structure
- Root-level Markdown (`README.md`, `git-*.md`, `plan.txt`) is reference and planning material.
- `blog/` is the publishing directory for all blog posts.
- Suggested media location: `blog/images/` for screenshots and PNG diagrams used by posts.

## Post Template Requirements
- Use `##` and `###` headings for clear sectioning.
- Keep paragraphs short and practical.
- Include these sections when relevant:
  - Goal/Problem
  - Definition or Concept
  - Comparison table
  - Architecture or process diagram (image)
  - Commands used
  - Code snippets
  - Key takeaway
- Include at least one concrete example per post.

## File Naming Rules
- Use kebab-case file names.
- Keep names descriptive and topic-aligned.
- Preferred style:
  - `theory-definition-agentic-ai.md`
  - `theory-structure-agentic-ai.md`
  - `applications-cli-agentic-tools.md`

## Build, Preview, and Review
- There is no automated build/test yet.
- Manual review is required before commit:
  - spelling and grammar
  - heading consistency
  - code block formatting
  - image links resolve correctly
- Optional local preview:
  - `npx serve blog`
  - open `http://localhost:5000`

## Git Workflow
- Use small, incremental commits after each meaningful content unit.
- Standard flow:
  - `git status`
  - `git add <file>`
  - `git commit -m "docs: <short summary>"`
  - `git push`
- Commit message format:
  - `<area>: <short summary>`
  - Example: `docs: add theory definition of agentic ai`

## Security and Hygiene
- Do not include secrets or tokens in Markdown.
- If config examples are needed, use template files and keep real values out of git.
- Keep planning docs (`plan.txt`) updated as roadmap changes.
