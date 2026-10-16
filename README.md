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

### Claude Code 2.1.301: Vylepšené Vim zkratky a stabilita 🚀 | Claude Code 2.1.301: Vim motions and LaTeX support 🚀

_Claude Code v2.1.301 — 2026-10-16_

## Claude Code 2.1.301: Vylepšené Vim zkratky a stabilita 🚀

**TL;DR** — Tato verze přináší podporu pro matematické zápisy v LaTeXu, vylepšení Vim režimu a opravu desítek drobných chyb pro plynulejší práci.

**⭐ Hlavní novinka**
Do Vim režimu jsme přidali pohyb `%`, který vám umožní okamžitě skákat mezi odpovídajícími závorkami – je to drobnost, která vám ušetří spoustu času při úpravě kódu.

**Co je nového**
* **LaTeX:** V VS Code nyní Claude vykresluje matematické vzorce (podpora `$$` i inline `$`).
* **Chytřejší UI:** Vylepšili jsme vykreslování dlouhých úkolů, takže se rozhraní nezpomaluje, když Claude usilovně přemýšlí.
* **Spolehlivost:** Opravili jsme chybu, kdy se binární soubory (např. .parquet nebo .epub) chybně četly jako text.
* **Lepší správa:** Claude nyní lépe zvládá přechod na modely s menším kontextovým oknem a automaticky je shrne, aby nedošlo ke ztrátě informací.

**Proč vás to zajímá**
Práce s kódem je nyní stabilnější, editor je svižnější a díky podpoře matematiky a lepšímu Vim režimu bude váš vývojářský workflow zase o něco přirozenější.

Užívejte si kódování a ať se daří!

---

## Claude Code 2.1.301: Vim motions and LaTeX support 🚀

**TL;DR** — This update brings LaTeX math rendering, Vim motion improvements, and a slew of stability fixes to make your coding sessions smoother.

**⭐ Highlight of the release**
We’ve added the `%` motion to Vim mode, letting you instantly jump between matching brackets—a small change that makes navigating complex code blocks feel much faster.

**What's new**
* **LaTeX Math:** Claude now renders beautiful math equations in VS Code responses using standard `$$` and `$` notation.
* **Better Performance:** Long-running tasks no longer cause the UI to stutter, as progress updates are now incremental rather than full-reloads.
* **Smarter Context:** Switching to a model with a smaller context window is now safer; Claude will summarize the conversation using the previous model before switching.
* **Binary Fixes:** The Read tool now correctly identifies and ignores binary files (like .epub or .parquet) instead of trying to read them as text.

**Why you'll care**
These updates resolve those annoying little friction points—like freezing UI or misread files—letting you stay in your flow state longer.

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
