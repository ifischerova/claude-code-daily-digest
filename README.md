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

### Claude Code 2.1.300: Vylepšená stabilita a nové možnosti pro vývojáře 🛠️ | Claude Code 2.1.300: Improved stability and power-user features 🛠️

_Claude Code v2.1.300 — 2026-10-15_

## Claude Code 2.1.300: Vylepšená stabilita a nové možnosti pro vývojáře 🛠️

**TL;DR** — Tato aktualizace přináší desítky oprav stability, lepší podporu pro mody a plynulejší spolupráci v rámci Claude Desktop a VS Code.

**⭐ Hlavní novinka**
Nová podpora pro `/advisor` v prostředí AWS, která vám dává větší kontrolu nad tím, jak a kdy vám Claude poskytuje rady při programování.

**Co je nového**
*   **Flexibilnější mody:** Přidali jsme nové nástroje pro úpravu vzhledu a interakci (např. `virtualText` nebo zobrazení historie agenta).
*   **Vylepšené VS Code:** Opravili jsme desítky drobností, včetně přesnějšího vkládání souborů a lepšího zobrazení diffů.
*   **Lepší správa agentů:** Agenti jsou nyní stabilnější při obnovení relace a lépe si pamatují kontext i po restartu.
*   **Chytřejší Slack:** Claude v Slacku nyní lépe rozumí hlasovým zprávám a podporuje sdílené kanály (Slack Connect).

**Proč by vás to mělo zajímat**
S touto verzí je Claude Code zase o kus spolehlivějším parťákem, který méně často „zapomíná“ kontext a lépe spolupracuje s vaším editorem i cloudovými nástroji.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.300: Improved stability and power-user features 🛠️

**TL;DR** — This release is packed with stability fixes, enhanced modding capabilities, and a smoother experience across VS Code and cloud sessions.

**⭐ Highlight of the release**
We’ve introduced `/advisor` support for Claude Platform on AWS, giving you granular control over when and how Claude provides guidance.

**What's new**
*   **Advanced Modding:** New hooks and UI tools allow for more interactive mods, including virtual prompt text and embedded agent transcripts.
*   **VS Code Polish:** Fixed dozens of UI quirks, including better file handling, improved font scaling for diffs, and more reliable session resumption.
*   **Agent Reliability:** We’ve squashed bugs that caused agents to disappear from tasks or lose context during session restarts.
*   **Smarter Slack Integration:** Claude in Slack now supports Slack Connect channels and can read Slack’s transcripts of voice clips.

**Why you'll care**
This update focuses on making the tool feel more solid—sessions are more resilient, and the integration with your development environment is tighter and more predictable.

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
