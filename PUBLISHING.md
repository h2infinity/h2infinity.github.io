# Publish the laboratory website

The project remains the existing al-folio/Jekyll website. There is one automatic publishing workflow: `.github/workflows/deploy.yml`. It builds the full Jekyll plugin configuration, checks generated local links and bibliography entries, and deploys through GitHub Pages Actions. It does not require a personal access token stored in the repository.

## Intended destination

- GitHub owner: `h2infinity`
- Recommended user-site repository: `h2infinity.github.io`
- Intended address: `https://h2infinity.github.io/`

This address is a configuration target, not a verified live deployment. This session did not have an authenticated GitHub connection, Git/GitHub CLI, or an exposed browser. Direct shell network access to GitHub was denied. No remote repository, branch, Pages settings, or live university site has been changed.

The local `.git/config` still points to `hban29/hban29.github.io`; it is deliberately preserved until the correct destination can be inspected. Do not push to that origin when intending to publish to `h2infinity`.

## Publish with authenticated GitHub access

1. Install and connect the GitHub integration to the `h2infinity` account, or use an authenticated Git/GitHub CLI environment.
2. Inspect `h2infinity/h2infinity.github.io` before creating or updating it. Preserve any existing unrelated work. Use the source files in this project, not the pre-existing `_site/` output.
3. In the destination repository, set **Settings → Pages → Build and deployment → Source** to **GitHub Actions**. This matches the repository's existing Actions deployment approach.
4. Push the source to `main`. The `Deploy site` workflow installs the existing Ruby/Jekyll dependencies, validates source, builds the site, checks generated output, uploads the artifact, and deploys it. Pull requests build and validate without deploying.
5. Confirm the workflow succeeds, then inspect the published home, research, people, publications, projects, teaching, news, and contact pages on desktop and mobile, including dark mode and publication search.

The workflow derives `url` and `baseurl` from the actual owner and repository name. The user-site repository gets an empty base path; a project repository gets `/<repository>`. For manual builds of a project repository, pass the corresponding `--baseurl /repository` value. For a custom domain, update the URL configuration and workflow together before deploying.

## Local validation and preview

The repository recommends Docker; with Docker installed:

```sh
docker compose up --build
```

Open `http://localhost:8080`. The native Ruby alternative is:

```sh
bundle install
bundle exec jekyll serve --config _config.yml,_config.github-pages.yml --port 4000
```

Source checks and fresh-build checks:

```sh
python -m pip install pyyaml
python bin/validate_site.py
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.github-pages.yml
python bin/validate_site.py --built _site
```

Use the existing installed Prettier executable, or install the dependencies with `npm ci`:

```sh
node node_modules/prettier/bin/prettier.cjs . --check
```

The former duplicate `jekyll.yml` deployment is archived. CV generation and citation scraping are manual-only because the laboratory site does not publish the template CV or scraped citation metrics. `bin/deploy` is a legacy branch-publishing helper; use the Actions workflow documented here for the configured site.

The UTK publishing profile remains available as `_config.utk.yml`. Uploading files to UTK requires separate university-host access; GitHub Pages publication will not replace the university-hosted site automatically.
