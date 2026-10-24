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

### Claude Code 2.1.310: Vylepšené cloudové relace a stabilita 🚀 | Claude Code 2.1.310: Better cloud sessions and stability 🚀

_Claude Code v2.1.310 — 2026-10-24_

## Claude Code 2.1.310: Vylepšené cloudové relace a stabilita 🚀

**TL;DR** — Tato aktualizace přináší lepší správu cloudových relací, opravy stability a přehlednější ovládání pro uživatele VS Code.

**⭐ Hlavní novinka** — Rozšířená správa přístupů: majitelé Enterprise účtů nyní mohou ovládat cloudové relace a vzdálené ovládání pomocí vlastních rolí.

**Co je nového**
* **Cloudové relace:** Snadnější načítání skriptů, přehlednější nastavení a lepší správa chybových hlášení.
* **Stabilita:** Claude Code je nyní chytřejší při komunikaci přes brány, které odmítají určité beta parametry.
* **Vylepšení pro VS Code:** Opraveny chyby v rozhraní pro zpětnou vazbu a přepínání větví.
* **Linux a Windows:** Lepší diagnostika omezení systému (AppArmor) a oprava oprávnění v Git Bash.
* **Claude Tag:** Oprava zpracování příkazů, které byly formátovány tučně nebo kurzívou.

**Proč na tom záleží** — Vaše pracovní prostředí bude spolehlivější a bezpečnější, a to zejména v týmových a cloudových scénářích.

Užívejte si kódování s novou verzí!

---

## Claude Code 2.1.310: Better cloud sessions and stability 🚀

**TL;DR** — This update brings robust improvements to cloud session management, better system compatibility, and smoother VS Code integration.

**⭐ Highlight of the release** — Enhanced Enterprise control: Owners can now assign granular permissions for cloud sessions and remote control to specific custom roles.

**What's new**
* **Cloud Sessions:** Simplified environment setup with file uploads for scripts and a cleaner UI for managing network and variable settings.
* **Reliability:** Improved handling of network gateways that reject specific beta parameters, preventing unnecessary request failures.
* **VS Code:** Fixed UI bugs in the feedback loop and branch switching workflows.
* **OS Fixes:** Better diagnostic messages for Linux sandbox issues and resolved permission hook bugs on Windows.
* **Claude Tag:** Fixed formatting issues where command triggers were being ignored when styled with bold or italics.

**Why you'll care** — You’ll spend less time troubleshooting environment quirks and more time building with a more stable, enterprise-ready tool.

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
