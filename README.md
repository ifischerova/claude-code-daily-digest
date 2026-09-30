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

### Claude Code 2.1.285: Nové možnosti správy pluginů a lepší desktopová integrace 🚀 | Claude Code 2.1.285: Better plugin control and smoother desktop workflows 🚀

_Claude Code v2.1.285 — 2026-09-30_

## Claude Code 2.1.285: Nové možnosti správy pluginů a lepší desktopová integrace 🚀

**TL;DR** — Tato aktualizace přináší vylepšenou správu pluginů, snadnější spouštění z desktopové aplikace a řadu oprav pro hladší fungování.

**⭐ Hlavní novinka**
Nyní můžete snadno konfigurovat pluginy přímo při instalaci pomocí příkazu `claude plugin install --config <server>.<klíč>=<hodnota>`, což vám ušetří zdlouhavé nastavování přes webové rozhraní.

**Co je nového**
*   **Desktopová integrace:** Příkaz `claude --desktop` nyní otevře aplikaci přímo v aktuálním adresáři nebo naváže na předchozí relaci.
*   **Správa pluginů:** Přibyl příkaz `claude plugin configure`, který vám přehledně ukáže, co je potřeba v nastavení doplnit.
*   **Bezpečnost:** Přidána možnost `allowedProviders` pro správce, kteří chtějí omezit povolené API poskytovatele na daném stroji.
*   **Větší stabilita:** Opravili jsme desítky drobných chyb v napojení na SSH, chování subagentů a synchronizaci artifactů, aby vás při práci nic nezastavilo.

**Proč na tom záleží**
Claude Code je díky těmto změnám mnohem předvídatelnější a lépe se integruje do vašeho stávajícího pracovního postupu, ať už používáte VS Code nebo terminál.

Ať se vám dnes skvěle kóduje!

---

## Claude Code 2.1.285: Better plugin control and smoother desktop workflows 🚀

**TL;DR** — This release streamlines plugin configuration, improves desktop app integration, and squashes a wide variety of bugs for a more reliable experience.

**⭐ Highlight of the release**
You can now configure MCP server settings directly during installation using `claude plugin install --config <server>.<key>=<value>`, letting you jump straight into your work without navigating to the settings menu.

**What's new**
*   **Desktop Workflow:** Use `claude --desktop` to launch the app in your current folder or resume a specific session instantly.
*   **Plugin Management:** Added `claude plugin configure` to easily view and set missing plugin options.
*   **Enterprise Control:** Admins can now use `allowedProviders` to restrict which API providers (like Bedrock or Vertex AI) are permitted on a machine.
*   **Stability Improvements:** Dozens of fixes for SSH handling, subagent behavior, and artifact synchronization ensure a more seamless development environment.

**Why you'll care**
These updates make Claude Code feel more like a native part of your workflow, reducing friction when setting up tools and keeping your sessions stable.

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
