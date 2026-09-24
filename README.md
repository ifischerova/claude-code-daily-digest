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

### Claude Code 2.1.281: Větší přehlednost a stabilita 🚀 | Claude Code 2.1.281: Polished, stable, and smarter 🚀

_Claude Code v2.1.281 — 2026-09-24_

## Claude Code 2.1.281: Větší přehlednost a stabilita 🚀

**TL;DR** — Tato verze přináší vylepšenou stabilitu, chytřejší automatický režim a rozhraní, které je nyní přehlednější a lépe se ovládá.

**⭐ Highlight of the release** — Kompletní vylepšení stability při obnovování relací (resuming) a opravy chyb, které dříve způsobovaly ztrátu kontextu nebo nečekané ukončení konverzace.

**What's new**
* **Chytřejší automatický režim:** /insights nyní odhaduje, kolik dotazů na oprávnění by za vás automatika zvládla.
* **Lepší ovládání:** Všechny seznamy (plugins, skills, mcp) mají nyní funkční posuvníky a podporu pro klávesové zkratky.
* **Bezpečnost:** Přísnější kontrola příkazů typu `rm` a vylepšená správa oprávnění v izolovaném prostředí (sandbox).
* **Integrace:** Rozšířená podpora pro Claude apps gateway a Bedrock, včetně podpory IAM rolí.
* **Opravy:** Vyřešeny desítky drobných chyb, od pádů při retries až po zobrazení dlouhých PDF souborů.

**Why you'll care** — Vaše práce bude plynulejší, méně často vás budou přerušovat technické chyby a rozhraní konečně funguje tak, jak byste od moderního nástroje čekali.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.281: Polished, stable, and smarter 🚀

**TL;DR** — This release focuses on rock-solid session reliability, a smarter auto-mode, and a much more polished UI experience.

**⭐ Highlight of the release** — Massive improvements to session resuming, ensuring that large conversations or interrupted tasks pick up exactly where you left off without losing reasoning or context.

**What's new**
* **Auto-mode insights:** The `/insights` command now estimates how many permission prompts the auto-mode could have handled for you.
* **UI Polish:** Lists like `/skills`, `/mcp`, and `/plugin` now feature proper scrollbars and consistent keyboard navigation.
* **Security:** Safer handling of dangerous commands (like `rm`) and better permission isolation for sandboxed tasks.
* **Enterprise/Gateway:** Added support for Bedrock IAM roles, guardrails, and improved Claude apps gateway configuration.
* **Bug squashing:** Resolved numerous issues, including session crashes, PDF reading delays, and inconsistent tool retries.

**Why you'll care** — You’ll spend less time fighting with session state or UI quirks and more time building, with a more reliable and predictable assistant.

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
