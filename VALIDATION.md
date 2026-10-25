# Validation record

Revision date: October 24, 2026.

## Scope preserved

The existing Jekyll/al-folio framework, Liquid layouts, homepage includes, research cards, project cards, Sass theme, dark-mode controls, and publication search are retained. The portrait now appears with the faculty biography on the people page. The navbar uses the existing Bootstrap collapse component at the large-screen breakpoint to accommodate the laboratory identity and navigation.

## Source checks

Repository-wide Prettier formatting completed successfully. Three inherited Sass files received formatting-only changes; theme values and layout rules were preserved.

`python bin/validate_site.py` passes for 18 active content files, 14 published papers, and five preprints. It checks front matter, layout/include references, route uniqueness, navigation order, required assets, balanced BibTeX fields, unique citation keys/DOIs, publication status and venue fields, and common placeholder/encoding errors.

The checker validates DOI syntax and source structure; it does not make network requests or certify external link availability. The factual verification record is in `CONTENT_SOURCES.md`.

The existing bibliography search was adjusted so publication-section and citation anchors navigate without hiding every paper, and its input now has an accessible label. The existing 300 ms search delay now uses a callback.

`node --check assets/js/bibsearch.js` passed. A focused Node behavior check passed for section/citation navigation, case-insensitive hash filtering, delayed input filtering, and malformed hash handling. All 25 YAML configuration/data/workflow files parsed successfully, and the inline deployment URL-generation script passed Python syntax parsing. These checks do not substitute for browser verification.

## Build and visual limits

A full Jekyll build has not run in this session. Git, GitHub CLI, Ruby, Bundler, Docker, and WSL are unavailable in the execution environment. There are no exposed browser sessions. Direct GitHub network access from the shell was denied. Accordingly, there is no claim of a successful rendered build, desktop/mobile review, dark-mode test, live link check, remote commit, or deployment.

The pre-existing `_site/` output predates this revision. It has not been hand-edited and must not be treated as an updated preview or deployment artifact.

## Checks required before release

The consolidated `Deploy site` workflow runs a fresh production Jekyll build using the existing Gemfile and plugins. It then runs `python bin/validate_site.py --built _site --baseurl "$SITE_BASEURL"`, which checks generated routes, local links/assets/fragments, publication inclusion, featured papers, unresolved Liquid, project base paths, and absence of template blog/book/sample-resume output. Deployment depends on those checks passing.

After GitHub access is available, verify the deployed site visually at desktop and mobile widths, switch light/dark mode, and exercise publication search and navigation.

## People biography update

The People page now incorporates all six biographies from the laboratory-provided `People_bio.txt`: Fatima Taousser and five current Ph.D. students (Hemanta Ban, Uzair Sharif Mughal, Maria Batool, Burcum Eken, and Umarbek Guvercin). The faculty-director biography, existing profile layout, and separate alumni section are retained. Earlier notices that the supplied students' roles were unconfirmed have been removed. Fatima's past UTK postdoctoral appointment is distinguished from her supplied Teaching Assistant Professor title.

The source file is unchanged. The updated page and maintenance documents pass Prettier checks and the existing source validator. A full Jekyll build and visual preview remain unavailable because Ruby/Bundler and Docker are absent.
