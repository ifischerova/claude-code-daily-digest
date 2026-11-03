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

### Claude Code 2.1.317: Lepší zabezpečení a hladší správa úloh 🚀 | Claude Code 2.1.317: Enhanced security and smoother workflows 🚀

_Claude Code v2.1.317 — 2026-11-03_

## Claude Code 2.1.317: Lepší zabezpečení a hladší správa úloh 🚀

**TL;DR** — Tato aktualizace přináší důležitá vylepšení zabezpečení, přesnější správu nákladů pro týmy a opravu desítek drobných chyb pro stabilnější chod.

**⭐ Hlavní novinka**
Nyní vás Claude Code vždy upozorní, pokud se nějaký nástroj (webový nebo shell) pokusí odeslat vaši e-mailovou adresu do sítě, a přidali jsme přehledné reporty nákladů pro správce přímo v API.

**Co je nového**
* **Bezpečí na prvním místě:** Lepší kontrola nad připojenými úlohami a jasnější varování při sdílení citlivých údajů.
* **Správa týmu:** Správci mají nyní detailní přehled o útratě (podle vývojářů nebo skupin) a lepší nástroje pro práci s identitou.
* **Stabilita:** Opravili jsme desítky chyb, včetně problémů s odpojováním MCP serverů, zasekáváním v režimu „auto“ a problémů s dlouhými konverzacemi.
* **Vylepšení pro VS Code:** Soubory se nyní otevírají v novém okně místo překrývání chatu a rozhraní lépe reaguje na změnu velikosti písma.

**Proč vás to zajímá**
Claude Code je díky těmto změnám bezpečnější pro firemní nasazení a mnohem spolehlivější při každodenním programování bez zbytečných přerušení.

Ať se vám dnes kód píše jedna báseň!

---

## Claude Code 2.1.317: Enhanced security and smoother workflows 🚀

**TL;DR** — This update introduces vital security checks, better cost transparency for teams, and dozens of fixes to make your development sessions more stable.

**⭐ Highlight of the release**
We’ve added proactive security prompts that ask for permission before any web or shell tool sends your email address across the network, keeping your data strictly under your control.

**What's new**
* **Security & Privacy:** New warnings for scheduled tasks and clearer handling of network-blocked regions.
* **Admin Insights:** A new cost reporting API allows admins to track spend by developer, day, or group with ease.
* **Stability:** Squashed dozens of bugs, including MCP server disconnects, auto-mode failures, and issues with long-running sessions.
* **VS Code Polish:** File links now open in their own editor groups, and the UI handles custom font sizes much more gracefully.

**Why you'll care**
These updates make Claude Code significantly more robust for team environments and ensure your long coding sessions stay uninterrupted and secure.

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
