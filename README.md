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

### Claude Code je nyní na Vertexu svižnější 🚀 | Claude Code is now faster on Vertex 🚀

_Claude Code v2.1.322 — 2026-11-10_

## Claude Code je nyní na Vertexu svižnější 🚀

**TL;DR** — Claude Code nyní využívá režim „fast“ na platformě Vertex AI pro rychlejší odezvu.

**⭐ Hlavní novinka**
Do globální, americké i evropské oblasti jsme přidali podporu režimu „fast“ (rychlý režim) pro Vertex. Pokud by však systém zrovna neměl kapacitu, automaticky se přepne na standardní rychlost, abyste nikdy nečekali zbytečně dlouho.

**Co je nového**
* Rychlejší odezva při používání Claude Code na infrastruktuře Vertex.
* Inteligentní záloha: pokud „fast“ režim není dostupný, plynule přejdeme na standardní rychlost.

**Proč vás to zajímá**
Vaše práce bude díky kratším prodlevám při dotazech na Claude plynulejší a efektivnější.

Ať se vám dnes skvěle kóduje!

---

## Claude Code is now faster on Vertex 🚀

**TL;DR** — Claude Code now supports "fast" mode on Vertex AI for snappier performance.

**⭐ Highlight of the release**
We’ve enabled "fast" mode for the global, US, and EU regions on Vertex. If the fast mode isn't available, the system will now gracefully fall back to standard speed so you never hit a wall.

**What's new**
* Faster response times when running Claude Code via Vertex infrastructure.
* Smart fallback: if the fast lane is busy, we automatically switch to standard speed to keep you moving.

**Why you'll care**
Less waiting for your AI assistant means more time spent actually building and shipping your projects.

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
