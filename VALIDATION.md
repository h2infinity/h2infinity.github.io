# UTK publishing-copy validation

Date: October 25, 2026.

## Scope

This separate copy preserves the existing al-folio/Jekyll site. Its default URL and UTK override both target `https://web.eecs.utk.edu/~mdjouadi/`. The original GitHub source and live GitHub Pages website are unchanged.

Thirty inherited template documents, contribution metadata, editor setup files, and GitHub-only publishing files were removed from this copy. Required theme components, styles, plugins, content, source attribution, bibliography, Docker build setup, formatting configuration, and maintenance guides remain. The final public package includes only rendered pages and their dependencies, not the editable framework, development dependencies, demo libraries, source maps, or maintenance documents.

## Automated checks

The existing source validator checks 18 content files, the roster and named biography files, 14 published papers, five labeled preprints, routes, required assets, and template placeholders. The UTK build checker additionally validates `/~mdjouadi` local paths, anchors, responsive image sources, canonical URLs, all members and publications, and shared research-theme inclusion.

`bin/package_utk.py` recursively collects HTML dependencies and CSS font/image references, checks the trimmed upload copy again, verifies the feed/sitemap/robots URLs, and verifies the ZIP and its SHA-256 manifest. A build-only workflow on the isolated UTK branch runs formatting, source validation, the production Jekyll build, and packaging. It has no deployment job or write permissions.

Build results are recorded after the workflow completes. A fresh successful UTK build is required; the old local `control-group/_site/` is not used.

## Limits

No UTK server upload, overwrite, or remote file deletion has been performed. EECS account access is unavailable. The old public homepage timed out when fetched, so old paper/course files and inbound links have not been inventoried. Browser surfaces are unavailable; desktop/mobile visual inspection and interactive checks remain to be performed after staging or upload.

The supplied grants profile remains inaccessible. Existing research themes retain their verified publication sources; complete coverage of funded-project topics is not claimed. The footer remains only the laboratory copyright, and current people details remain based on the supplied `People_bio.txt`.
