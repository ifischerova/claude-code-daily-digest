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

### Claude Code 2.1.296: Vylepšená správa agentů a vyšší stabilita 🛠️ | Claude Code 2.1.296: Better agent control and stability 🛠️

_Claude Code v2.1.296 — 2026-10-10_

## Claude Code 2.1.296: Vylepšená správa agentů a vyšší stabilita 🛠️

**TL;DR** — Tato verze přináší lepší kontrolu nad agenty, opravuje desítky chyb a zlevňuje práci s modelem Sonnet 5.5.

**⭐ Hlavní novinka**
Nyní můžete využít `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` pro přiřazení specifického modelu konkrétním workflow agentům, což vám dává mnohem větší kontrolu nad tím, který mozek na daném úkolu zrovna pracuje.

**Co je nového**
* **Flexibilnější agenti:** Přidali jsme `autoCompactWindow` pro rychlejší čištění paměti u podagentů a možnost číst rozsáhlé soubory pomocí `allow_large`.
* **Lepší správa:** Opravili jsme desítky drobných chyb v pluginech, přihlašování přes brány (gateways) a chování v terminálech.
* **Zlevnění:** Snížili jsme cenu za cache čtení u modelu Sonnet 5.5 na polovinu ($0.10 za milion tokenů).
* **Vylepšení pro Windows:** PowerShell nyní zvládne delší příkazy a instalace pluginů přes GitHub je spolehlivější.

**Proč vás to zajímá**
Claude Code je zase o kus stabilnější, rychlejší a lépe se přizpůsobí vašemu pracovnímu prostředí, ať už pracujete na Windows, nebo v cloudu.

Užívejte si kódování s novou verzí!

---

## Claude Code 2.1.296: Better agent control and stability 🛠️

**TL;DR** — This release adds powerful new agent configuration options, fixes dozens of edge cases, and lowers the cost of Sonnet 5.5 cache reads.

**⭐ Highlight of the release**
You can now use the `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` environment variable to pin specific models to your workflow agents, giving you fine-grained control over which model handles which part of your task.

**What's new**
* **Smarter Agents:** Added `autoCompactWindow` for subagents to manage memory better and an `allow_large` option for the Read tool to process big files in one go.
* **Fixes Galore:** Resolved various issues with plugin hooks, gateway sign-ins, and terminal display artifacts.
* **Cost Reduction:** Sonnet 5.5 cache reads are now 50% cheaper, down to $0.10 per million tokens.
* **Windows Polish:** Improved PowerShell command limits and made GitHub plugin installations more robust.

**Why you'll care**
This update makes Claude Code more predictable and reliable, especially in complex environments with multiple plugins or custom workflow requirements.

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
