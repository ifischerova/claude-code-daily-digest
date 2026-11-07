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

### Claude Code 2.1.319: Vylepšené úkoly na pozadí a správa oprávnění 🚀 | Claude Code 2.1.319: Background tasks and permission controls 🚀

_Claude Code v2.1.319 — 2026-11-07_

## Claude Code 2.1.319: Vylepšené úkoly na pozadí a správa oprávnění 🚀

**TL;DR** — Tato aktualizace přináší lepší podporu pro MCP úkoly na pozadí, pokročilé možnosti správy oprávnění a řadu oprav pro hladší chod v terminálu.

**⭐ Highlight of the release** — Claude Code nyní umí přesunout MCP úkoly běžící v terminálu na pozadí a automaticky zpracovat výsledek, jakmile jsou hotové, což vám uvolní ruce pro další práci.

**What's new**
- **Lepší kontrola:** Nové nastavení `permissions.denyInsteadOfPrompting` automaticky zamítne akce vyžadující povolení, místo aby na vás čekalo v terminálu.
- **Optimalizace API:** Příkaz `/claude-api latency-optimize` vám pomůže najít místa, kde vaše implementace zbytečně čeká.
- **Přehled nákladů:** Příkaz `/usage` nyní zobrazuje aktuální útratu za den, týden i měsíc (pro uživatele za bránou Claude).
- **Stabilita:** Opraveno mnoho chyb, včetně problémů s načítáním diffů u souborů pojmenovaných `HEAD` a pádů při plném disku.

**Why you'll care**
Claude Code je nyní mnohem méně rušivý – díky úkolům na pozadí a automatickému zamítání nevyžádaných akcí se můžete lépe soustředit na kód.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.319: Background tasks and permission controls 🚀

**TL;DR** — This release introduces background MCP tasks, smarter permission handling, and a host of stability fixes to keep your workflow fluid.

**⭐ Highlight of the release** — Claude Code can now move MCP tasks in the terminal to the background automatically, reporting the results to Claude once they finish so you don't have to wait.

**What's new**
- **Advanced permissions:** Added `permissions.denyInsteadOfPrompting` to automatically block actions that would normally trigger a prompt, keeping your terminal flow uninterrupted.
- **Latency optimization:** Use `/claude-api latency-optimize` to identify bottlenecks in your API usage and test faster configurations.
- **Spend visibility:** `/usage` now shows your spend for today, this week, and this month for developers behind a Claude apps gateway.
- **Reliability:** Fixed numerous bugs, including issues where folders named `HEAD` broke diff views and cases where disk space errors caused data loss.

**Why you'll care**
These changes make Claude Code feel more like a background companion and less like a blocker, letting you stay in the zone while it handles the heavy lifting.

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
