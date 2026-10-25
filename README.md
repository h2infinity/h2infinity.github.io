# Networked Systems Laboratory - UTK publishing copy

This is the separate university-hosted copy for **https://web.eecs.utk.edu/~mdjouadi/**. The original `../control-group/` source, its source ZIP, the GitHub `main` branch, and the live GitHub Pages website remain unchanged.

The existing al-folio/Jekyll layouts, Bootstrap navigation, Sass theme, dark mode, people biographies, research themes, and publication system are retained.

## Publish

Read [PUBLISHING.md](PUBLISHING.md). Upload the **contents of `utk-upload/`**, or extract `Networked-Systems-Laboratory-UTK-upload.zip` into the account's `~/webhome/`. The archive has `index.html` at its root. No Jekyll, Ruby, or Node installation is needed on the UTK web server.

The editable source in this folder is separate from the generated upload package. Do not upload the source folder itself.

## Edit

[START_HERE.md](START_HERE.md) maps content to its files. [CONTENT_SOURCES.md](CONTENT_SOURCES.md) records factual sources and outstanding grant-source limitations. [VALIDATION.md](VALIDATION.md) records technical checks and their limits.

## Build

```sh
bundle install
python -m pip install nbconvert pyyaml
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.utk.yml --destination _site-utk
python bin/package_utk.py --built _site-utk --output dist
```

ImageMagick is required for responsive portraits. Use a new or empty `dist` directory for each package. The isolated `utk-publishing-copy-20261025` branch has a build-only workflow that produces the same package; it has no Pages deployment job and does not update `main`.

## Attribution

Built with [Jekyll](https://jekyllrb.com/) and the existing [al-folio theme](https://github.com/alshedivat/al-folio). Original licensing remains in [LICENSE](LICENSE) and is included in the upload package.
