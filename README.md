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

### Claude Code 2.1.327: Stabilita a vylepšené ovládání 🚀 | Claude Code 2.1.327: Reliability and performance boosts 🚀

_Claude Code v2.1.327 — 2026-11-18_

## Claude Code 2.1.327: Stabilita a vylepšené ovládání 🚀

**TL;DR** — Tato aktualizace přináší desítky oprav stability, rychlejší start na Windows a lepší správu oprávnění.

**⭐ Hlavní novinka**
Nyní můžete bezpečněji spravovat MCP servery pomocí `claude mcp add-json <název> -`, což umožňuje vložit konfiguraci ze standardního vstupu a udržet citlivé tokeny mimo historii příkazového řádku.

**Co je nového**
* **Lepší přehled:** Příkaz `/status` nyní vypíše všechny chyby v konfiguraci, neplatné vazby kláves nebo nedostupné sandbox prostředí.
* **Bezpečnější export:** Claude se vás nyní zeptá, než přepíše existující soubor při použití `/export`.
* **Rychlejší Windows:** Zrychlili jsme start aplikace díky optimalizaci vyhledávání PowerShellu a Gitu.
* **VS Code integrace:** Přidali jsme možnost „Claude Code: Add to Chat“ přímo do kontextové nabídky v průzkumníku souborů.
* **Opravy:** Vyřešili jsme desítky drobných pádů, problémů se zobrazením v terminálu a nekonzistentního chování při obnovování relací.

**Proč vás to zajímá**
Claude Code je nyní spolehlivější parťák, který vás méně vyrušuje technickými chybami a lépe spolupracuje s vaším prostředím.

Ať se vám dnes dobře kóduje!

---

## Claude Code 2.1.327: Reliability and performance boosts 🚀

**TL;DR** — This release focuses on stability, faster Windows startup, and smarter permission handling to keep your workflow smooth.

**⭐ Highlight of the release**
You can now add MCP servers securely using `claude mcp add-json <name> -`, which reads configuration from stdin so your tokens never touch the command line history.

**What's new**
* **Diagnostic clarity:** The `/status` command now lists broken agents, command errors, and ignored permission settings in one place.
* **Safer exports:** Claude will now ask for confirmation before overwriting an existing file during `/export`.
* **Faster Windows:** Startup time is improved by optimizing how the app finds PowerShell and Git.
* **VS Code love:** A new "Claude Code: Add to Chat" option in the Explorer context menu lets you quickly @-mention files and folders.
* **Bug fixes:** Dozens of fixes for UI glitches, session resumption crashes, and shell display issues.

**Why you'll care**
Your coding sessions should feel snappier and more predictable, with fewer interruptions from configuration errors or lost states.

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
