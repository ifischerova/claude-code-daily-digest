# Claude Code Changelog Digest — Design

**Date:** 2026-06-22
**Author:** Iva Fischerova
**Status:** Proposed

## One-liner

A scheduled GitHub Action that, every morning, checks the Claude Code changelog,
and — if there is a new release — has an LLM rewrite it as a friendly newsletter,
emails it to me, and commits the digest into the repo as a public archive.

The repo doubles as a portfolio piece: "I automate a routine task (reading
changelogs) with AI."

## Goals

- Demonstrate practical AI automation of a real, recurring chore.
- Be impressive at a glance: a visitor sees the latest AI-written digest right in
  the README, without running anything.
- Read well: the digest has personality (friendly newsletter voice), not raw
  bullet dumps.

## Non-goals (YAGNI)

- No Slack/Telegram/Discord delivery — email + git archive only.
- No database — state is derived from files in the repo.
- No web UI.

## Architecture

Small, focused Python modules. The GitHub Action just runs the script and commits
the results.

| Component | Responsibility |
|-----------|----------------|
| `src/changelog.py` | Fetch `CHANGELOG.md` from `anthropics/claude-code`; extract the latest version block (version string + raw notes). |
| `src/summarizer.py` | Call OpenRouter; turn raw notes into the chatty newsletter (subject + body). |
| `src/mailer.py` | Send the digest via the Resend API. |
| `src/digest.py` | Write the digest archive file; update the README's "latest" section. |
| `src/main.py` | Orchestrate: fetch → "is this version new?" → summarize → email → archive. Exit quietly if nothing new. |
| `tests/test_changelog.py` | Unit tests for the parser against sample changelog text. |
| `.github/workflows/daily-digest.yml` | Cron (~07:00 CEST) + manual `workflow_dispatch`. Runs the script, commits new digest + README. |
| `digests/YYYY-MM-DD-vX.Y.Z.md` | The public archive — one Markdown file per release. |
| `README.md` | Story intro, badges, embedded latest digest, setup guide. |
| `requirements.txt`, `.gitignore`, `.env.example`, `LICENSE` | Project scaffolding. |

## Data flow

1. **Fetch:** GET the raw `CHANGELOG.md` from
   `https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md`.
2. **Parse:** The newest `##` heading is the latest release. Capture its version
   string and the raw notes until the next `##` heading.
3. **New-version guard:** If `digests/` already contains a file for that version,
   there is nothing new → exit 0 quietly (no email, no commit). This is the
   anti-spam mechanism; the changelog does not change every day.
4. **Summarize:** Send the raw notes to OpenRouter with a "friendly newsletter
   editor" system prompt. The model returns a JSON object with a catchy subject
   line and a Markdown body.
5. **Email:** Send via Resend (`from` = `onboarding@resend.dev`, `to` = `MAIL_TO`).
6. **Archive:** Write `digests/<date>-v<version>.md`, and refresh the README's
   `<!-- LATEST:START -->…<!-- LATEST:END -->` block with the new digest.
7. **Commit:** The workflow commits the new files as
   `Iva Fischerova <fischerova.ivka@gmail.com>`.

## The "chatty and interesting" layer

Personality lives in two places:

**Summarizer prompt** — the model is instructed to produce a fixed structure:
- A **catchy subject line** (with one tasteful emoji), e.g.
  `☕ Claude Code v1.2.0 — checkpoints have landed`.
- **TL;DR**: one sentence.
- **⭐ Highlight of the release**: the single most exciting change, up top.
- **What's new**: plain-language bullets (translate dev-speak to human terms).
- **Why you'll care**: a short "so what" angle.
- A warm sign-off.

**Repo presentation** — README opens like a story ("I got tired of reading
changelogs, so I made an AI read them for me"), shows a `last digest` badge, and
embeds the most recent digest so the value is visible in 2 seconds.

## Configuration

Environment variables (provided as GitHub Actions secrets):

| Variable | Purpose |
|----------|---------|
| `OPENROUTER_API_KEY` | OpenRouter auth. **Set in GitHub Secrets only — never committed.** |
| `OPENROUTER_MODEL` | Model slug. Default `google/gemini-3.1-flash-lite`; swappable to `qwen/qwen3.6-flash`. Exact slug verified against OpenRouter's `/models` endpoint at build time. |
| `RESEND_API_KEY` | Resend auth. |
| `MAIL_TO` | Recipient address. |
| `MAIL_FROM` | Sender; default `onboarding@resend.dev` (works on Resend free tier without a verified domain). |

A `.env.example` documents these for local runs; real values live in GitHub
Secrets. `.env` is gitignored.

## Error handling

- **Network/parse failure on fetch:** log and exit non-zero so the Action run is
  visibly red; no partial email.
- **LLM call failure:** retry once, then fall back to emailing the raw changelog
  notes with a note that the AI summary was unavailable (so you still get the
  release news).
- **Email failure:** still commit the archive (the digest isn't lost), but exit
  non-zero so the run is flagged.
- **No new version:** exit 0, no side effects.

## Testing

- Unit tests for `changelog.py` parsing against fixture text (multiple versions,
  edge cases like a single version, pre-release tags).
- `summarizer` and `mailer` kept thin and dependency-injected so they can be
  exercised without live API calls (network calls behind a small client seam).

## Security notes

- The OpenRouter key originally shared in chat is considered compromised and will
  be **rotated** by the user; a fresh key goes into GitHub Secrets.
- No secret is ever written to the repo. The workflow reads them from
  `secrets.*`.

## Open items to confirm at build time

- Exact OpenRouter model slugs (verify via the API; the names may need adjusting).
- Confirm `anthropics/claude-code` default branch is `main` for the raw URL.
