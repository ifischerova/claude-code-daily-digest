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

### Claude Code 2.1.287: Nový parťák, který vám kryje záda 🛡️ | Claude Code 2.1.287: Meet your new sidekick 🛡️

_Claude Code v2.1.287 — 2026-10-02_

## Claude Code 2.1.287: Nový parťák, který vám kryje záda 🛡️

**TL;DR** — Nejnovější verze přináší „hlídacího agenta“, vylepšenou podporu pluginů a desítky oprav pro plynulejší vývoj.

**⭐ Hlavní novinka**
Představujeme *You should know* – vestavěného pomocníka, který aktivně sleduje vaši práci a upozorní vás na detaily, které byste vy nebo Claude mohli přehlédnout. Aktivujete ho příkazem `/plugin enable cc-plugin-you-should-know@builtin`.

**Co je nového**
*   **Claude Mods:** Pluginy nyní mohou hlouběji ovlivňovat chování Claude Code.
*   **Chytřejší vyhledávání:** V seznamu agentů nyní funguje filtr `n:<text>` pro rychlé hledání v názvech a úkolech.
*   **Lepší správa modelů:** Modely Opus 4.7+ a Fable nyní standardně využívají 1M kontextové okno.
*   **Vylepšení pro VS Code:** Přidána možnost „Run in background“ pro přesun úloh na pozadí a lepší přehled o běžících procesech.
*   **Opravy a stabilita:** Desítky oprav zaměřených na odezvu, práci s MCP servery a přístupnost pro čtečky obrazovky.

**Proč vás to bude zajímat**
Claude Code je teď zase o kus samostatnější a pozornější, což vám ušetří čas strávený kontrolou drobných chyb.

Ať se kód jen zelená!

---

## Claude Code 2.1.287: Meet your new sidekick 🛡️

**TL;DR** — This release introduces a proactive "watchdog" agent, deeper plugin capabilities, and a massive set of stability improvements.

**⭐ Highlight of the release**
We've added *You should know*, a built-in agent that watches your back and flags things you or Claude might miss. Enable it with `/plugin enable cc-plugin-you-should-know@builtin`.

**What's new**
*   **Claude Mods:** Plugins can now modify deeper system behaviors.
*   **Improved Navigation:** Use the `n:<text>` filter in the agents view to instantly jump to specific tasks or sessions.
*   **Expanded Context:** Opus 4.7+ and Fable models now default to a 1M context window.
*   **VS Code Enhancements:** You can now move commands to the background and see live output from shells directly in the agent map.
*   **Polished Experience:** Dozens of fixes for MCP server reliability, file handling, and accessibility for screen readers.

**Why you'll care**
With an agent actively keeping an eye on your workflow, you can focus on the logic while Claude handles the oversight.

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
