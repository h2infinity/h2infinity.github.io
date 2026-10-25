# Replace the university-hosted website

Target: **https://web.eecs.utk.edu/~mdjouadi/**. This package is an independent UTK copy; the GitHub Pages site remains unchanged.

## Which files to upload

Use `Networked-Systems-Laboratory-UTK-upload.zip`, or the identical `utk-upload/` directory. The archive contains the finished HTML pages, referenced styles, scripts, portrait variants, icon fonts, favicon, feed, sitemap, robots file, and license. `index.html` is at the archive root.

Do not upload this editable source folder, a GitHub Pages artifact, or the old `control-group/_site/` output. The UTK build uses `url: https://web.eecs.utk.edu` and `baseurl: /~mdjouadi`. The university URL prefix is embedded in the links; do not create another `~mdjouadi` subfolder inside the web directory.

## Upload using the EECS account

1. Connect to the university VPN when off campus. Open the EECS Linux account associated with `mdjouadi` through the university-supported SFTP/SCP service, or its mapped network share. Use the host/share supplied for that account; the public website hostname is not a verified SFTP endpoint.
2. Back up the existing `~/webhome/` contents to a location outside `webhome` before replacing them.
3. Copy the **contents** of `utk-upload/` directly into `~/webhome/`, overwriting the current `index.html` and matching assets. Alternatively, upload and extract the upload ZIP there, then remove the ZIP from the public directory. Do not nest `utk-upload/` under `webhome/`.
4. Files need mode `644` and directories `755`, or the equivalent EECS `userweb` permissions. Files copied through the supported mapped share receive its group permissions.
5. Open the target URL and check Home, Research, People, Publications, Projects, Teaching, News, Contact, the portrait, publication search, and light/dark mode at desktop and phone widths. Reload without the browser cache if old styling appears.

The [EECS Personal User Web Pages guide](https://help.eecs.utk.edu/knowledge-base/linux-topics/user-websites) documents `~/webhome`, upload methods, VPN access, and permissions.

The generated manifest lists every new public file. Remove obsolete public files only after comparing them with the backed-up old site. Existing PDF, paper, and course URLs have not been inventoried because the old site could not be fetched in this session. Preserve such files until their inbound links are checked. No server-side deletion or upload has been performed here.

## Rebuild after content changes

```sh
bundle install
python -m pip install nbconvert pyyaml
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.utk.yml --destination _site-utk
python bin/package_utk.py --built _site-utk --output dist
```

Install ImageMagick before building. Use a new or empty output directory; the packager refuses to mix a new release with stale files. It checks pages, local links and fragments, responsive image sources, CSS fonts/images, canonical URLs, feed/sitemap/robots URLs, and every ZIP member against a SHA-256 manifest.

The build-only GitHub workflow on `utk-publishing-copy-20261025` provides an alternative when Ruby is unavailable locally. Download its `UTK-website-upload` artifact. This branch does not deploy to GitHub Pages or change `main`.

## Remaining readiness checks

The package can be prepared and checked without an EECS login. Actual replacement still requires access to `mdjouadi`'s `webhome`. Browser appearance and old-site legacy URLs need the live checks above. Grant-derived theme updates remain pending readable funded-project records; see `CONTENT_SOURCES.md`.
