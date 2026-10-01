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

### Claude Code 2.1.286: Vylepšená navigace a stabilita 🚀 | Claude Code 2.1.286: Smoother navigation and stability 🚀

_Claude Code v2.1.286 — 2026-10-01_

## Claude Code 2.1.286: Vylepšená navigace a stabilita 🚀

**TL;DR** – Tato aktualizace přináší desítky oprav stability, vylepšené ovládání rozhraní a nové funkce pro uživatele VS Code.

**⭐ Highlight of the release** – Kompletně přepracované seznamy v režimu celé obrazovky nyní podporují myš, obsahují přehledné posuvníky a umožňují rychlejší navigaci v dlouhých výstupech.

**What's new**
* **Lepší přehled:** Permission prompty jsou nyní přehlednější a jasně ukazují pořadí požadavků.
* **Stabilita:** Opravili jsme chyby při obnovování relací a pády způsobené neplatným formátem dat z nástrojů.
* **VS Code novinky:** Přidali jsme záložky pro důležité odpovědi a vylepšili zobrazení otázek a odpovědí v chatu.
* **Inteligentnější retries:** Claude nyní při selhání modelu automaticky zkusí alternativu, místo aby ukončil celou konverzaci.
* **Čistší rozhraní:** Vylepšené našeptávání příkazů a přehlednější správa pluginů.

**Why you'll care**
Claude Code je nyní mnohem stabilnější při dlouhých relacích a díky novým prvkům v UI se v něm lépe zorientujete, i když pracujete na složitých úkolech.

Užívejte si kódování s novou verzí!

---

## Claude Code 2.1.286: Smoother navigation and stability 🚀

**TL;DR** – This update delivers dozens of stability fixes, refined UI controls, and powerful new features for the VS Code extension.

**⭐ Highlight of the release** – Fullscreen lists are now fully mouse-navigable with improved scrollbars and intuitive "N more" row handling for a much smoother experience.

**What's new**
* **Clearer Permissions:** Permission prompts now show a progress count, so you always know where you are in a stack of requests.
* **Rock-solid Sessions:** Fixed several bugs that caused session loss during crashes, API errors, or when resuming from a cloud state.
* **VS Code Enhancements:** Added a Bookmarks panel to save key responses and improved the chat view to clearly show your interaction history with questions.
* **Smarter Fallbacks:** Claude now automatically retries with a different model if your preferred one hits an API issue, keeping your flow uninterrupted.
* **Polished UI:** Slash command suggestions are snappier, and list screens are now consistently formatted for better readability.

**Why you'll care**
Whether you're managing complex background agents or just performing a quick task, these improvements make your workflow feel more reliable and significantly easier to navigate.

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
