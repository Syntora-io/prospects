# GetPrimera -- Pre-Call Research

## Primera Insurance & Tax Services
- Independent insurance agency, San Antonio/Dallas TX
- ~11-50 employees, ~10 offices, founded ~2010
- Personal + commercial insurance, tax prep, notary
- Progressive agent, multi-carrier
- Standard local agency -- no tech platform, no APIs, no public QTB capability
- No press, no funding, no public leadership bios

## Irfan Ranmal -- Full Profile
- **Education:** BS Computer Science (Georgia Tech), MBA (Duke Fuqua)
- **Location:** Plano, TX (DFW)
- **LinkedIn:** linkedin.com/in/irfan-ranmal-2b107611

### Career Timeline
| Company | Title |
|---------|-------|
| Texas Instruments | Early career (analytics/engineering) |
| DirecTV | Manager, Business Analytics |
| NBCUniversal | Sr. Manager CRM > Director, BI |
| Activision Blizzard | Director > Sr. Director > VP, Consumer Tech/CRM/Analytics (AI/ML, micro-transactions) |
| Disney | VP, Global Marketing & Sales Technology and Analytics |
| Hulu | VP, Data & Analytics (full end-to-end data ecosystem) |
| Beachbody/BODi | EVP Data > Chief Product, Data & Technology Officer (named in SEC filings) |
| DNA Consulting Services | Chief Digital and Data Officer (likely solo consultancy, bridge role) |
| **RFI Ventures** | **Chief Digital & Technology Officer (CURRENT)** |

### RFI Ventures (Current)
- Website: rfi.vc
- "A small venture fund with giant ambitions, investing in the future of global health"
- Barebones site -- no team page, no portfolio listed
- Contact: capital@rfi.vc
- Global health thesis -- adjacent to health insurance but not directly insurtech

### Angel Investing & Ismaili Network
- Listed on AngelMatch and PitchBook as angel/individual investor
- Portfolio companies not publicly disclosed
- Runs the **Ismaili Startup Deal Flow Email List** (connects Ismaili founders raising capital with investors)
- **Speaker at IPN Summit 2026** (Jan 2-4, Houston) -- Ismaili Professionals Network
- IPN Summit featured "Beyond the Billion" founders including Suneera Madhani (Stax/fintech)
- Deeply embedded in Ismaili professional and entrepreneurial community

### Activision Lawsuit (2017-2019)
- Breach of contract + fraud + credit reporting violation
- Filed Nov 2017, dismissed Feb 2019 (likely settled)
- Activision tried to compel arbitration; Ranmal claimed he opted out

### Public Profile
- Very low media presence -- no podcasts, blogs, or interviews found
- Twitter @irfan_ranmal exists but low activity
- Sparse LinkedIn posting

### Primera Connection: Still Unknown
- Has @getprimera.com email (confirmed from calendar invite)
- No public connection found anywhere
- Likely paths: angel investment, Ismaili network connection, advisory role, or acquirer
- RFI Ventures' "global health" thesis could overlap with health insurance

## GetPrimera Tech Stack
| Layer | Technology |
|-------|-----------|
| CMS | WordPress 6.7.4 |
| Forms | Gravity Forms (AJAX, nonce validation) |
| JS | jQuery, RevSlider, AOS |
| Menu | UberMenu v3.7.2 |
| Icons | Font Awesome 4 |
| Analytics | Google Analytics (UA-166680428-19), Google Ads (AW-443274328) |
| Tracking | Phone conversion (210-569-0397) |
| Reviews | Trust.app widget |
| SEO | JSON-LD (Organization, WebPage, BreadcrumbList), OpenGraph |
| Spam | Zero Spam + honeypot |
| Fonts | Google Fonts |

No APIs, no CRM, no AMS, no comparative rater, no client portal. Quote requests go through Gravity Forms -- someone manually reads the submission and calls back. Entire quoting workflow is manual.

## Insurance Quoting API / QTB Landscape

### What QTB Means
Full workflow is RQB: Rate, Quote, Bind.
- **Rate** -- carrier calculates premiums from risk data
- **Quote** -- terms, limits, fees presented to agent/customer
- **Bind** -- quote accepted, policy issued

QTB ratio (quote-to-bind conversion) is the key KPI. Industry range: 20-50%.

### Pain Points in the Space
- Agents manually re-enter same submission into 5-10 carrier portals
- Days-long turnaround for specialty quotes
- No standard data format across carriers
- High drop-off between quote and bind
- Legacy systems everywhere (85% of orgs report this as primary challenge)
- Non-standard APIs (SOAP, screen scraping, flat files)

### Competitors / Players
| Company | Focus |
|---------|-------|
| Herald API | Single API to 60+ commercial products |
| CoverForce | White-label quote-and-bind platform |
| Bold Penguin | Comparative rater + marketplace (acquired by AmFam) |
| Tarmika | Commercial P&C quoting engine |
| EZLynx | Multi-carrier comparative rater |
| Bindable | Embedded insurance API |
| Further AI | AI-powered quote comparison ($25M Series A, Oct 2025) |
| Inaza | AI instant quote-to-bind |

### Common Needs Companies Bring to Syntora
- API aggregation layer across carriers
- Data normalization (canonical model mapped to each carrier's schema)
- Submission intake automation (parsing PDFs, emails, ACORD forms)
- Smart routing (carrier appetite matching before submission)
- Real-time quoting UX
- Embedded distribution APIs

### Key Terms
| Term | Meaning |
|------|---------|
| RQB | Rate, Quote, Bind |
| QTB Ratio | Quote-to-bind conversion rate |
| MGA/MGU | Managing General Agent/Underwriter |
| E&S | Excess & Surplus lines (specialty) |
| ACORD | Industry standard forms/data |
| BOP | Business Owner's Policy |
| GL/WC/PL | General Liability / Workers Comp / Professional Liability |
| Comparative Rater | Tool querying multiple carriers for rate comparison |
| AMS | Agency Management System (Applied Epic, HawkSoft) |
| Appetite | What risks a carrier will write |
| Bindable Quote | Quote that can be accepted without further underwriting |

### 2025-2026 Trends
- AI-powered quoting (LLMs parsing submissions, auto-filling carrier apps)
- Embedded distribution expanding (insurance at point of sale)
- Commercial lines getting most attention (personal lines largely solved)
- Consolidation around proven platforms
- Insurtech market ~$23.5B by 2026
