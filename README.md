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

### Claude Code 2.1.268: Rychlejší, plynulejší a chytřejší 🚀 | Claude Code 2.1.268: Smoother, faster, and more reliable 🚀

_Claude Code v2.1.268 — 2026-09-11_

## Claude Code 2.1.268: Rychlejší, plynulejší a chytřejší 🚀

**TL;DR** — Tato aktualizace přináší zásadní vylepšení výkonu, opravy chyb v oprávněních a plynulejší práci s pluginy i v rozšíření pro VS Code.

**⭐ Highlight of the release** — Pluginy nyní fungují okamžitě: instalace, aktivace či deaktivace se projeví v běžících relacích bez nutnosti restartu.

**Co je nového**
* **Lepší správa:** Správci mohou nyní využít `gatewayInternalNetworks` pro bezpečný přístup k bráně z interních sítí.
* **Plynulejší práce:** Opravili jsme chyby způsobující vysoké vytížení CPU a zrychlili načítání při obnovování konverzací.
* **Přehlednější pluginy:** Příkaz `claude plugin` nyní podporuje `--json` pro snadnější automatizaci.
* **Chytřejší oprávnění:** Claude nyní lépe vysvětluje, proč zablokoval určitou akci, a nabízí bezpečnější alternativy.
* **VS Code:** Opraveny problémy s nekonzistentním zobrazením modelů a vylepšeno ovládání pomocí klávesnice.

**Proč vás to zajímá**
Claude Code je nyní stabilnější a méně vás vyrušuje při práci – vše od pluginů až po obnovu relací funguje přesně tak, jak byste čekali.

Užívejte si kódování bez zbytečných zádrhelů!

---

## Claude Code 2.1.268: Smoother, faster, and more reliable 🚀

**TL;DR** — This release brings major performance optimizations, refined permission handling, and a much smoother experience for plugins and VS Code users.

**⭐ Highlight of the release** — Plugin changes (installs, enables, and disables) now take effect in open sessions instantly—no more `/reload-plugins` required.

**What's new**
* **Gateway control:** Added `gatewayInternalNetworks` to let admins allow login access from specific public IPv4 blocks.
* **Performance:** Fixed high CPU usage in idle sessions and optimized startup times for projects with many workflow scripts.
* **Better feedback:** Claude now explains exactly which rule blocked an action and suggests safer alternatives.
* **Plugin automation:** Added `--json` output support for all plugin management commands.
* **VS Code improvements:** Fixed model picker glitches, improved keyboard navigation, and ensured session settings persist correctly.

**Why you'll care**
Your workflow will feel snappier and more intuitive, with fewer manual restarts and clearer guidance when permissions get in the way.

Happy coding, and let us know what you think!

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
