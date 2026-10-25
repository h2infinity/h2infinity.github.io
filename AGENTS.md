# Laboratory website maintenance

This folder is the separate UTK publishing copy. Preserve the existing Jekyll/al-folio architecture and laboratory content. Do not modify `../control-group/`, the GitHub `main` branch, or GitHub Pages when maintaining this copy.

Read `START_HERE.md` for content locations, `PUBLISHING.md` for the UTK build and upload procedure, and `CONTENT_SOURCES.md` before changing research claims. Relevant content/YAML/Liquid instructions remain in `.github/instructions/`.

Before a release, run the source validator, the locked Prettier formatter, a fresh production Jekyll build with `_config.utk.yml`, and `bin/package_utk.py`. The isolated UTK build workflow can perform compilation when local Ruby or Docker is unavailable. Never reuse stale generated output.

The primary URL is `https://web.eecs.utk.edu` with base path `/~mdjouadi`. Keep both `_config.yml` and `_config.utk.yml` aligned. Upload only generated public files, never the editable source or development dependencies. Preserve the LICENSE and use verified sources for factual updates.
