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

### Oprava oprávnění v příkazech Git 🛠️ | Smoother Git operations are back 🛠️

_Claude Code v2.1.270 — 2026-09-13_

## Oprava oprávnění v příkazech Git 🛠️

**TL;DR** — Opravili jsme chybu, kvůli které si Claude Code po delší době zbytečně říkal o potvrzení u příkazů Git pouze pro čtení.

**⭐ Hlavní novinka**
Vyřešili jsme nepříjemnou regresi, která vás nutila opakovaně schvalovat příkazy jako `git status` nebo `git log` v delších relacích.

**Co je nového**
* Odstranili jsme zbytečné výzvy k potvrzení u bezpečných operací v Gitu.
* Claude teď opět plynule pracuje s vaším repozitářem bez přerušování.

**Proč vás to zajímá**
Vaše práce s Gitem bude zase o něco hladší a bez zbytečného vyrušování.

Ať se vám dnes skvěle kóduje!

---

## Smoother Git operations are back 🛠️

**TL;DR** — We’ve fixed a bug where Claude Code would unnecessarily ask for permission to run read-only Git commands during long sessions.

**⭐ Highlight of the release**
We squashed a regression that was interrupting your workflow by prompting for approval on simple commands like `git status` or `git log`.

**What's new**
* Removed redundant permission prompts for safe, read-only Git operations.
* Improved session stability so Claude stays focused on your code, not your configuration.

**Why you'll care**
Your terminal experience is now back to being fluid and distraction-free.

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
