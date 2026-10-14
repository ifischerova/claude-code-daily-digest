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

### Claude Code 2.1.299: Chytřejší paměť a lepší kontrola 🚀 | Claude Code 2.1.299: Smarter memory and better control 🚀

_Claude Code v2.1.299 — 2026-10-14_

## Claude Code 2.1.299: Chytřejší paměť a lepší kontrola 🚀

**TL;DR** — Tato verze přináší efektivnější správu paměti (kompakci), lepší zabezpečení a spoustu oprav pro hladší vývoj.

**⭐ Highlight of the release** — Automatická kompakce konverzace: Pokud necháte relaci s více než 200 tisíci tokeny nečinnou déle než 54 minut, Claude ji nyní automaticky zkomprimuje. Ušetříte tak čas i tokeny při příštím dotazu, protože se nebude muset znovu zpracovávat celá historie.

**What's new**
* **Chytřejší soubory:** Pomocí `CLAUDE_CODE_DISABLE_FILE_MENTIONS` můžete nastavit, aby Claude viděl cesty k souborům, ale nečetl jejich obsah.
* **Rychlejší start:** V agentním zobrazení nyní můžete použít `/fast` nebo `/effort` pro nastavení preferencí relace.
* **Bezpečí na prvním místě:** Opravena řada bezpečnostních chyb v izolovaném prostředí (sandboxu) a přidán „safe mode“ pro background relace.
* **Lepší ovládání:** Nové příkazy pro vypnutí (drain), vylepšené varování o využití limitů a podrobnější informace pro autory pluginů.
* **Opravy:** Desítky vylepšení stability pro VS Code, cloudové relace a vzdálené ovládání.

**Why you'll care** — Vaše relace budou nyní stabilnější, méně „hladové“ po paměti a díky lepšímu zabezpečení sandboxu můžete pracovat s ještě větším klidem.

Šťastné kódování!

---

## Claude Code 2.1.299: Smarter memory and better control 🚀

**TL;DR** — This release introduces automatic conversation compaction, enhanced security, and a massive list of stability improvements for a smoother workflow.

**⭐ Highlight of the release** — Idle conversation compaction: Conversations with over 200K tokens that sit idle for 54 minutes will now be automatically compacted. This prevents your next message from triggering a massive re-processing of your prompt cache.

**What's new**
* **File mentions:** Use `CLAUDE_CODE_DISABLE_FILE_MENTIONS` to allow Claude to see file paths without reading their contents.
* **Faster workflow:** You can now use `/fast` or `/effort` in the agent view to set session preferences instantly.
* **Security hardening:** Numerous fixes for sandbox isolation and a clearer "safe mode" indicator for background tasks.
* **Better control:** Added `--shutdown-drain-sec` for graceful runner shutdowns and improved usage warnings for max effort and context limits.
* **Quality of life:** Dozens of fixes for VS Code integration, cloud session memory spikes, and remote control reliability.

**Why you'll care** — Your sessions will be more memory-efficient and stable, and the updated sandbox rules mean you can work with greater confidence.

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
