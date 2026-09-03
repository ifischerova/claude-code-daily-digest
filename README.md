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

### Claude Code 2.1.259: Stabilnější a chytřejší 🚀 | Claude Code 2.1.259: Better team management and stability 🚀

_Claude Code v2.1.259 — 2026-09-03_

## Claude Code 2.1.259: Stabilnější a chytřejší 🚀

**TL;DR** — Tato verze přináší lepší správu pro týmy, stabilnější relace a opravu mnoha drobných chyb.

**⭐ Highlight of the release** — Administrátoři mohou nyní centrálně spravovat MCP servery pro celý tým, což usnadňuje nastavení prostředí pro všechny kolegy.

**What's new**
* **Headless režim:** Přidán tichý režim `--permission-prompts none` pro automatizované servery.
* **GitLab podpora:** Claude nyní lépe rozumí GitLab merge requestům a zobrazuje jejich stav přímo v rozhraní.
* **Stabilita:** Opraveny problémy s přepisováním konfigurace při více běžících relacích.
* **Lepší přehled:** Výsledky pracovních postupů (workflows) jsou nyní čitelnější díky formátování JSON a možnosti skrýt dlouhé výstupy.
* **VS Code:** V postranním panelu relací nyní můžete filtrovat podle stavu (např. „Čeká na vstup“).

**Why you'll care**
Claude Code je nyní spolehlivějším parťákem pro práci v týmu i pro automatizované skripty, aniž byste se museli bát ztráty nastavení nebo přerušení práce.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.259: Better team management and stability 🚀

**TL;DR** — This release brings improved enterprise configuration, rock-solid session stability, and a polished experience for GitLab users.

**⭐ Highlight of the release** — You can now centrally manage MCP servers for your entire organization, ensuring everyone has the tools they need without manual setup.

**What's new**
* **Headless Mode:** Added `--permission-prompts none` to automatically deny prompts on unattended hosts.
* **GitLab Integration:** Claude now recognizes GitLab merge requests, showing status updates directly in the footer.
* **Reliability:** Fixed issues where concurrent sessions would accidentally overwrite each other’s configuration files.
* **Better Visibility:** Workflow outcomes are now pretty-printed with syntax highlighting and collapsible sections for long logs.
* **VS Code:** Added handy status filters (Needs input, Working, Completed) to the session sidebar.

**Why you'll care**
These updates make Claude Code much more robust for collaborative environments and automated pipelines, saving you from fighting with configuration conflicts or hidden errors.

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
