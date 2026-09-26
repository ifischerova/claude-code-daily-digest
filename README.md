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

### Claude Code 2.1.283: Novinky v auditech a ovládání 🛠️ | Claude Code 2.1.283: Prompt auditing and UI refinements 🛠️

_Claude Code v2.1.283 — 2026-09-26_

## Claude Code 2.1.283: Novinky v auditech a ovládání 🛠️

**TL;DR** — Tato aktualizace přináší nástroj pro audit vašich promptů, lepší správu pluginů a řadu oprav pro hladší zážitek v terminálu i VS Code.

**⭐ Highlight of the release** — Nový příkaz `/doctor prompt-audit` (nebo `/checkup prompt-audit`), který zkontroluje vaše soubory `CLAUDE.md`, dovednosti a agenty a upozorní vás na zastaralé vzorce, které nebudou s nejnovějšími modely fungovat optimálně.

**What's new**
* **Lepší správa modelů:** Přidáno nastavení `availableModelsMatch: "exact"` pro přísnější kontrolu verzí a `deniedModels` pro blokování konkrétních modelů.
* **Vylepšené pluginy:** Opraveno načítání v kontejnerech, lepší validace a přehlednější správa nainstalovaných pluginů.
* **Optimalizace výkonu:** Rychlejší start aplikace díky odložení načítání některých komponent a efektivnější práce s API připojením.
* **Vylepšení rozhraní:** Seznamy (tasks, mcp, help) nyní podporují rolování kolečkem myši a klávesy pro stránkování.
* **Opravy:** Vyřešeny problémy v režimu Vim, vylepšeno renderování odkazů v terminálu Warp a opraveno chování při práci s repozitáři.

**Why you'll care**
Získáte větší kontrolu nad tím, jak Claude přistupuje k vašim projektům, a díky novému auditu promptů zajistíte, že vaše nastavení bude vždy využívat plný potenciál nejnovějších modelů.

Ať se vám dnes v kódu daří!

---

## Claude Code 2.1.283: Prompt auditing and UI refinements 🛠️

**TL;DR** — This release introduces a prompt auditing tool, better plugin management, and a massive list of stability fixes across terminal and VS Code.

**⭐ Highlight of the release** — The new `/doctor prompt-audit` (or `/checkup prompt-audit`) command, which scans your `CLAUDE.md` files, skills, and agents to flag outdated prompting patterns that aren't optimized for newer models.

**What's new**
* **Model control:** Added `availableModelsMatch: "exact"` to restrict model versions and `deniedModels` to explicitly block specific models.
* **Plugin polish:** Fixed plugin loading in devcontainers, improved validation logic, and added better feedback when managing installed plugins.
* **Faster startup:** Claude now delays loading non-essential components until they are actually needed, making your initial launch snappier.
* **UI navigation:** Lists (tasks, help, plugins, etc.) now support mouse-wheel scrolling and page-up/down keys for easier navigation.
* **Fixes:** Squashed bugs in Vim mode, fixed clickable links in Warp, and resolved various issues with MCP server connectivity and session persistence.

**Why you'll care**
You’ll spend less time troubleshooting configuration issues and more time using a tool that’s better at staying up-to-date with your project’s specific requirements.

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
