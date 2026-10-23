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

### Claude Code 2.1.309: stabilita a lepší správa souborů 🛠️ | Claude Code 2.1.309: stability and polish 🛠️

_Claude Code v2.1.309 — 2026-10-23_

## Claude Code 2.1.309: stabilita a lepší správa souborů 🛠️

**TL;DR** — Tato aktualizace opravuje desítky chyb v sandboxu, vylepšuje práci se soubory a zpřesňuje chování v prostředí VS Code.

**⭐ Highlight of the release** — Kompletní revize zabezpečení sandboxu a Bash příkazů, která zajišťuje, že Claude Code vždy dodržuje nastavená omezení přístupu k souborům.

**What's new**
* **Opravy sandboxu:** Lepší izolace na macOS a Linuxu a oprava problémů se symbolickými odkazy.
* **Vylepšení VS Code:** Rychlejší úpravy kódu a lepší správa historie relací.
* **Git & Bash:** Chytřejší práce s repozitáři a oprava chybných oprávnění u složitých příkazů.
* **Claude API:** Rozšířené možnosti sledování (tracing) a lepší podpora pro OpenTelemetry.
* **Slack & Cloud:** Stabilnější propojení a oprava chyb při odesílání zpráv.

**Why you'll care**
Claude Code je nyní předvídatelnější, bezpečnější a v editoru VS Code mnohem svižnější. 

Užívejte si kódování s novou verzí!

---

## Claude Code 2.1.309: stability and polish 🛠️

**TL;DR** — This release squashes dozens of bugs across the sandbox, git operations, and VS Code extension to make your workflow smoother and more reliable.

**⭐ Highlight of the release** — A comprehensive hardening of sandbox and Bash command security, ensuring your file permissions and isolation rules are strictly enforced.

**What's new**
* **Sandbox fixes:** Robust fixes for macOS/Linux pathing, symlink handling, and background processes.
* **VS Code improvements:** Snappier edit performance and cleaner session history management.
* **Git & Bash:** Better handling of complex commands and improved git operations in worktrees.
* **Claude API:** Enhanced tracing support, including better OpenTelemetry integration.
* **Reliability:** Fixed various UI flickers, connection drops in cloud sessions, and Slack integration edge cases.

**Why you'll care**
Your coding sessions will feel more consistent, with fewer permission hiccups and a faster, more responsive chat panel in VS Code.

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
