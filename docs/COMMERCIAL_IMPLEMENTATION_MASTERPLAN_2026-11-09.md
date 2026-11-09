# leosofttechnologies — research-led implementation and portfolio decision plan

**Date:** 2026-11-09 · **Portfolio lane:** Legacy Leosoft corporate presentation — consolidate · **Evidence level:** README or source detail incomplete; do not treat project name as implemented functionality.

## Commercial purpose
**Proposed role:** Corporate brand and lead-generation system, not parallel operations backend.
**Audience and hypothesis:** Local and international software prospects; monetize through referrals into existing SaaS products.
**Research/terms to verify:** https://asvs.owasp.org/. Research three relevant substitutes before writing code. A missing README or empty repo is not evidence of functionality or commercial readiness.

## Project-specific implementation sequence
### Priority 0 — evidence and risk assessment
P0 inspect legacy branch, content rights, deployed DNS and overlap with leosoftug, All-tech-hub and leosoft-webapp; audit dependencies and security.

### Priority 1 — consolidation or one complete workflow
P1 consolidate service catalog, demonstrations, documentation, support, product-specific privacy and contact forms in chosen canonical site; avoid direct database coupling across products.

### Priority 2 — commercialization only if justified
P2 instrument opt-in lead capture and source attribution, simple proposal request workflow and partner page; create redirects from superseded site.

### Unambiguous release/closure acceptance
All product links and support contact functional, consented analytics, clear ownership and no duplicate account system. Archive is a valid successful outcome where no distinct customer need exists.

## Implementation operating contract
**Discover → design → implement → validate → pilot → release.** Current code takes precedence over assumptions in this plan. Every claimed complete feature requires evidence linked to the latest commit, not a checklist tick.

1. **Current-state inventory (week 1):** inspect repository tree/branches/issues/README, license, dependency manifests, deployment, open vulnerabilities and code ownership. Produce module inventory, data classification and overlap chart. Record confidence as observed / inferred / unknown; avoid inventing functionality.
2. **Product decision (week 2):** conduct 10 real buyer interviews if a distinct buyer exists, benchmark three direct alternatives, identify supported workflow, price hypothesis, operational costs, and choose **invest / merge / archive**. Do not invest in an unverified product market.
3. **Solution design (weeks 2–3 if investing):** one approved customer journey, data flow, authoritative transactions, role matrix, UI map, integration architecture, threat model and measurable acceptance; create issue tickets with scope, estimate range and dependency ordering.
4. **Full-stack development (weeks 3–7):** migration, server/domain logic, API, responsive user and admin screens, empty/loading/error states, audit, backups, rollback and support workflows as one vertical slice. Avoid unnecessary SaaS infrastructure when a static site or single-tenant service suffices.
5. **Verification (weeks 6–9):** run unit, integration, permissions, end-to-end, dependency and accessibility tests; simulate network loss/concurrency; verify production build/deploy, complete restore and incident response. Use sample/synthetic data until consent and controls are approved.
6. **Commercial test (weeks 9–12):** fixed-scope pilot with signed limitations, support owner and price test; count qualified inbound leads, demos, activation, paid users, support time, gross margin and retention. Don't claim market validation without paying use.

### Acceptance record for every milestone
Link the issue, author, pull request and SHA, test command/exit code, affected UI and back-end routes, reviewer, sample screenshots, baseline and deployed revision, migration/rollback, known limitations and explicit ship/repair/pause decision. Backups must be restored and tested—not simply scheduled.

### Architecture and security rules
Keep project boundaries intact; reuse shared commercial services through API/events, not a shared unscoped database. Use secrets manager/environment, least privilege, audit of privileged actions, accurate error states, opt-in analytics, privacy notices and customer export/deletion. Follow NIST SSDF and OWASP ASVS where relevant; review Uganda PDPO obligations. Never turn a private experimental repository into a public service without threat modeling and permission to use its data.

### Commercial support model
Do not quote rates unsupported by observed usage. Price based on interviews and total customer costs including onboarding, hosting, payment fees, support, refunds, taxes and churn. For archived repositories, keep a clear successor/redirect, preservation notice and maintenance owner. For active products, publish terms, SLA boundaries, incidents, support channel and an honest demo.

### Core references
- https://csrc.nist.gov/projects/ssdf
- https://asvs.owasp.org/
- https://doingbusiness.finance.go.ug/licensing/pdpo-data-protection-registration

**Status:** advisory roadmap; no application code, infrastructure or customer records modified by this document.
