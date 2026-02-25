---
name: read-tistory
description: Read and explain a Tistory blog post that may require login. Use when the user asks to open https://jeffdissel.tistory.com/, sign in with Kakao login using user-provided credentials, read one target post, and deliver a clear explanation or summary in the user's requested language.
---

# Read Tistory

## Overview

Open Tistory, authenticate with credentials provided during the session, access a target post, and explain its content clearly for the user. Use browser automation for reliable page rendering and extraction.

## Required Inputs

- Kakao account ID/email
- Kakao account password
- Target post URL or title hint
- Output language and depth (short summary vs detailed explanation)

## Workflow

1. Confirm target
- Confirm exactly which post to explain (explicit URL preferred).
- If not provided, ask for the exact title or let the user pick from recent posts.

2. Sign in
- Navigate to `https://jeffdissel.tistory.com/`.
- Open the `카카오계정으로 로그인` flow (Kakao login).
- Use browser automation to enter user-provided Kakao credentials.
- If MFA/captcha blocks automation, pause and ask the user for the next action.

3. Open and read the post
- Open the target post page.
- Extract the main body only (ignore sidebar/navigation/ads where possible).
- Capture core claims, steps, code snippets, and conclusions.

4. Explain for the user
- Provide a concise explanation first.
- Then provide a structured breakdown:
  - Topic and purpose
  - Key points
  - Important examples or code
  - Practical takeaway

5. Validate understanding
- Mention any unclear or missing parts from the original post.
- Offer follow-up explanations on specific sections if requested.

## Output Format

- `Summary`: 3-6 lines in plain language
- `Details`: bullet list of major points
- `Notes`: assumptions, ambiguities, or missing context from the source post

## Safety and Privacy

- Do not store credentials in files, logs, or commits.
- Use credentials only for the live session.
- Avoid copying unrelated private account content; read only the requested post.
