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

### Novinky v Claude Code: vylepšené řízení rozpočtů a opravy chyb 🛠️ | Claude Code updates: Team budgets and stability improvements 🛠️

_Claude Code v2.1.316 — 2026-10-31_

## Novinky v Claude Code: vylepšené řízení rozpočtů a opravy chyb 🛠️

**TL;DR** — Tato aktualizace přináší flexibilnější správu rozpočtů pro týmy, vylepšení pro VS Code a řadu oprav, které zvyšují stabilitu a spolehlivost nástroje.

**⭐ Hlavní novinka**
Nyní můžete využívat sdílené rozpočty pro celé skupiny v rámci brány Claude apps, což usnadňuje správu nákladů na úrovni týmů vedle individuálních limitů.

**Co je nového**
*   **Správa a bezpečnost:** Přidána podpora pro vrstvené zásady (layered policies) a lepší integrace s bezpečnostními filtry Amazon Bedrock.
*   **VS Code:** Přihlašování k bráně Claude apps nyní funguje přímo z chatovacího panelu a vylepšili jsme zobrazení „ultrathink“.
*   **Stabilita:** Opravili jsme chyby, kdy procesy zůstávaly běžet na pozadí, vylepšili práci s aliasy v Bash a vyřešili zasekávání síťových požadavků.
*   **Cloudové relace:** Přidána přehlednější správa formulářů a indikátor „Dohánění...“ (Catching up) při načítání historie konverzace.

**Proč by vás to mělo zajímat**
Pokud pracujete v týmu nebo využíváte cloudové relace, tyto změny vám ušetří čas při nastavování a zajistí, že Claude poběží plynuleji i při náročnějších úkolech.

Šťastné kódování!

---

## Claude Code updates: Team budgets and stability improvements 🛠️

**TL;DR** — This release introduces pooled team budgets, better VS Code integration, and a long list of stability fixes for a smoother experience.

**⭐ Highlight of the release**
We’ve added pooled group budgets for the Claude apps gateway, allowing teams to share a monthly budget on top of individual user limits.

**What's new**
*   **Administration:** Added layered policy support and input tagging for Bedrock guardrails to improve security controls.
*   **VS Code:** You can now sign in to a Claude apps gateway directly from the chat panel, and the "ultrathink" feature now matches the terminal’s rainbow UI.
*   **Reliability:** Fixed issues where shell processes would hang after exit, resolved Bash alias conflicts, and improved network request handling.
*   **Cloud sessions:** Added a "Catching up..." indicator for smoother session switching and better form handling for MCP servers.

**Why you'll care**
Whether you're managing team costs or just want your terminal tools to be more reliable, these updates make Claude Code feel more robust and easier to manage in professional environments.

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
