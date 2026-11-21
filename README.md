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

### Claude Code 2.1.330: Nástroj na kreslení grafů a lepší firemní správa 📈 | Claude Code 2.1.330: Built-in charts and enterprise polish 📈

_Claude Code v2.1.330 — 2026-11-21_

## Claude Code 2.1.330: Nástroj na kreslení grafů a lepší firemní správa 📈

**TL;DR** — Tato aktualizace přináší vestavěné kreslení grafů, vylepšenou podporu firemních účtů a desítky oprav pro plynulejší práci.

**⭐ Hlavní novinka**
Nyní můžete Claude požádat o vizualizaci dat – vestavěný modul „easel“ automaticky vykreslí přehledné grafy přímo v terminálu nebo jako součást metrik MCP.

**Co je nového**
*   **Firemní správa:** Lepší integrace s podnikovými konzolemi Anthropicu a možnost správy nastavení na úrovni organizace.
*   **Rychlost a stabilita:** Výrazné zrychlení práce se soubory, opravy zamrzání při dlouhých konverzacích a stabilnější práce s nástroji.
*   **VS Code vylepšení:** Nové příkazy jako `/fork` nebo `/workflows`, lepší práce s klávesovými zkratkami a oprava problémů s kopírováním kódu.
*   **Samostatné běžce (Self-hosted runners):** Lepší správa úloh, diagnostika a podrobnější metriky pro týmy provozující vlastní infrastrukturu.

**Proč vás to bude zajímat**
Claude Code je díky těmto změnám mnohem spolehlivější pro každodenní kódování a vizualizace dat vám pomůže rychleji pochopit složité metriky bez přepínání oken.

Užívejte si kódování a ať se vám daří!

---

## Claude Code 2.1.330: Built-in charts and enterprise polish 📈

**TL;DR** — This release adds a built-in charting tool, improved enterprise identity management, and a massive set of stability fixes.

**⭐ Highlight of the release**
Meet "easel," a built-in tool that automatically draws charts when you ask for them or when viewing MCP metrics, making your data much easier to visualize.

**What's new**
*   **Enterprise support:** Better sign-in flows for organizations managed via Anthropic’s Admin Console.
*   **Performance:** Faster file diffs, fixes for session freezes during long conversations, and improved responsiveness in Code Mode.
*   **VS Code enhancements:** Added `/fork` and `/workflows` commands, plus better handling of keyboard shortcuts and terminal focus.
*   **Self-hosted runner updates:** Improved error reporting, smarter resource management, and new metrics for tracking job execution times.

**Why you'll care**
This update removes many of the small "papercuts" that disrupt your flow, making Claude Code faster, smarter, and much more capable for complex development tasks.

Happy coding, and enjoy the new charts!

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
