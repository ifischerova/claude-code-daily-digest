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

### Vylepšení stability a hladší workflow v Claude Code 🛠️ | Smoother sessions and better error reporting 🛠️

_Claude Code v2.1.273 — 2026-09-16_

## Vylepšení stability a hladší workflow v Claude Code 🛠️

**TL;DR** — Tato verze přináší desítky oprav chyb, lepší chybové hlášky a plynulejší spolupráci mezi vaším terminálem a cloudem.

**⭐ Highlight of the release** — Nyní můžete snadno „forknout“ relaci z aplikace Claude přímo do svého počítače jako proces na pozadí, což vám umožní plynule přecházet mezi rozhraními bez ztráty kontextu.

**What's new**
- **Lepší diagnostika:** Chybové zprávy u GitHubu, AWS a proxy připojení jsou nyní mnohem konkrétnější a říkají vám, co přesně opravit.
- **Stabilita:** Opravili jsme chybu, kvůli které auto-kompakce kontextu běžela příliš agresivně, a vylepšili jsme odezvu při dlouhých relacích.
- **Bezpečnost:** Přísnější kontrola oprávnění pro Bash a opravy v chování MCP serverů.
- **Code Review:** Vylepšili jsme logiku revizí, takže se už nebudou zbytečně opakovat u stejných změn.

**Why you'll care**
Získáte spolehlivější nástroj, který vás méně často vyruší obecnými chybami a lépe si rozumí s vaším GitHubem i cloudovým nastavením.

Užívejte si kódování!

---

## Smoother sessions and better error reporting 🛠️

**TL;DR** — This release is packed with stability improvements, smarter error messages, and seamless session handling to keep you in the flow.

**⭐ Highlight of the release** — You can now fork a session started in the Claude app directly to your local machine as a background process, making it easier than ever to switch environments without losing your place.

**What's new**
- **Clearer Errors:** GitHub, AWS, and proxy connection issues now provide actionable advice instead of generic codes.
- **Improved Stability:** Fixed an issue where context auto-compaction was triggering too early, and reduced UI lag during long sessions.
- **Enhanced Security:** Refined Bash permission checks and fixed edge cases in MCP server management.
- **Smarter Code Reviews:** PR reviews are now more efficient, avoiding redundant re-reviews for identical code pushes.

**Why you'll care**
Claude Code is now more predictable and transparent, helping you spend less time troubleshooting your tools and more time building.

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
