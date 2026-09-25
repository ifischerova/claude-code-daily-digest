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

### Claude Code 2.1.282: Vylepšená stabilita a opravy 🛠️ | Claude Code 2.1.282: Stability and polish 🛠️

_Claude Code v2.1.282 — 2026-09-25_

## Claude Code 2.1.282: Vylepšená stabilita a opravy 🛠️

**TL;DR** — Tato verze přináší desítky oprav chyb, vylepšení stability rozhraní a hladší integraci s nástroji třetích stran.

**⭐ Highlight of the release** — Výrazné zlepšení odolnosti relací; Claude nyní lépe zvládá přerušení, výpadky databází a automaticky opravuje chyby v historii konverzací, aby vás nic nezastavilo v práci.

**What's new**
* **Lepší čitelnost:** Nové nastavení `maxProseWidth` omezuje šířku textu v terminálu, zatímco tabulky a kód zůstávají přes celou obrazovku.
* **Stabilita:** Opraveny chyby při obnovování relací (`--continue`, `--resume`) a problémy s výpadky během dlouhých operací.
* **Vim režim:** Kompletně opraveny chyby v navigaci a editaci (např. chyby při mazání řádků nebo vkládání textu).
* **Cloud & Slack:** Vylepšená správa GitHub repozitářů a přesnější notifikace v Slacku.
* **Bezpečnost:** Lepší správa oprávnění a transparentnější upozornění, pokud jsou některé proměnné ignorovány kvůli nastavení organizace.

**Why you'll care** — Všechno prostě funguje spolehlivěji – od terminálového rozhraní až po složité příkazy. Claude nyní lépe respektuje váš pracovní prostor a zbytečně vás neobtěžuje chybovými hláškami.

Užívejte si hladší kódování!

---

## Claude Code 2.1.282: Stability and polish 🛠️

**TL;DR** — This release is packed with dozens of bug fixes, UI refinements, and improved stability for long-running sessions.

**⭐ Highlight of the release** — Enhanced session resilience: Claude now handles database failovers, connection drops, and history corruption gracefully, ensuring your work isn't interrupted by transient errors.

**What's new**
* **Better readability:** Added `maxProseWidth` to cap prose width in wide terminals while keeping code blocks and tables full-width.
* **Reliability:** Fixed issues where resuming sessions (`--continue`, `--resume`) would inadvertently drop context or trigger API errors.
* **Vim mode:** Squashed bugs related to line joining, cursor placement, and repeating commands.
* **Cloud & Slack:** Smoother repository management and better synchronization for enterprise Slack workspaces.
* **Settings:** Improved transparency when managed settings or security policies override local configurations.

**Why you'll care** — Everything just feels more solid. From the terminal layout to the way Claude handles complex tasks, this update removes the friction that occasionally gets in the way of your flow.

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
