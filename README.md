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

### Nová verze Claude Code 2.1.325 je tady! 🚀 | Claude Code 2.1.325 is here! 🚀

_Claude Code v2.1.325 — 2026-11-14_

## Nová verze Claude Code 2.1.325 je tady! 🚀

**TL;DR** – Tato aktualizace přináší vylepšení bezpečnosti, hladší práci s Jupyter notebooky a lepší přehlednost v terminálu.

**⭐ Highlight of the release**
Nyní vás Claude Code chytře navede, co dělat, když vaše organizace zablokuje požadavek – stačí použít `/rewind` pro změnu zprávy nebo `/clear` pro nový start.

**What's new**
* **Lepší terminál:** V VS Code uvidíte tipy pro opakování buněk v Jupyter noteboocích.
* **Bezpečnost:** Oprava chyby při dekódování komprimovaných odpovědí a přísnější pravidla pro sandbox.
* **Stabilita:** Opraveno mnoho chyb při obnovování relací, práci v repozitářích a spouštění na Windows/Linuxu.
* **Chytřejší nápověda:** Claude nyní lépe vysvětluje, proč vyžaduje oprávnění nebo proč byla akce zamítnuta.

**Why you'll care**
Claude Code je díky těmto opravám stabilnější, bezpečnější a méně vás bude zdržovat při řešení konfiguračních zádrhelů.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.325 is here! 🚀

**TL;DR** – This update brings security fixes, smoother Jupyter notebook workflows, and better guidance when you hit policy roadblocks.

**⭐ Highlight of the release**
When your organization's policy blocks a request, Claude Code now provides clear instructions: simply run `/rewind` to adjust your message or `/clear` to start fresh.

**What's new**
* **VS Code improvements:** New spinner tips for re-running Jupyter notebook cells after edits.
* **Security:** Fixed a vulnerability in zstd-compressed response decoding and tightened sandbox protections.
* **Stability:** Numerous fixes for session resumption, worktree git commands, and platform-specific issues on Windows and Linux.
* **Better transparency:** Clearer explanations when Claude needs permission or when a tool call is restricted by policy.

**Why you'll care**
This release focuses on removing friction, ensuring your sessions are more reliable, and helping you navigate permissions without the guesswork.

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
