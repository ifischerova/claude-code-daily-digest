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

### Claude Code 2.1.267: Lepší stabilita a plynulejší práce 🚀 | Claude Code 2.1.267: Better stability and smoother sessions 🚀

_Claude Code v2.1.267 — 2026-09-10_

## Claude Code 2.1.267: Lepší stabilita a plynulejší práce 🚀

**TL;DR** — Tato aktualizace přináší vylepšenou stabilitu mezipaměti, opravu mnoha chyb při obnovování relací a celkové zrychlení odezvy.

**⭐ Highlight of the release** — Výrazně jsme zlepšili stabilitu mezipaměti (prompt-cache), takže Claude si nyní lépe pamatuje kontext a nástroje, i když přepínáte modely nebo obnovujete starší relace.

**What's new**
* **Kontrola úsilí:** Nové nastavení `maxEffortLevel` vám umožní zastropovat náročnost modelu napříč všemi poskytovateli.
* **Iterace promptů:** Nový příznak `--system-prompt-snapshot off` vynutí čerstvé vykreslení systémového promptu při každém požadavku.
* **Opravy v VS Code:** Vyřešili jsme problémy s výkonem při práci s velkými soubory, vkládáním obrázků na WSL2 a nesprávným barevným schématem v panelech rozdílů (diff).
* **Spolehlivější publikování:** Artifacty se nyní při výpadku spojení automaticky pokusí o obnovení nahrávání.
* **Lepší nápověda:** Claude nyní lépe vysvětluje, proč se akce nezdařila a jak ji opravit, místo aby jen vypsal obecnou chybu.

**Why you'll care** — Vaše relace budou stabilnější, méně často se budou „ztrácet“ a práce v terminálu i editoru bude mnohem předvídatelnější.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.267: Better stability and smoother sessions 🚀

**TL;DR** — This release focuses on rock-solid session restoration, improved prompt-cache efficiency, and a smoother experience across VS Code and CLI.

**⭐ Highlight of the release** — Massive improvements to prompt-cache stability: Claude now remembers tool definitions and context perfectly when you switch models or resume long sessions.

**What's new**
* **Effort control:** Added `maxEffortLevel` to cap compute usage across all providers, including Bedrock, Vertex, and Foundry.
* **Prompt iteration:** Use `--system-prompt-snapshot off` to force a fresh system prompt on every request.
* **VS Code fixes:** Resolved high CPU usage in large workspaces, fixed image pasting on WSL2, and ensured diff views now respect your active color theme.
* **Resilient publishing:** Artifact uploads now automatically retry once if a connection drops mid-transfer.
* **Clearer feedback:** Error messages for failed publishes or API limits are now actionable, telling you exactly what went wrong and how to fix it.

**Why you'll care** — You’ll spend less time managing session state and more time building, with fewer interruptions during model switches or deep-dive coding sessions.

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
