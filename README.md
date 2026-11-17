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

### Claude Code 2.1.326: Vylepšená práce s agenty a stabilita 🚀 | Claude Code 2.1.326: Agent team improvements and stability 🚀

_Claude Code v2.1.326 — 2026-11-17_

## Claude Code 2.1.326: Vylepšená práce s agenty a stabilita 🚀

**TL;DR** — Tato aktualizace přináší lepší podporu pro týmy agentů, vyšší bezpečnost v sandboxu a desítky oprav pro plynulejší zážitek v terminálu i VS Code.

**⭐ Highlight of the release** — Nyní můžete aktivovat „Code Mode“ i při zapnutých týmech agentů, což umožňuje plynulejší přechod mezi psaním kódu a kooperací s ostatními agenty.

**What's new**
* **Chytřejší zabezpečení:** Přidali jsme varování při neúplných pravidlech nástrojů a vylepšili ochranu v Bash sandboxu.
* **Lepší přehled:** Příkaz `/status` nyní jasně ukazuje, proč jsou některé funkce (např. telemetrie) vypnuté.
* **Stabilita:** Opravili jsme desítky drobných chyb, od zasekávání obrazovky při dlouhých výstupech až po problémy s obnovou historie konverzace.
* **VS Code:** Vylepšili jsme rychlost úprav kódu a opravili chyby v přihlašování a správě paměti.

**Why you'll care** — Váš pracovní postup bude méně přerušovaný díky spolehlivějšímu sandboxu a lepším informacím o tom, co se „pod kapotou“ právě děje.

Ať se vám dnes dobře kóduje!

---

## Claude Code 2.1.326: Agent team improvements and stability 🚀

**TL;DR** — This release brings better support for agent teams, strengthened sandbox security, and dozens of fixes for a smoother experience in the terminal and VS Code.

**⭐ Highlight of the release** — You can now enable "Code Mode" while agent teams are active, allowing for a more seamless transition between coding and multi-agent collaboration.

**What's new**
* **Smarter Security:** Added startup warnings for incomplete tool rules and improved Bash sandbox protections across all platforms.
* **Better Visibility:** The `/status` command now explicitly explains why specific features (like telemetry) might be disabled.
* **Stability:** Squashed dozens of bugs ranging from screen freezes during long outputs to history loss during session resumes.
* **VS Code:** Improved Edit/Write performance and fixed recurring issues with sign-in flows and memory management.

**Why you'll care** — Your workflow will be less interrupted thanks to a more robust sandbox and clearer feedback on what's happening under the hood.

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
