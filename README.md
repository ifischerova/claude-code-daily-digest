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

### Claude Code 2.1.269: Nové možnosti vyhodnocování a vylepšení pro VS Code 🚀 | Claude Code 2.1.269: Plugin evaluation and VS Code power-ups 🚀

_Claude Code v2.1.269 — 2026-09-12_

## Claude Code 2.1.269: Nové možnosti vyhodnocování a vylepšení pro VS Code 🚀

**TL;DR** — Tato verze přináší nástroje pro vyhodnocování pluginů, vylepšené rozhraní ve VS Code a desítky oprav pro plynulejší práci.

**⭐ Highlight of the release** — Nový příkaz `claude plugin eval`, který vám umožní spustit testovací sadu pro pluginy a získat přehledné výsledky ve formátu JSON nebo HTML.

**What's new**
* **Nové nástroje:** Přidali jsme `/output-style` pro přepínání výstupů a možnost nastavit limit souběžných agentů (`CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`).
* **Lepší přehled ve VS Code:** Nová mapa agentů, dialogy pro správu oprávnění a háčků (hooks) přímo v editoru.
* **Bash vylepšení:** Claude nyní zobrazuje diff změn u souborů, které upravil pomocí Bash příkazů.
* **Opravy:** Vyřešili jsme problémy s terminály (kitty, st, WezTerm), vylepšili filtrování návrhů pro asijské jazyky a opravili stabilitu při obnovování relací.

**Why you'll care**
Získáte větší kontrolu nad tím, jak Claude pracuje s pluginy a soubory, a díky novým prvkům ve VS Code už nebudete muset tak často přepínat do terminálu.

Užívejte si kódování a ať se daří!

---

## Claude Code 2.1.269: Plugin evaluation and VS Code power-ups 🚀

**TL;DR** — This release introduces plugin evaluation tools, a major UI upgrade for VS Code, and dozens of stability fixes.

**⭐ Highlight of the release** — You can now use `claude plugin eval` to run a plugin's evaluation suite against Claude Code and generate clean, reproducible JSON or HTML reports.

**What's new**
* **New controls:** Added `/output-style` for headless sessions and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` to scale up your agent fan-outs.
* **VS Code enhancements:** Added a new agent map, a dedicated Permission rules dialog, and a Hooks manager directly in the extension.
* **Bash visibility:** Claude now provides a diff of file changes whenever it executes a Bash command that edits files.
* **Refinements:** Fixed various terminal rendering issues (kitty, st, WezTerm), improved non-English prompt suggestions, and hardened session resumption logic.

**Why you'll care**
These updates make Claude Code more transparent and easier to manage, whether you're building plugins or just need a more reliable experience in your VS Code workspace.

Happy coding, and see you in the next build!

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
