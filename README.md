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

### Claude Code 2.1.318: Větší stabilita a lepší správa přihlášení 🚀 | Claude Code 2.1.318: Stability and authentication improvements 🚀

_Claude Code v2.1.318 — 2026-11-04_

## Claude Code 2.1.318: Větší stabilita a lepší správa přihlášení 🚀

**TL;DR** — Tato aktualizace přináší desítky oprav stability, lepší správu přihlášení a plynulejší práci v síťových prostředích.

**⭐ Highlight of the release** — Výrazně jsme zlepšili odolnost konfigurace při práci na sdílených síťových discích, takže se vám už nestane, že by Claude Code „zapomněl“ vaše nastavení nebo MCP servery.

**What's new**
* **Lepší přehled o přihlášení:** Claude vás nyní včas upozorní, když bude potřeba se znovu přihlásit ke claude.ai.
* **Flexibilnější modely:** Přidali jsme možnost nastavit úroveň úsilí (`effort`) pro rychlé dílčí úlohy.
* **Bezpečnější oprávnění:** Správa oprávnění pro nové agenty je nyní standardizovaná a předvídatelnější.
* **Stabilita:** Opravili jsme desítky chyb, včetně pádů při práci s pamětí na macOS a problémů s obnovením relací po výpadcích.

**Why you'll care**
Claude Code je díky této verzi spolehlivější parťák, který vás nenechá ve štychu ani při komplikovanějších síťových operacích či dlouhých relacích.

Užívejte si kódování!

---

## Claude Code 2.1.318: Stability and authentication improvements 🚀

**TL;DR** — This release focuses on rock-solid stability, clearer authentication status, and smoother performance across shared network environments.

**⭐ Highlight of the release** — We’ve significantly improved how configuration files are handled on shared network drives, ensuring your settings and MCP servers stay synced and safe.

**What's new**
* **Auth clarity:** You’ll now get a heads-up warning when your claude.ai session is about to expire.
* **Effort control:** Added an `effort` option to fork tasks, allowing you to run quick side jobs with `low` effort.
* **Permission polish:** Agent permission policies are now more consistent, matching the behavior you expect from the Claude Console.
* **Bug squashing:** Resolved numerous issues, including memory stalls on macOS and session restoration bugs during cloud or remote connections.

**Why you'll care**
These fixes make Claude Code a much more dependable tool, especially if you work in complex environments, on network drives, or across multiple remote sessions.

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
