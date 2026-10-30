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

### Claude Code 2.1.314: Chytřejší paměť a lepší zabezpečení 🚀 | Claude Code 2.1.314: Smarter memory and tighter security 🚀

_Claude Code v2.1.314 — 2026-10-30_

## Claude Code 2.1.314: Chytřejší paměť a lepší zabezpečení 🚀

**TL;DR** — Nejnovější verze přináší automatickou kompresi dlouhých konverzací a vylepšené zabezpečení souborů.

**⭐ Hlavní novinka**
Claude nyní automaticky „komprimuje“ dlouhé konverzace (nad 200 tisíc tokenů) v době nečinnosti. Když se ke konverzaci vrátíte, Claude využije její shrnutí, což výrazně zrychluje reakce a šetří místo v paměti.

**Co je nového**
*   **Lepší zabezpečení:** Claude nyní striktně odmítá zápis mimo pracovní adresáře a bezpečněji pracuje s oprávněními v CI/CD úlohách.
*   **Chytřejší řešení chyb:** Pokud narazíte na limit modelu, Claude se nyní automaticky pokusí přepnout na nižší úroveň náročnosti, místo aby prostě přestal fungovat.
*   **Opravy pro VS Code a Desktop:** Vylepšili jsme stabilitu, opravili chyby v zobrazení tabulek a vyřešili problémy s přihlašováním k MCP serverům.
*   **Čistší prostředí:** Automaticky čistíme staré soubory v koši pluginů a skriptů, aby vám nezabíraly místo.

**Proč vás to zajímá**
Práce s dlouhými projekty bude plynulejší a Claude se bude chovat předvídatelněji, i když narazí na složitější bezpečnostní pravidla nebo limity modelu.

Užívejte si kódování s novým Claude!

---

## Claude Code 2.1.314: Smarter memory and tighter security 🚀

**TL;DR** — This release introduces automatic conversation compaction and improved security guardrails for your workflow.

**⭐ Highlight of the release**
Claude now performs "idle compaction" on long conversations (200K+ tokens). When you leave a session idle, it summarizes the history so your next interaction is snappy and efficient, even if your prompt cache has expired.

**What's new**
*   **Strict Security:** Write and edit operations are now strictly blocked outside of your working directories.
*   **Smarter Retries:** If an organization's admin caps your model's effort, Claude Code now automatically lowers the effort level and continues without failing.
*   **Stability Fixes:** Dozens of fixes for VS Code, Claude Desktop, and Remote Control, including better handling of TLS certificates, image pastes, and plugin manifests.
*   **Cleaner Housekeeping:** We now automatically limit the size of plugin and skill trash folders to keep your filesystem tidy.

**Why you'll care**
Your long-running coding sessions will feel much lighter, and you’ll spend less time troubleshooting environment or permission errors.

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
