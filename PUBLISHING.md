# Publish the laboratory website

The project retains the existing al-folio/Jekyll architecture. `.github/workflows/deploy.yml` builds the existing Gemfile and plugins, validates source and generated HTML, uploads a Pages artifact, and deploys through GitHub Pages Actions. No personal access token is stored in this repository.

## Repository and address

- GitHub repository: `h2infinity/h2infinity.github.io`
- Website: `https://h2infinity.github.io/`
- Branch: `main`
- Pages source: **GitHub Actions**

The existing repository was renamed successfully (repository ID `1200937480`); no new website architecture or hosting provider was introduced. The workflow derives its URL and base path from the current repository name. `_config.yml` and `_config.github-pages.yml` both target the root address.

## Edit and deploy

1. Use [START_HERE.md](START_HERE.md) to find the content file. Edit Markdown biographies, the YAML roster or Markdown research themes, BibTeX publications, or dated news as appropriate.
2. Commit changes to `main`. **Actions > Deploy site** validates source, builds the production Jekyll site, checks generated routes and links, and deploys after those checks pass. Pull requests build without publishing.
3. To rebuild without a content change, use **Actions > Deploy site > Run workflow** on `main`.
4. Confirm both the build and deployment jobs succeed. Inspect the public home, research, people, publications, projects, teaching, news, and contact pages at desktop and mobile widths.

The prior cleanup deployment passed in [run 40149849042](https://github.com/h2infinity/h2infinity.github.io/actions/runs/40149849042). Current deployment status is available in the repository's Actions tab.

The local `.git/config` still points to the original `hban29/hban29.github.io` remote and has not been modified because that metadata is read-only in this environment. When using Git locally, set the remote to `https://github.com/h2infinity/h2infinity.github.io.git` before pushing. Connected GitHub tool updates target the renamed repository directly.

## Maintenance checks and local preview

The retained deployment, formatting, CodeQL, and development-setup workflows support the laboratory site. Template container-publishing, sample-CV generation, citation scraping, automatic TOC editing, and obsolete report workflows have been removed. Formatting uses the checked-in npm lockfile via `npm ci`.

```sh
python -m pip install pyyaml
python bin/validate_site.py
npm ci
npx prettier . --check
docker compose up --build
```

Open `http://localhost:8080` for the Docker preview. Native Ruby builds remain available:

```sh
bundle install
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.github-pages.yml
python bin/validate_site.py --built _site
```

The workflow validates project builds using `--baseurl "$SITE_BASEURL"`. A fresh `_site/` produced by a successful build is the deployable artifact; the old local output must not be uploaded.

The UTK profile remains in `_config.utk.yml`. GitHub Pages publication does not modify the university-hosted site.
