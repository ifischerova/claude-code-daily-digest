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

### Claude Code 2.1.289: stabilnější a spolehlivější pluginy 🛠️ | Claude Code 2.1.289: smoother plugins and better stability 🛠️

_Claude Code v2.1.289 — 2026-10-04_

## Claude Code 2.1.289: stabilnější a spolehlivější pluginy 🛠️

**TL;DR** — Tato aktualizace opravuje řadu chyb v pluginech, vylepšuje stabilitu terminálu a zpřesňuje pravidla pro zabezpečení.

**⭐ Highlight of the release** — Výrazně jsme zlepšili odolnost pluginů: chyby v jednom modulu už neshodí celé zobrazení, ale ohlásí se lokálně, což udržuje vaši práci v chodu.

**What's new**
- **Stabilita:** Opravili jsme zamrzání terminálu při práci s komplexním kódem a tagy.
- **Pluginy:** Vyřešili jsme problémy s načítáním lokálních pluginů, jejich aktualizací a chybným vykreslováním v panelech.
- **Zabezpečení:** Pravidla pro čtení souborů a vykonávání příkazů (Bash) nyní lépe respektují symlinky a proměnné prostředí.
- **Vývojářské nástroje:** Přidali jsme `agent.spawn` a vylepšili validaci pluginů.

**Why you'll care** — Váš pracovní prostor bude nyní mnohem předvídatelnější, pluginy se vám nebudou „rozpadat“ a bezpečnostní pravidla budou fungovat přesně tak, jak mají.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.289: smoother plugins and better stability 🛠️

**TL;DR** — This release squashes a long list of plugin rendering bugs, fixes terminal freezes, and tightens up security rule enforcement.

**⭐ Highlight of the release** — Plugins are now much more resilient: if a module fails to render, it now fails gracefully on its own rather than taking down the entire UI.

**What's new**
- **Stability:** Fixed terminal freezes caused by complex code blocks or unclosed script tags.
- **Plugins:** Resolved issues with stale plugin loading, local marketplace syncing, and rendering glitches in side panes.
- **Security:** Bash deny/ask rules are now correctly applied even when environment variables or symlinks are involved.
- **Developer Experience:** Added `agent.spawn` for better team collaboration and improved `claude plugin validate` reliability.

**Why you'll care** — You'll spend less time troubleshooting UI glitches or unexpected crashes and more time letting Claude help you build.

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
