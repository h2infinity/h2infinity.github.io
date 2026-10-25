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

A full production Jekyll build completed successfully in GitHub Actions for commit `d8885df33e6ac8bbdc1d817272db9b09a5ec47d0` on `h2infinity/hban29.github.io`. [Run 40149173656](https://github.com/h2infinity/hban29.github.io/actions/runs/40149173656) passed source validation, Jekyll compilation, generated HTML/local-link checks, artifact upload, and Pages deployment. The owner subsequently requested reusing this repository, deleting extra files, and renaming it to `h2infinity.github.io`. The root-address deployment remains pending the rename.

Git, GitHub CLI, Ruby, Bundler, Docker, and WSL remain unavailable locally. There are no exposed browser sessions. Desktop/mobile appearance, dark mode, and interactive publication search have not been reviewed in a browser.

The pre-existing `_site/` output predates this revision. It has not been hand-edited and must not be treated as an updated preview or deployment artifact.

## Checks required before release

The consolidated `Deploy site` workflow runs a fresh production Jekyll build using the existing Gemfile and plugins. It then runs `python bin/validate_site.py --built _site --baseurl "$SITE_BASEURL"`, which checks generated routes, local links/assets/fragments, publication inclusion, featured papers, unresolved Liquid, project base paths, and absence of template blog/book/sample-resume output. Deployment depends on those checks passing.

After the repository is renamed and redeployed, verify the site visually at desktop and mobile widths, switch light/dark mode, and exercise publication search and navigation.

## People biography update

The People page now incorporates all six biographies from the laboratory-provided `People_bio.txt`: Fatima Taousser and five current Ph.D. students (Hemanta Ban, Uzair Sharif Mughal, Maria Batool, Burcum Eken, and Umarbek Guvercin). The faculty-director biography, existing profile layout, and separate alumni section are retained. Earlier notices that the supplied students' roles were unconfirmed have been removed. Fatima's past UTK postdoctoral appointment is distinguished from her supplied Teaching Assistant Professor title.

The source file is unchanged. The updated page and maintenance documents pass Prettier checks and the existing source validator. The production build and generated-site checks also passed in the GitHub Actions run above.

## Formatting workflow consistency

The initial remote formatting job installed the newest formatter instead of using the checked-in lockfile and flagged `_layouts/bib.liquid`, which passes with the locally installed locked dependencies. The workflow now installs dependencies with `npm ci` so local and CI formatting use the same versions. Local formatting checks pass.

## Repository cleanup

Removed 132 files: template blog posts, example projects, sample books/courses/resumes/media, superseded publication lists, duplicate archive records, old Lighthouse reports and README screenshots, and unrelated template automation. The inherited Jekyll framework, layouts, styles, reusable components, laboratory content, source provenance, and build/development configuration remain. The cleared sample venue map remains available to the existing bibliography component.

Cleanup was checked against an explicit path list confined to the project directory. Source validation and formatting pass. A fresh remote build is required to verify this cleanup revision before reporting its deployment as successful. Repository renaming is unavailable through the current connector and must be performed through GitHub Settings.
