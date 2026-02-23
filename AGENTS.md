# Repository Guidelines

## Project Structure & Module Organization
- Root-level Markdown (`README.md`, `blog-test.md`, `git-*.md`) holds personal notes and guidance; treat them as reference artifacts, not generated output.
- The `blog/` directory is the active content area for any site-related writing; keep posts or pages inside as plain Markdown and honor the folder naming for any future static-site tooling.
- Keep ad-hoc documents (e.g., `git-branch.md`, `git-commands.md`) focused on their stated topic so contributors know where to look for workflow reminders.

## Build, Test, and Development Commands
- No automated build or test system exists yet—content changes are tracked directly in Markdown.
- Use `git status`, `git add <file>`, and `git commit` to stage updates, then `git push` to share with collaborators.
- For quick previews, open the Markdown in your editor or run `npx serve blog` (or another simple static server) and navigate to `http://localhost:5000` after installing `serve` globally.

## Coding Style & Naming Conventions
- Markdown files should stay lightweight: use `##`, `###` for nested sections, short paragraphs, and bullet lists where clarity demands it.
- Prefer descriptive filenames that mirror the subject (e.g., `git-commands.md` for Git tips); avoid spaces and rely on kebab-case for future consistency.
- Maintain single-space indentation in fenced code blocks and consistent heading capitalization for readability.

## Testing Guidelines
- There are no automated tests; manual review is sufficient. Re-read any updated document for typos and structural consistency before committing.
- If future tooling arrives, document the entry point and expected assertions here before adding scripts.

## Commit & Pull Request Guidelines
- Commit messages should follow `<area>: <short summary>` (e.g., `docs: clarify blog organization`).
- PRs should include a brief description of changes, linked issues or goals if relevant, and mention what was verified manually.

## Security & Configuration Tips
- Avoid checking secrets into Markdown; if configuration becomes necessary, add a template (e.g., `config.example.md`) and ignore the real file via `.gitignore`.
