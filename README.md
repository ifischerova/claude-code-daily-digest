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

### Claude Code 2.1.274: Hladší, rychlejší a spolehlivější 🚀 | Claude Code 2.1.274: Smoother, faster, and more reliable 🚀

_Claude Code v2.1.274 — 2026-09-17_

## Claude Code 2.1.274: Hladší, rychlejší a spolehlivější 🚀

**TL;DR** — Tato aktualizace přináší desítky oprav stability, vylepšené propojení s MCP servery a chytřejší chování v VS Code.

**⭐ Highlight of the release** — Claude nyní lépe zvládá kritické situace: pokud vám dochází paměť, dostanete jasné varování s návodem, jak situaci vyřešit, aniž byste přišli o rozdělanou práci.

**What's new**
* **VS Code:** Snadnější přístup k paměti a instrukcím přímo z menu a automatické pokračování v práci po restartu okna.
* **Stabilita MCP:** Opravili jsme zasekávání při chybách a vylepšili připojování k serverům, které používají starší formáty.
* **Chytřejší Claude:** Claude nyní lépe chápe kontext po obnovení relace a efektivněji spravuje úkoly na pozadí.
* **Vylepšená komunikace:** Opravili jsme formátování seznamů v chatu a přidali možnost rozbalit zprávy kolegů v režimu celé obrazovky.

**Why you'll care** — Váš vývojářský workflow bude méně přerušovaný a Claude bude lépe reagovat na vaše potřeby v prostředí, na které jste zvyklí.

Užijte si kódování s novým, stabilnějším Claudem!

---

## Claude Code 2.1.274: Smoother, faster, and more reliable 🚀

**TL;DR** — This release brings dozens of stability fixes, improved MCP server connectivity, and a much more polished VS Code experience.

**⭐ Highlight of the release** — We’ve added proactive memory management: Claude will now warn you when system memory is critical and provide clear steps to free it up or restart safely, preventing crashes.

**What's new**
* **VS Code:** Added quick access to memory settings and project instructions in the Customize menu, plus automatic session resumption after window reloads.
* **MCP Robustness:** Fixed various connection loops and timeout issues, ensuring your tools work reliably even with legacy servers.
* **Smarter Context:** Claude now maintains goals and background tasks better when resuming sessions or switching models.
* **Better UX:** Fixed chat formatting glitches (like renumbered lists) and added click-to-expand functionality for messages in fullscreen mode.

**Why you'll care** — You'll spend less time troubleshooting the tool and more time building, with a much more stable experience across VS Code, the web, and Slack.

Happy coding with this more robust Claude!

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
