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

### Nová verze Claude Code 2.1.331 je tady! 🚀 | Claude Code 2.1.331 is here! 🚀

_Claude Code v2.1.331 — 2026-11-24_

## Nová verze Claude Code 2.1.331 je tady! 🚀

**TL;DR** — Tato aktualizace přináší podporu Code Mode pro více cloudových platforem, rychlejší starty a desítky oprav pro plynulejší práci v terminálu i VS Code.

**⭐ Highlight of the release** — Claude Code nyní nativně podporuje Code Mode v terminálových relacích na platformách Amazon Bedrock, Google Cloud, Microsoft Foundry a Claude Platform na AWS.

**Co je nového**
* **Lepší diagnostika:** Příkaz `claude doctor` nyní prověří připojení k API a vypíše podrobnosti o případných chybách.
* **Vylepšení pro VS Code:** Přidány rychlé akce pro řešení konfliktů při slučování (merge) a možnost přidat buňky z poznámkových bloků přímo do chatu.
* **Rychlejší start:** Snížili jsme čekací dobu při spouštění, zejména pokud nepracujete v Git repozitáři.
* **Opravy chyb:** Vyřešili jsme desítky problémů, včetně zamrzání při volání MCP nástrojů a nechtěného zkracování textů v úzkých oknech.

**Proč vás to bude zajímat**
Vaše vývojářské prostředí bude díky těmto optimalizacím stabilnější a rychlejší, ať už pracujete lokálně nebo v cloudu.

Šťastné kódování!

---

## Claude Code 2.1.331 is here! 🚀

**TL;DR** — This update brings Code Mode support to major cloud platforms, faster startup times, and dozens of fixes to make your workflow smoother in both the terminal and VS Code.

**⭐ Highlight of the release** — We’ve added Code Mode support for terminal sessions on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, and the Claude Platform on AWS.

**What's new**
* **Better diagnostics:** The `claude doctor` command now checks API connectivity and reports specific HTTP status codes or errors.
* **VS Code improvements:** New quick-fix actions for merge conflicts and the ability to add notebook cells directly into your chat.
* **Faster startup:** We’ve reduced wait times when starting sessions, especially for non-Git projects.
* **Bug fixes:** We’ve squashed dozens of issues, including hangs during MCP tool calls and text truncation in narrow terminal windows.

**Why you'll care**
These optimizations make your development environment more stable and responsive, whether you're working locally or in the cloud.

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
