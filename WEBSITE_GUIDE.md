# Laboratory website guide

The website retains its existing Jekyll/al-folio architecture. Update content in Markdown and BibTeX; keep presentation changes in the existing Liquid includes and Sass files.

1. Edit the laboratory introduction in `_pages/about.md`. Homepage sections remain in `_includes/home/`.
2. Update research summaries in `_pages/research.md` and the five numbered research pages under `_projects/`.
3. Maintain names and roles in `_data/people.yml` and biographies in the named Markdown files under `_includes/people/`. The People page stays at `_pages/profiles.md`. Confirm present appointments directly; coauthorship alone is not proof of current student membership. Keep alumni separate.
4. Add source-verified entries to `_bibliography/papers.bib`. Use `publication_status = {published}` or `{preprint}` so the existing bibliography component renders the correct section. Add `selected = {true}` only to papers intended for the homepage. Cite every author and include a DOI or academic source link.
5. Add dated news to `_news/` only when the underlying event is documented. Do not invent acceptance dates or awards.
6. Record new evidence and access limitations in `CONTENT_SOURCES.md`.
7. Maintain funded-award records in `_data/funded_projects.yml`, using only verified Funded entries from the official UTK grants profile. Coverage is currently incomplete because that profile's records were inaccessible; do not infer awards from research themes.
8. Run source checks, formatting, and a fresh Jekyll build. See `PUBLISHING.md`, `VALIDATION.md`, and the direct file map in `START_HERE.md`.

Template demos, sample media, superseded decade lists, redundant archive copies, old performance reports, and unrelated template publishing workflows have been removed. Git history retains prior revisions. Maintenance documents are excluded from the published site.

The configured GitHub Pages user site is `https://h2infinity.github.io/`; the workflow also supports a project repository base path. Keep `_config.yml` and `_config.github-pages.yml` aligned. The UTK profile remains available in `_config.utk.yml` for a separate university-host build.
