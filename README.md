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

### Claude Code 2.1.280: Nový model Opus 5.5 a spousta vylepšení 🚀 | Claude Code 2.1.280: Meet Opus 5.5 and improved polish 🚀

_Claude Code v2.1.280 — 2026-09-23_

## Claude Code 2.1.280: Nový model Opus 5.5 a spousta vylepšení 🚀

**TL;DR** — Tato aktualizace přináší chytřejší model Claude Opus 5.5, lepší podporu myši v terminálu a desítky oprav pro plynulejší práci.

**⭐ Hlavní novinka**
Nyní můžete využívat model **Claude Opus 5.5** (`claude-opus-5-5`), který se stává výchozím pro uživatele placených tarifů. Nabízí obrovské 1M kontextové okno a efektivnější práci s mezipamětí.

**Co je nového**
*   **Ovládání:** V celoobrazovkovém režimu už můžete pohodlně scrollovat seznamy kolečkem myši a klikat na možnosti pluginů.
*   **Flexibilita:** Přidali jsme proměnnou `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH`, díky které si můžete sami upravit limit pro délku popisků MCP nástrojů.
*   **Stabilita:** Opravili jsme desítky drobných chyb, od chování klávesových zkratek v dialozích až po bezpečnější zpracování souborů a automatických režimů.
*   **VS Code:** Přidali jsme nové přehledné dialogy pro stav, sandbox a integraci s Chrome.

**Proč by vás to mělo zajímat**
Claude Code je díky těmto změnám mnohem předvídatelnější a lépe reaguje na vaše vstupy, ať už pracujete v terminálu nebo přímo ve VS Code.

Užívejte si kódování s novým výkonem!

---

## Claude Code 2.1.280: Meet Opus 5.5 and improved polish 🚀

**TL;DR** — This release introduces the new Claude Opus 5.5 model, enhanced mouse support, and a massive set of stability fixes.

**⭐ Highlight of the release**
We’ve added **Claude Opus 5.5** (`claude-opus-5-5`) as the new default Opus model, featuring a 1M token context window and improved cost-efficiency with cache reads.

**What's new**
*   **Better navigation:** You can now use your mouse wheel to scroll lists in fullscreen mode and click directly on plugin state options.
*   **Customization:** Use the new `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` setting to increase the character limit for MCP tool descriptions.
*   **Quality of life:** We’ve squashed dozens of bugs, including fixes for dialog navigation, auto-mode retries, and better handling of invisible characters in terminal inputs.
*   **VS Code updates:** New dedicated dialogs for status, sandbox mode, and Chrome integration make managing your session easier than ever.

**Why you'll care**
Everything feels snappier and more reliable, especially when handling complex workflows or navigating settings in fullscreen mode.

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
