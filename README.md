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

### Claude Code 2.1.288: Vylepšená práce s historií a flexibilnější recenze kódu 🚀 | Claude Code 2.1.288: Better session recovery and refined code reviews 🚀

_Claude Code v2.1.288 — 2026-10-03_

## Claude Code 2.1.288: Vylepšená práce s historií a flexibilnější recenze kódu 🚀

**TL;DR** — Tato verze přináší lepší stabilitu při obnovování konverzací, nové ovládací prvky pro kontrolu kódu a řadu drobných oprav pro hladší zážitek.

**⭐ Highlight of the release** — Nový parametr `--max-findings <n>|all` pro příkaz `/code-review`, který vám dává plnou kontrolu nad tím, kolik připomínek od Claudea k vašemu kódu dostanete.

**What's new**
*   **Obnova po Ctrl+C:** Pokud omylem smažete rozepsaný prompt, klávesa šipka nahoru vám ho vrátí zpět včetně vložených obrázků.
*   **Chytřejší procházení:** Pomocí Ctrl+F můžete snadno vyhledávat v relacích a Alt+šipky vám umožní rychle přeskakovat mezi skupinami agentů.
*   **Vylepšená práce s historií:** Claude nyní lépe zvládá dlouhé konverzace díky vylepšené automatické komprimaci dat.
*   **Lepší podpora pluginů:** Opravy instalací přes GitHub a stabilnější běh v rámci subagentů.
*   **Přístupnost:** Vylepšené oznámení pro čtečky obrazovky při schvalování plánů.

**Why you'll care** — S těmito změnami je Claude Code spolehlivější při delším programování a dává vám větší kontrolu nad tím, jakým způsobem vám pomáhá s recenzí kódu.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.288: Better session recovery and refined code reviews 🚀

**TL;DR** — This release improves session stability, adds flexible controls for code reviews, and squashes a long list of bugs to keep your workflow smooth.

**⭐ Highlight of the release** — The new `--max-findings <n>|all` flag for `/code-review` lets you decide exactly how many issues you want Claude to report, giving you control over the verbosity of your reviews.

**What's new**
*   **Draft recovery:** Accidentally cleared your prompt with Ctrl+C? Just hit Up to restore your draft, including any pasted text or images.
*   **Easier navigation:** Use Ctrl+F to find sessions by name and Alt+Up/Down to jump between agent groups.
*   **Smarter history:** Conversations are now more reliable thanks to improved auto-compaction and better handling of resumed sessions.
*   **Plugin fixes:** Smoother plugin installs from GitHub and improved reliability when running multiple subagents.
*   **Accessibility:** Screen reader users get clearer announcements when approving plans and navigating permission modes.

**Why you'll care** — These updates make Claude Code feel more robust during long coding sessions and ensure you get exactly the level of feedback you need during reviews.

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
