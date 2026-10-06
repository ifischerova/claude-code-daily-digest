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

### Claude Code 2.1.291: Opravy pro hladší průběh práce 🛠️ | Claude Code 2.1.291: Smoother sessions ahead 🛠️

_Claude Code v2.1.291 — 2026-10-06_

## Claude Code 2.1.291: Opravy pro hladší průběh práce 🛠️

**TL;DR** — Tato aktualizace opravuje chyby, které způsobovaly ztrátu zpráv a problémů s potvrzováním v cloudu.

**⭐ Hlavní novinka** — Vyřešili jsme nepříjemnou chybu, kvůli které se při ukončení relace občas ztratily poslední zprávy.

**Co je nového**
* Opravili jsme výpadek v cloudových relacích, kdy Claude přestal reagovat na žádosti o oprávnění.
* Zajištění stability: už se vám nestane, že by se vaše poslední konverzace při vypnutí aplikace „vypařila“.

**Proč vás to bude zajímat** — Všechno teď funguje spolehlivě, takže se můžete plně soustředit na kód bez obav o svá data.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.291: Smoother sessions ahead 🛠️

**TL;DR** — This update fixes bugs that caused dropped permission prompts and lost session messages.

**⭐ Highlight of the release** — We've squashed a bug that was causing your final messages to vanish when quitting a session.

**What's new**
* Fixed an issue where cloud sessions would occasionally ignore your responses to permission prompts.
* Improved data integrity so your conversation history stays intact when you close the app.

**Why you'll care** — You can now work with peace of mind, knowing your commands and chat history are being saved correctly.

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
