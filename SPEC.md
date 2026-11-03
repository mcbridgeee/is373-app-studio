# App Studio decisions

The durable agreement between learner and AI. Update only agreed decisions and
actual evidence; pending is a valid state. Keep explanations/help in
[LEARNING.md](LEARNING.md), not a second copy here.

## Current stage

- **Current feature:** APP-001.
- **Status:** Verbella homepage built on branch `app-001-homepage` for issue [#1](https://github.com/mcbridgeee/is373-app-studio/issues/1); full checks pass locally; learner kept it.
- **Next step:** Open the PR, review its CI, then decide whether to merge.
- **Implementation marker:** `studio.json` is at `implemented_through: 1` after APP-001 checks passed.

This repository owns application code. Server/proxy changes and production
deployment are outside these three local-development lessons. Prepared helpers
are reusable foundations, not evidence that unfinished routes are implemented.

## APP-001 · Branded homepage

**Scope:** make the neutral FastAPI homepage express one chosen identity with
a simple original SVG mark, coherent copy, navigation and shared style tokens.
Keep account actions honest about their unfinished state. Agreed addition:
design mobile-first, then scale up to desktop.

| Decision | Agreement |
|---|---|
| Visitor and concrete use situation | Someone who reads a lot or talks with people who have big vocabularies, and keeps looking up unfamiliar words, sometimes the same one more than once. They want one place to keep those words so they learn them instead of forgetting them. |
| Reused IS117 brand, or name / promise / primary archetype | Name: Verbella, a personal vocabulary page of words you actually ran into. Promise: "Keep the words you find." Archetype: Sage (learning and quiet wisdom, not flashy). Learner's own logo in forest, sage and cream, static and animated, in `app/static/brand/`. A later word of the day is an idea only, outside APP-001. |
| One visible choice and visitor benefit | Soft sage and cream colors with a bookish serif, so it feels like reading at home rather than a study app pushing you (learner's reason). Palette: forest `#474329`, sage `#AEB1A0`, cream `#F2EDE2`. Type: Cormorant Garamond headings and EB Garamond body (free OFL fonts close to the mood board's Ivy Presto and The Seasons, self-hosted). All visible app text displays lowercase, applied site-wide in CSS. Dark mode deferred. |
| Own issue / branch / PR | Issue [#1](https://github.com/mcbridgeee/is373-app-studio/issues/1) / `app-001-homepage` / PR [#2](https://github.com/mcbridgeee/is373-app-studio/pull/2) |

**Keep when:** the agreed identity is visible and usable at desktop/narrow widths;
full foundation + APP-001 checks pass; AI review and the learner's actual check
interpretation/browser observation/keep reason are recorded; reviewed evidence
and verified GitHub state are linked below.

## APP-002 · Signup, login and logout

**Scope:** add browser forms and REST behavior for member signup, login, a private
dashboard and logout backed by SQLite. Reuse the prepared password/JWT/CSRF/session
helpers; keep data local. New accounts cannot choose their role.

| Decision | Agreement |
|---|---|
| Expected public/private behavior and account flow | Pending |
| Valid and rejected cases to demonstrate | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** the agreed forms/API work; duplicate/invalid signup and wrong
credentials are rejected; passwords are hashed; authentication uses validated,
expiring JWTs with protected cookies and CSRF; private requests require a live
session and logout revokes it. Full cumulative checks, AI review, actual learner
contributions and GitHub state are recorded. This is not a production-security certification.

## APP-003 · Server-enforced roles

**Scope:** enforce a small member/admin boundary in the API and browser. Assign
roles only through the trusted local terminal command; use current server-side
permissions, including for an existing session after a role change.

| Visitor | Homepage | Member area | Admin area/API |
|---|---|---|---|
| Anonymous | Allowed | Login required | Login required |
| Member | Allowed | Allowed | Forbidden |
| Admin | Allowed | Allowed | Allowed |

| Decision | Agreement |
|---|---|
| Intended admin-only result | Pending |
| Actual allowed/denied request evidence | Pending |
| Own issue / branch / PR | Pending |

**Keep when:** a direct request cannot bypass the role boundary, role changes
take effect as specified, new signup remains member-only, and full cumulative
checks plus AI review pass. Link the learner's actual interpretation/observation,
reviewed record and verified GitHub result. Hidden navigation alone is insufficient.

## Evidence

Link actual files/checks and the student's own issues/PRs. No fabricated URLs,
customer research or claims that a timestamp proves learning.

| Feature | Files / own issue / PR | Actual checks and learner observations | Kept / GitHub state |
|---|---|---|---|
| APP-001 | Issue [#1](https://github.com/mcbridgeee/is373-app-studio/issues/1); `app/brand.json`, `app/templates/home.html`, `app/templates/base.html`, `app/static/site.css`, `app/static/logo.svg`, `app/static/brand/`, `app/static/fonts/` | Local `check --lesson APP-001` and full `check` at marker 1: Black, Pylint, 98 foundation cases, 2 APP-001 contracts, 2 Chromium journeys passed. AI reviewed 390px and desktop layouts, keyboard focus and reduced motion (fixed: static logo shown when reduce motion is on). Learner's check interpretation, browser observation and keep reason are in [LEARNING.md](LEARNING.md) | Kept; PR [#2](https://github.com/mcbridgeee/is373-app-studio/pull/2) open, CI pending |
| APP-002 | Pending | Unfinished; explicit contracts not yet passed | Pending |
| APP-003 | Pending | Unfinished; explicit contracts not yet passed | Pending |

The instructor's reference branches show possible implementations. They do not
establish this repository's completion or the learner's own reasoning.
