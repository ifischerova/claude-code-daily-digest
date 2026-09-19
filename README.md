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

### Chytřejší a úspornější automatický režim 🚀 | Smarter and more cost-effective auto mode 🚀

_Claude Code v2.1.278 — 2026-09-19_

## Chytřejší a úspornější automatický režim 🚀

**TL;DR**
Automatický režim je nyní efektivnější díky přesunu klasifikátoru na stranu serveru, což šetří vaše náklady.

**⭐ Hlavní novinka**
Claude Code nyní standardně využívá serverový klasifikátor pro automatický režim, takže za jeho provoz už neplatíte žádné poplatky navíc.

**Co je nového**
*   Automatický režim pro API, Enterprise, Bedrock, Vertex a Foundry nyní automaticky využívá bezplatný serverový klasifikátor.
*   V příkazu `/status` najdete nový řádek „Auto mode server“, který vám vždy ukáže, zda klasifikátor běží na serveru.
*   Pokud by došlo k problému a systém musel přepnout na placenou variantu, včas vás na to upozorníme.

**Proč vás to zajímá**
Vaše automatizace bude nyní levnější a díky novému indikátoru ve statusu máte vždy přehled o tom, jak vaše náklady vznikají.

Ať se vám dnes skvěle kóduje!

---

## Smarter and more cost-effective auto mode 🚀

**TL;DR**
Auto mode is now more efficient by defaulting to a server-side classifier, eliminating extra overhead costs.

**⭐ Highlight of the release**
Claude Code now defaults to using a server-side classifier for auto mode, meaning you won't be charged for classifier overhead.

**What's new**
*   Auto mode for API, Enterprise, Bedrock, Vertex, and Foundry now uses the server-side classifier by default.
*   A new "Auto mode server" row in the `/status` command lets you see exactly how your session is being handled.
*   The system will provide a warning if it ever needs to fall back to a billed classifier model.

**Why you'll care**
Your automated workflows are now more budget-friendly, and you have full transparency into your session costs via the status command.

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
