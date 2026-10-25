# Publish the laboratory website

The project retains the existing al-folio/Jekyll architecture. `.github/workflows/deploy.yml` builds the existing Gemfile and plugins, validates source and generated HTML, uploads a Pages artifact, and deploys through GitHub Pages Actions. No personal access token is stored in this repository.

## Repository and address

- GitHub owner: `h2infinity`
- Existing repository: `h2infinity/hban29.github.io`
- Requested final repository name: `h2infinity.github.io`
- Final site address after renaming and redeploying: `https://h2infinity.github.io/`

The laboratory source was uploaded in commit `d8885df33e6ac8bbdc1d817272db9b09a5ec47d0`. [Deployment run 40149173656](https://github.com/h2infinity/hban29.github.io/actions/runs/40149173656) passed the production Jekyll build, generated-site checks, and Pages deployment. The repository is being reused and cleaned up at the owner's request. The current GitHub connector can update repository contents but has no repository-renaming operation, and no browser is exposed. The final repository name and root address must not be described as active until the rename and subsequent deployment are verified.

## Rename and redeploy

1. Open the repository's **Settings > General** page and change **Repository name** from `hban29.github.io` to `h2infinity.github.io`.
2. Keep **Settings > Pages > Build and deployment > Source** set to **GitHub Actions**.
3. In **Actions > Deploy site**, choose **Run workflow** on `main`. Renaming alone does not rebuild the Pages artifact. Any subsequent source commit to `main` also triggers deployment.
4. Confirm the build and deployment jobs succeed, then inspect the home, research, people, publications, projects, teaching, news, and contact pages at the final address.

The workflow derives `url` and `baseurl` from the current owner and repository. The final user-site name produces an empty base path; the existing project name produces `/hban29.github.io`. `_config.yml` and `_config.github-pages.yml` already target the requested root address. Keep those configurations aligned.

The local `.git/config` still points to the original `hban29/hban29.github.io` remote and has not been modified. Update it to `https://github.com/h2infinity/h2infinity.github.io.git` only after the rename is confirmed.

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
