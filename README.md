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

### Claude Code 2.1.312: Pohodlnější ovládání a opravené chyby 🚀 | Claude Code 2.1.312: Smoother workflows and fixes 🚀

_Claude Code v2.1.312 — 2026-10-28_

## Claude Code 2.1.312: Pohodlnější ovládání a opravené chyby 🚀

**TL;DR** — Nejnovější aktualizace přináší rychlejší odesílání zpráv, lepší stabilitu při úpravách velkých souborů a opravy mnoha nepříjemných chyb.

**⭐ Highlight of the release** — Nyní můžete odeslat zprávu okamžitě kliknutím na nápovědu „to send now“ přímo v rozhraní, což vám ušetří drahocenné sekundy.

**Co je nového**
* **Chytřejší úpravy:** Claude už nepřepisuje velké soubory, které celé neviděl – nyní si je raději celé načte.
* **Lepší přehled:** V cloudových relacích uvidíte jasnější přehled o tom, co se stalo při přidávání repozitářů, místo surových dat.
* **Stabilita:** Opravili jsme chyby při navigaci v terminálu, zobrazení stavu relací a náhodné pády při čtení PDF.
* **Vylepšení pro VS Code:** Jasnější informace o limitech využití a přehlednější chybové hlášky při přihlašování.

**Proč vás to bude zajímat** — Tato verze dělá z Claude Code spolehlivějšího parťáka, který vás nebude vyrušovat chybami a lépe rozumí vašim souborům i limitům.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.312: Smoother workflows and fixes 🚀

**TL;DR** — This release introduces instant message sending, smarter file handling, and a suite of stability improvements for your daily workflow.

**⭐ Highlight of the release** — You can now send queued messages instantly by clicking the "to send now" hint, making your interaction feel much snappier.

**What's new**
* **Smarter file editing:** Claude now avoids overwriting large files it hasn't fully read, opting to read the whole file or edit in place instead.
* **Better cloud visibility:** Repository setup steps in cloud sessions now show a clean table instead of raw JSON data.
* **Stability fixes:** Resolved issues with directory navigation in Git, PDF reading failures, and session state persistence.
* **VS Code & UI polish:** Clearer "5-hour limit" messaging, better error handling for organization settings, and more helpful retry prompts.

**Why you'll care** — We’ve ironed out the friction points that get in your way, ensuring Claude stays focused on your code rather than struggling with file size or session state.

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
