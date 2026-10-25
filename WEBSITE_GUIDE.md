# Laboratory website guide

The website retains its existing Jekyll/al-folio architecture. Update content in Markdown and BibTeX; keep presentation changes in the existing Liquid includes and Sass files.

1. Edit the laboratory introduction in `_pages/about.md`. Homepage sections remain in `_includes/home/`.
2. Update research summaries in `_pages/research.md` and the five numbered research pages under `_projects/`.
3. Maintain people in `_pages/profiles.md`. Confirm present appointments directly; coauthorship alone is not proof of current student membership. Keep alumni separate.
4. Add source-verified entries to `_bibliography/papers.bib`. Use `publication_status = {published}` or `{preprint}` so the existing bibliography component renders the correct section. Add `selected = {true}` only to papers intended for the homepage. Cite every author and include a DOI or academic source link.
5. Add dated news to `_news/` only when the underlying event is documented. Do not invent acceptance dates or awards.
6. Record new evidence and access limitations in `CONTENT_SOURCES.md`.
7. Run source checks, formatting, and a fresh Jekyll build. See `PUBLISHING.md` and `VALIDATION.md`.

Template demos and superseded decade lists are excluded in `_config.yml`. Superseded source records are kept in `docs/archive/`; neither that directory nor the maintenance documents are published.

The configured GitHub Pages user site is `https://h2infinity.github.io/`; the workflow also supports a project repository base path. Keep `_config.yml` and `_config.github-pages.yml` aligned. The UTK profile remains available in `_config.utk.yml` for a separate university-host build.
