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

### Claude Code 2.1.295: Vylepšené notifikace a stabilita 🚀 | Claude Code 2.1.295: Better notifications and stability 🚀

_Claude Code v2.1.295 — 2026-10-09_

## Claude Code 2.1.295: Vylepšené notifikace a stabilita 🚀

**TL;DR** — Tato verze přináší desítky oprav stability, lepší podporu pro pluginy a chytřejší notifikace v terminálu.

**⭐ Highlight of the release** — Podpora protokolu OSC 7501, díky kterému váš terminál nyní pozná, kdy Claude Code pracuje, kdy na vás čeká a kdy má hotovo.

**What's new**
* **Chytřejší notifikace:** Přidáno `$.ui.notify`, které umožňuje pluginům posílat nativní oznámení přímo do vašeho systému.
* **Lepší spolehlivost:** Opraveno mnoho chyb, které způsobovaly zamrzání terminálu při dlouhých výstupech nebo pády spojení s MCP servery.
* **Vylepšené pluginy:** Přidána varování při instalaci pluginů, pokud nelze načíst konfigurační soubor, a možnost blokovat akce při selhání hooků.
* **Opravy pro VS Code:** Vyřešeny problémy s fokusem klávesnice a chyby při větvení konverzací.
* **Stabilita na pozadí:** Vylepšeno chování úloh běžících na pozadí, aby se vzájemně neovlivňovaly a neblokovaly.

**Why you'll care**
Claude Code je nyní mnohem stabilnější, lépe komunikuje s vaším prostředím a díky novým notifikacím už nezmeškáte, když bude potřebovat vaši pozornost.

Užijte si kódování s novou verzí!

---

## Claude Code 2.1.295: Better notifications and stability 🚀

**TL;DR** — This release brings dozens of stability fixes, improved plugin support, and smarter terminal notifications.

**⭐ Highlight of the release** — Added support for the OSC 7501 protocol, allowing your terminal to visually indicate whether Claude Code is busy, waiting for you, or finished.

**What's new**
* **Smarter notifications:** Added `$.ui.notify`, allowing plugins to send native system notifications.
* **Improved reliability:** Fixed numerous terminal freezes during long outputs and connection issues with MCP servers.
* **Plugin enhancements:** Added warnings for plugin configuration issues and a new `block` option for failing hooks to prevent invalid actions.
* **VS Code fixes:** Resolved keyboard focus issues and bugs when branching conversations.
* **Background stability:** Improved background task management to prevent tasks from interfering with each other.

**Why you'll care**
Claude Code is now significantly more reliable and communicative, ensuring your workflow stays smooth without missing critical status updates.

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
