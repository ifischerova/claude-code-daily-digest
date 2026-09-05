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

### Claude Code 2.1.261: Lepší správa dovedností a ladění 🛠️ | Claude Code 2.1.261: Smarter skill management & fixes 🛠️

_Claude Code v2.1.261 — 2026-09-05_

## Claude Code 2.1.261: Lepší správa dovedností a ladění 🛠️

**TL;DR** — Tato verze přináší vylepšenou diagnostiku dovedností, větší flexibilitu v nastavení výstupů a opravu mnoha drobných chyb pro plynulejší práci.

**⭐ Hlavní novinka** — Příkaz `/skill-doctor`. Konečně uvidíte, které dovednosti (skills) zbytečně plýtvají vaším kontextem, a můžete je snadno vyčistit.

**Co je nového**
* **Více prostoru:** Nastavení `bashOutputMaxChars` a `taskOutputMaxChars` nyní umožňují předávat až 128 000 znaků výstupu přímo do kontextu.
* **Organizační politika:** Příkaz `/status` nyní jasně napoví, proč se firemní pravidla nenačetla (např. kvůli proxy).
* **Větší soubory:** Nový příznak `--append-subagent-system-prompt-file` pro načítání dlouhých systémových promptů ze souboru.
* **VS Code vylepšení:** Snadnější správa MCP serverů a možnost „sbalit“ okna s dotazy, abyste viděli na historii konverzace.
* **Opravy:** Vyřešili jsme zasekávání při psaní, chyby v Remote Control a lepší stabilitu při práci za firemními proxy.

**Proč by vás to mělo zajímat** — Claude Code je nyní mnohem přehlednější a lépe zvládá složité projekty, kde záleží na každém tokenu a stabilním připojení.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.261: Smarter skill management & fixes 🛠️

**TL;DR** — This release adds powerful new diagnostic tools, increased output limits, and a long list of quality-of-life fixes for a smoother terminal experience.

**⭐ Highlight of the release** — The new `/skill-doctor` command. You can now see exactly which loaded skills are going unused and how much context they’re costing you, making it easy to prune your setup.

**What's new**
* **More breathing room:** You can now increase inline command and task output up to 128K characters using new settings.
* **Clearer status:** `/status` now explains why your organization's policy might fail to load, such as proxy interference.
* **Large prompts:** Use `--append-subagent-system-prompt-file` to feed massive system prompts to subagents without hitting command-line limits.
* **VS Code polish:** Manage MCP servers directly from the UI and use the new fold button on prompts to keep your conversation flow visible while answering questions.
* **Reliability:** Fixed various input glitches, Remote Control UI hangs, and connectivity issues behind TLS-inspecting corporate proxies.

**Why you'll care** — You’ll spend less time debugging your environment and more time coding, with better visibility into what’s actually using up your model's context.

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
