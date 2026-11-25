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

### Claude Code 2.1.332: Vylepšené MCP a stabilnější práce 🚀 | Claude Code 2.1.332: Better MCP support and rock-solid stability 🚀

_Claude Code v2.1.332 — 2026-11-25_

## Claude Code 2.1.332: Vylepšené MCP a stabilnější práce 🚀

**TL;DR** — Tato aktualizace přináší podporu pro MCP servery, chytřejší správu paměti a desítky oprav pro plynulejší vývoj.

**⭐ Highlight of the release** — Nyní můžete přímo v menu `/` využívat schopnosti (skills) z připojených MCP serverů, což výrazně rozšiřuje možnosti Claude Code.

**What's new**
* **MCP integrace:** Schopnosti z MCP serverů se zobrazují jako `server:skill`.
* **Lepší stabilita:** Opravili jsme desítky příčin zamrzání terminálu a nadměrného využívání paměti.
* **Chytřejší modely:** Vylepšené přepínání mezi modely a lepší podpora pro nejnovější verze (např. Sonnet 5.5).
* **Vylepšené VS Code:** Hladší práce s historií, lepší zobrazení diffů a oprava drobných chyb v UI.
* **Spolehlivější autentizace:** Jasnější chybové hlášky při problémech s přihlášením.

**Why you'll care** — Váš Claude Code bude konečně méně „zamrzat“ při složitějších úkolech a díky podpoře MCP serverů získáte mnohem výkonnějšího pomocníka pro své projekty.

Ať se vám dnes kódování daří!

---

## Claude Code 2.1.332: Better MCP support and rock-solid stability 🚀

**TL;DR** — This release brings beta MCP server support, significant performance improvements, and dozens of fixes to keep your workflow smooth.

**⭐ Highlight of the release** — You can now access skills from MCP servers directly via the `/` menu, labeled as `server:skill` for easy discovery.

**What's new**
* **MCP Integration:** Beta support for using external server skills directly in your chat.
* **Performance Boosts:** Dozens of fixes for terminal freezes, memory leaks, and unresponsive sessions.
* **Smarter Model Logic:** Improved fallback behavior and better support for the latest model versions like Sonnet 5.5.
* **VS Code Refinements:** Smoother diff handling, better history navigation, and UI polish for a less cluttered experience.
* **Clearer Feedback:** Better error reporting for login issues and saved-session status.

**Why you'll care** — You’ll spend less time troubleshooting the tool and more time building, thanks to improved stability and deeper integration with your custom MCP tools.

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
