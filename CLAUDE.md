# Prospects - Project Context for Claude

## Purpose
Syntora sales pipeline. Research, meeting notes, and strategy docs for active prospects.

## Structure
```
prospects/
├── {prospect}/
│   ├── PROSPECT.md          # Status, contacts, company info (source of truth)
│   ├── meetings/            # Call notes (YYYY-MM-DD-description.md)
│   ├── notes/               # Internal strategy and analysis
│   └── research/            # Industry research, technical approach, pricing
├── CLAUDE.md
└── README.md
```

## Conventions
- All files are Markdown
- Date format: YYYY-MM-DD in filenames and content
- PROSPECT.md is the single source of truth for prospect status and stage
- Meeting notes go in `meetings/`, named by date and description
- No code, no credentials, no client data -- research and strategy only

## Workflow
1. New prospect: create `{prospect}/PROSPECT.md` with status and company info
2. After each call: add meeting notes in `meetings/`
3. Research and prep docs go in `research/`
4. Internal strategy and analysis go in `notes/`
5. Update PROSPECT.md status after every interaction

## Active Prospects
| Prospect | Industry | Stage |
|----------|----------|-------|
| bearproperty | Property Management (LIHTC) | Presenting Solution |
| falonilaw | Debt Collection Law | Proposal |
