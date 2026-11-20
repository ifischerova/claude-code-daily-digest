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

### Claude Code 2.1.329 je tady: stabilita a vylepšený Code Mode 🛠️ | Claude Code 2.1.329: Performance and stability boost 🛠️

_Claude Code v2.1.329 — 2026-11-20_

## Claude Code 2.1.329 je tady: stabilita a vylepšený Code Mode 🛠️

**TL;DR** — Tato aktualizace přináší zásadní opravy stability, lepší správu paměti v Code Mode a plynulejší práci v VS Code.

**⭐ Highlight of the release** — Vylepšili jsme Code Mode, který je nyní mnohem odolnější: lépe zvládá velké objemy dat, efektivněji využívá paměť a skripty se díky novým limitům nezacyklí.

**What's new**
* **Lepší přehled o úkolech:** Příkaz `/tasks` nyní přehledně zobrazuje vše od naplánovaných úloh až po aktivní forky.
* **Robustnější VS Code:** Opravili jsme zasekávání při psaní, problémy s klávesovými zkratkami a lepší práci s uživatelskými vstupy (IME).
* **Vylepšená diagnostika:** Pokud se MCP server nepřipojí, uvidíte přímo konkrétní chybovou hlášku, místo aby se jen „nic nestalo“.
* **Bezpečnější soubory:** Opravili jsme chybu, kdy se u některých souborů (PDF, obrázky) při přenosu přes MCP ztrácela jejich správná identifikace.

**Why you'll care**
Claude Code je nyní stabilnější, rychlejší a méně „hladový“ po paměti, což oceníte hlavně při dlouhých relacích a práci na složitějších projektech.

Užijte si kódování s Claude!

---

## Claude Code 2.1.329: Performance and stability boost 🛠️

**TL;DR** — This release focuses on rock-solid stability, major memory management improvements for Code Mode, and a smoother VS Code experience.

**⭐ Highlight of the release** — Code Mode is now much more robust; it handles large file reads and script execution with better memory safety and smarter limits to prevent runaway loops.

**What's new**
* **Task Clarity:** The `/tasks` command now gives you a unified view of scheduled tasks, active forks, and background loops.
* **VS Code Polish:** Fixed annoying focus issues with input methods (IME), corrected keybinding glitches, and improved how permission prompts behave.
* **Better MCP Debugging:** You’ll now see actual JSON-RPC error messages when an HTTP MCP server refuses a connection.
* **File Integrity:** Fixed issues where certain file types (like PDFs or images) were mislabeled as binary data during MCP transfers.

**Why you'll care**
Your sessions will feel snappier and more reliable, especially during long coding sessions where memory usage used to be a pain point.

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
