# 📰 Claude Code Daily Digest

> I got tired of reading changelogs, so I taught an AI to read them for me — and email me the good parts every morning.

This repo is a tiny, fully automated newsletter. Every day a GitHub Action checks the [Claude Code](https://github.com/anthropics/claude-code) changelog. When there's a new release, an LLM (via [OpenRouter](https://openrouter.ai)) rewrites the notes as a friendly digest, emails it to me through [Resend](https://resend.com), and commits it here as a permanent archive.

No servers. No cost beyond pennies of tokens. Just a robot doing my reading for me. ☕

## ✨ How it works

```
GitHub Action (daily cron)
  └─ fetch CHANGELOG.md from anthropics/claude-code
       └─ new version? ── no ─► stop quietly
              │ yes
              ▼
        LLM writes a friendly digest (OpenRouter)
              ▼
        email it (Resend)  +  commit it to /digests
```

## 📬 Latest digest

<!-- LATEST:START -->

### Claude Code 2.1.328: Chytřejší automatizace a lepší stabilita 🚀 | Claude Code 2.1.328: Smarter automation and improved stability 🚀

_Claude Code v2.1.328 — 2026-11-19_

## Claude Code 2.1.328: Chytřejší automatizace a lepší stabilita 🚀

**TL;DR** — Tato aktualizace přináší režim "auto" pro modely na cloudu, vylepšení pro Code Mode a desítky oprav pro plynulejší vývoj.

**⭐ Highlight of the release** — Nyní můžete využívat automatický režim (auto mode) pro modely Claude Opus a Sonnet 4.6 i na platformách jako Amazon Bedrock, Google Cloud nebo Microsoft Foundry.

**What's new**
- **Code Mode:** Rychlejší běh skriptů, lepší správa úloh na pozadí a oprava chyb při práci s příkazy.
- **Spolehlivost:** Opraveny desítky drobných chyb v terminálu, zasekávání obrazovky a správa úloh.
- **Self-hosted runner:** Nové metriky pro sledování fronty a lepší podpora pro repozitáře.
- **Code Review:** Příkaz `/code-review` je nyní přehlednější a zaměřuje se primárně na chyby a pravidla v `CLAUDE.md`.

**Why you'll care** — Váš vývojářský workflow bude díky rychlejšímu Code Mode a širší podpoře cloudu méně přerušovaný a předvídatelnější.

Šťastné kódování!

---

## Claude Code 2.1.328: Smarter automation and improved stability 🚀

**TL;DR** — This release brings auto mode to cloud-hosted models, significant Code Mode refinements, and dozens of stability fixes.

**⭐ Highlight of the release** — We’ve enabled auto mode for Claude Opus and Sonnet 4.6 across Amazon Bedrock, Google Cloud, Microsoft Foundry, and the Claude apps gateway.

**What's new**
- **Code Mode:** Faster script execution, better background task handling, and improved command output visibility.
- **Reliability:** Fixed various UI freezes, terminal input issues, and scheduled task management bugs.
- **Self-hosted runner:** Added new metrics for session queuing and better repository configuration options.
- **Code Review:** The `/code-review` command is now more focused, clearly highlighting bugs and `CLAUDE.md` violations with suggested fixes.

**Why you'll care** — You’ll spend less time wrestling with configuration and interrupted scripts, letting you focus on building with a more responsive Claude.

Happy coding!

<!-- LATEST:END -->

Browse every past edition in [`/digests`](./digests).

## 🛠️ Run it yourself

1. Fork this repo.
2. Add **Actions secrets** (`Settings → Secrets and variables → Actions`):
   - `OPENROUTER_API_KEY` — from openrouter.ai
   - `RESEND_API_KEY` — from resend.com
   - `MAIL_TO` — where the digest is sent
3. (Optional) Add **Actions variables**: `OPENROUTER_MODEL`, `MAIL_FROM`.
4. Under **Settings → Actions → General → Workflow permissions**, choose **Read and write** so the action can commit each new digest back.
5. Enable Actions, then run **Daily Claude Code Digest → Run workflow** to test.

### 🔑 Getting your keys

- **`OPENROUTER_API_KEY`** — sign up at [openrouter.ai](https://openrouter.ai), open **Keys → Create Key**, and copy the `sk-or-...` value. Add a little credit (the flash models cost a fraction of a cent per digest).
- **`RESEND_API_KEY`** — sign up at [resend.com](https://resend.com), open **API Keys → Create API Key** (permission: *Sending access*), and copy the `re_...` value. It's shown only once.
- **`MAIL_TO`** — the address that receives the digest. On Resend's free tier (no custom domain) you can only send to the email you registered your Resend account with, so use that one to start.

The default sender is `onboarding@resend.dev` (Resend's free-tier address), so you don't need `MAIL_FROM` or a verified domain to get going. Free tier covers 100 emails/day — plenty for one daily digest. Keep every key in GitHub Secrets, never in the code.

Local run (to test before scheduling):

```bash
pip install -r requirements-dev.txt
pytest
```

To run the digest end-to-end locally you must set the environment variables yourself (there's no `.env` auto-loader — `.env.example` just documents what's needed):

```bash
export OPENROUTER_API_KEY=... RESEND_API_KEY=... MAIL_TO=you@example.com
python -m src.main
```

On Windows PowerShell: `$env:OPENROUTER_API_KEY="..."` (etc.) then `python -m src.main`.

## 🧱 Tech

Python · OpenRouter · Resend · GitHub Actions. Tested with `pytest`; every network call is injectable so the suite runs offline.

---

Built by Iva Fischerova.
