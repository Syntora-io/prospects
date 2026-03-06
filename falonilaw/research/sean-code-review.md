# Sean Code Review -- agent_email_scraper_python.py

**Date:** 2026-03-02
**Source:** Sean shared this script. It's one of his Jeffers3 email scrapers.
**Context:** Pre-proposal code review to understand their codebase quality and patterns.

---

## What the Script Does

Scrapes a Microsoft 365 mailbox via Graph API, extracts case/docket numbers and ShareFile links from court emails, outputs to Excel on a network share, then auto-formats with COM automation.

**Flow:**
1. Pulls Microsoft Graph API credentials from AWS Secrets Manager
2. Authenticates via OAuth2 client credentials flow
3. Fetches today's emails from a specific mailbox (`$top=100`)
4. Parses HTML body with BeautifulSoup, extracts File # and Docket Number via regex
5. Extracts ShareFile links from HTML
6. Filters to emails sent TO a specific address
7. Writes to Excel on network share (`\\server\shared\scrapes\output\{date}\agent_emails_{date}.xlsx`)
8. Auto-formats Excel columns via COM automation (win32com)

---

## What's Solid

- **AWS Secrets Manager for credentials.** Sean isn't hardcoding API keys. He knows to pull them from a secrets manager at runtime. This is the right pattern.
- **Microsoft Graph API** instead of IMAP or Outlook COM for email access. Modern, well-supported, correct approach.
- **Regex extraction** for file numbers and docket numbers is clean and handles missing values gracefully (returns "N/A").
- **Date-based folder organization** on the output path. Each day's scrape goes into its own folder.
- **BeautifulSoup for HTML parsing.** Standard library choice, handles malformed HTML well.

---

## What a PR Review Would Catch

### 1. No pagination -- only gets first 100 emails

```python
endpoint = f'...?$top=100&$filter=receivedDateTime ge ...'
```

They get 1000+ emails/day. This only processes the first 100. Microsoft Graph API requires handling `@odata.nextLink` to page through all results. On a high-volume day, this script misses 90% of emails. A `while` loop following `nextLink` until exhausted is the standard fix.

**Impact:** Potentially missing the majority of daily court emails. This is a data accuracy issue -- exactly what Trisha said is their core job to prevent.

### 2. `cleanup_excel_file()` deletes from the wrong path

```python
def cleanup_excel_file():
    ...
    output_file = f"agent_emails_{today_est_str}.xlsx"  # looks in current directory
    if os.path.exists(output_file):
        os.remove(output_file)
```

But `fetch_emails_and_create_excel()` saves to:
```python
output_file = os.path.join(date_folder, f"agent_emails_{today_est_str}.xlsx")  # network share
```

The cleanup function and the creation function reference different paths. The cleanup never actually hits the right file.

### 3. `fetch_emails_and_create_excel()` always returns `None`

```python
def fetch_emails_and_create_excel():
    ...
    return None  # always returns None, never the output path
```

```python
file_path = fetch_emails_and_create_excel()  # file_path is always None
```

The function works (creates the Excel file), but the return value is never set to the actual output path. If anything downstream depended on `file_path`, it would fail silently.

### 4. Bare `except:` clause

```python
for cell in column:
    try:
        if len(str(cell.value)) > max_length:
            max_length = len(cell.value)
    except:
        pass
```

Swallows every exception silently during column width calculation. Could hide real errors (NoneType, encoding issues, etc.). Should be `except (TypeError, AttributeError):` at minimum.

### 5. COM automation locks script to Windows

```python
from win32com.client import Dispatch

def auto_format(filename):
    excel = Dispatch('Excel.Application')
```

Requires Excel installed on the machine. Ties this script to Windows/AWS Workspace. Can't run in a container, Linux CI runner, or any non-Windows environment. This is fine for their current setup but limits future flexibility.

### 6. Hardcoded identifiers

```python
secret_name = "[CENSORED_SECRET]"
tenant = "[CENSORED_TENANT_ID]"
```

In the real file, these are likely hardcoded strings. Should be environment variables or pulled from config. GitHub's basic secret scanning would flag these if they were committed to a repo.

---

## Dependencies

| Package | Purpose | Notes |
|---------|---------|-------|
| requests | HTTP calls to Graph API and token endpoint | Standard |
| pandas | DataFrame creation, Excel writing | Standard |
| beautifulsoup4 | HTML parsing for email body and link extraction | Standard |
| boto3 | AWS Secrets Manager access | Confirms they use AWS SDK |
| openpyxl | Excel file writing engine | Standard |
| pytz | Timezone handling (US/Eastern) | Standard |
| win32com | COM automation for Excel formatting | Windows-only, requires Excel installed |
| re, os, json, datetime | Standard library | -- |

No `requirements.txt` or `pyproject.toml` assumed. Dependency management is likely manual (pip install on each Workspace).

---

## What This Confirms About Our Proposal

1. **Sean writes clean, functional code.** He understands auth patterns, API integration, and data processing. He's not the problem -- the lack of review process is.

2. **A single PR review would catch the pagination bug.** They're potentially missing 90% of daily emails on high-volume days. That's the kind of thing that costs them real money and directly undermines Trisha's mandate ("collect all the data coming in and put it into the system as fast and accurate as possible").

3. **The `win32com` dependency is a pattern we'll see across their scripts.** Anything using COM automation is locked to Windows. Worth cataloging during the Stage 1 audit but not worth changing until there's a reason to.

4. **AWS Secrets Manager usage is a good sign.** Sean already thinks about credential management. Moving to GitHub with secret scanning reinforces a practice he's already following.

5. **No tests, no linting, no type hints.** Standard for a team without CI/CD. GitHub Actions adding a basic pylint check on every PR would catch obvious issues without requiring Sean to change how he writes code.

6. **Their scripts ARE production quality for a team without review.** With review, they'd be significantly more reliable. The gap between where they are and where they need to be is smaller than the deck might imply -- it's process, not skill.

---

## Talking Points for the Call

- Don't critique Sean's code on the call. That's not the message. The message is: "Your team writes solid code. A review process catches the edge cases that individual developers miss -- pagination limits, path mismatches, silent error handling. That's not a skill issue, it's a process issue."
- The pagination bug is a concrete example of ROI. If they're processing 100 out of 1000+ daily emails, that's a data gap. One PR review closes it.
- Sean already uses AWS Secrets Manager. He'll appreciate that GitHub's secret scanning adds another layer without changing his workflow.