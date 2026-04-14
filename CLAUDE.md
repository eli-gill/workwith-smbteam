# SMB Team — Law Firm Growth Audit Repository

This repository stores completed Law Firm Growth Audit reports generated for prospective SMB Team clients.

## Session Initialization — REQUIRED

At the start of every session, before doing anything else, run:

```bash
git pull origin main
```

This ensures you have the latest version of all slash commands and configuration files before proceeding.

## Purpose

Each audit is a branded HTML report produced by the `/audit` slash command. Reports are generated from browser research and a discovery call transcript, then committed directly to this repo.

## Folder Structure

```
Design Files/                          ← templates, read-only, never modified
├── SMB_Team_Audit_Agent_System_Prompt.txt
├── audit_styles.css
├── audit_master_assembly.html
├── section_01_cover.html
├── section_02_toc.html
├── section_03_firm_overview.html
├── section_04_about_smb.html
├── section_05_growth_health.html
├── section_06_lead_generation.html
├── section_07_08_09_intake_team_profit.html
├── section_10_whats_possible.html
└── section_11_next_steps.html

SMB Team Client Audit/
└── [friendly-name]/
    ├── index.html                     ← final assembled output
    ├── audit_styles.css               ← copied from Design Files at assembly
    ├── [FirmName]_[Date]_Research_Notes.txt
    └── sections/                      ← working copies of filled-in section files
        ├── section_01_cover.html
        └── ...
```

Each firm gets its own folder named with a lowercase hyphenated friendly name.
- Example: `SMB Team Client Audit/mandel-law-firm/index.html`
- Example: `SMB Team Client Audit/angel-law/index.html`

**Design Files are permanent templates. Never modify them.** Claude Code reads from them and writes working copies to the firm's folder.

## How to Run an Audit

Use the `/audit` slash command. It handles research, report generation, and git push end to end. See `.claude/commands/audit.md` for full usage.

## Important Notes

- Never modify completed audit HTML files after they are committed without noting the change in the commit message
- The `Outputs/` folder is the only place audit reports should be saved
- Do not commit partial or incomplete audits — only run `/audit` when you have all required inputs (firm name, URL, sales rep, date, revenue, practice area, and transcript)
