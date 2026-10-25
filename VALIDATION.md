# UTK publishing-copy validation

Date: October 25, 2026.

## Scope

This separate copy preserves the existing al-folio/Jekyll site. Its default URL and UTK override both target `https://web.eecs.utk.edu/~mdjouadi/`. The GitHub and UTK copies retain separate hosting profiles. At the owner's subsequent request, the biography, publication-search fix, and ACC publication update are being applied to both.

Thirty inherited template documents, contribution metadata, editor setup files, and GitHub-only publishing files were removed from this copy. Required theme components, styles, plugins, content, source attribution, bibliography, Docker build setup, formatting configuration, and maintenance guides remain. The final public package includes only rendered pages and their dependencies, not the editable framework, development dependencies, demo libraries, source maps, or maintenance documents.

## Automated checks

The existing source validator checks 21 content files (including three legacy redirects), the roster and named biography files, 15 published papers, four labeled preprints, routes, required assets, and template placeholders. Known old publication, course, and student URLs redirect to their replacement pages; their new content no longer cites the replaced pages as historical archives. The UTK build checker additionally validates `/~mdjouadi` local paths, anchors, responsive image sources, canonical URLs, all members and publications, and shared research-theme inclusion.

`bin/package_utk.py` recursively collects HTML dependencies and CSS font/image references, checks the trimmed upload copy again, verifies the feed/sitemap/robots URLs, and verifies the ZIP and its SHA-256 manifest. A build-only workflow on the isolated UTK branch runs formatting, source validation, the production Jekyll build, and packaging. It has no deployment job or write permissions.

The production UTK build passed in [run 40163507788](https://github.com/h2infinity/h2infinity.github.io/actions/runs/40163507788), commit `159b8406a548ccb227b924a0c4f6d3c560748cdc`, on the isolated `utk-publishing-copy-20261025` branch. Formatting, source validation, Jekyll compilation, 21 generated HTML pages and local links, responsive images, trimmed dependency validation, ZIP integrity, and SHA-256 checks all passed. The old local `control-group/_site/` was not used.

The upload ZIP contains **43 public files**, is **4,982,623 bytes**, and has SHA-256 `13ff99554f814f707f6efeab6fe3577543470e82d1beeb9751d33d73356dacc5`. It is inside the [UTK-website-upload artifact](https://github.com/h2infinity/h2infinity.github.io/actions/runs/40163507788/artifacts/12586894400), together with the identical upload directory, manifest, checksum, and instructions. The artifact expires January 23, 2027; rebuild the isolated branch to regenerate it after expiry.

The GitHub `main` head was checked and remains `d353afbc1d55e2e3fef81ad3b486d39c4bc0e9a1`. Original source files still match the original source ZIP byte for byte. The generated artifact was fetched through the connected GitHub tool, but saving it to this local machine was blocked by the environment's network socket restrictions. Download it through GitHub for server upload.

## Limits

No UTK server upload, overwrite, or remote file deletion has been performed. EECS account access is unavailable. The old public homepage timed out when fetched, so old paper/course files and inbound links have not been inventoried. Browser surfaces are unavailable; desktop/mobile visual inspection and interactive checks remain to be performed after staging or upload.

The supplied grants profile remains inaccessible. Existing research themes retain their verified publication sources; complete coverage of funded-project topics is not claimed. The footer remains only the laboratory copyright, and current people details remain based on the supplied `People_bio.txt`.

## October 25 content and search correction

The updated owner-supplied `People_bio.txt` changes Hemanta Ban's interests, UT Knoxville master's education, and RWTH Aachen experience. The other supplied biographies still match. The publication-search include now wraps its input in an HTML block, preventing its indentation from producing visible code in Markdown. The build validator requires exactly one accessible search input outside code blocks and rejects visible input markup.

The formation-control entry is now an ACC 2026 paper with pages 1398-1403, the IEEE DOI, and the supplied publisher link. It appears once under Published papers; news and research links use the conference record. The author-maintained arXiv record confirms the conference, pages, DOI, and IEEE document number. Current totals are 15 published papers and four preprints. Fresh build results for this revision will supersede the older run/package details above.
