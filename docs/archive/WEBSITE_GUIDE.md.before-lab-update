# WEBSITE GUIDE

## 1. Introduction

This repository powers an academic website based on the al-folio Jekyll template, customized for your research profile and content style.

Primary public profile target:

- UTK profile: https://web.eecs.utk.edu/~mdjouadi/

### What this website is

- A static academic website for biography, research, publications, news, and professional links.
- Content-first: most updates are done by editing Markdown and BibTeX files.
- Theme-based: layout and components come from al-folio (`_layouts/`, `_includes/`, `_sass/`).

### Tech stack

- Jekyll (Ruby static site generator)
- Markdown + Liquid templates
- BibTeX via `jekyll-scholar` for publications
- Git and GitHub for version control/deployment
- GitHub Pages-compatible workflow

## 2. Project Structure

These are the most important directories for day-to-day maintenance.

### `_pages/`

- Purpose: top-level website pages (home, research, publications, CV, contact, etc.).
- In this repo, homepage content is controlled by `_pages/about.md` with `permalink: /`.
- Navigation visibility is generally page-level via frontmatter (`nav: true`, `nav_order`).

### `_publications/`

- Purpose: curated publication pages grouped by decade/period (for custom lists).
- Current examples: `2000s.md`, `2010s.md`, `2020s.md`.
- Note: full publications page is primarily generated from BibTeX (`_bibliography/papers.bib`) via `jekyll-scholar`.

### `_news/`

- Purpose: short announcement entries.
- Each file is a dated/inline post-like Markdown file with frontmatter.
- Rendered on `/news/` and also on homepage (through custom include).

### `_layouts/`

- Purpose: page templates used by frontmatter `layout:`.
- This repo uses `_layouts/about.liquid` as the homepage layout engine.
- If you need structural page-wide changes (header order, social block location, section wrappers), edit layouts.

### `_includes/`

- Purpose: reusable components used by pages and layouts.
- Your homepage is modularized in `_includes/home/`:
  - `hero.liquid`
  - `research_areas.liquid`
  - `featured_publications.liquid`
  - `recent_news.liquid`
- Reusing include files is the preferred way to add/maintain sections.

### `assets/`

- Purpose: static assets (images, pdfs, icons, additional resources).
- Typical usage:
  - `assets/img/` for profile and section images
  - publication/supporting files as needed

## 3. Running The Website Locally

You can run locally in two ways. For quick consistency, Docker is easiest. For direct editing/debugging, Ruby+Bunder works well.

### Option A (Recommended): Docker

```bash
docker compose pull
docker compose up
```

Then open:

- http://localhost:8080

Stop with `Ctrl+C`, then:

```bash
docker compose down
```

### Option B: Native Ruby + Bundler

#### Install prerequisites (Linux)

```bash
sudo apt-get update
sudo apt-get install -y ruby-full build-essential zlib1g-dev imagemagick
```

Optional but useful for notebook-related plugins:

```bash
python3 -m pip install --upgrade pip nbconvert jupyter
```

#### Install gems and serve

```bash
gem install bundler
bundle install
bundle exec jekyll serve --livereload --port 4000
```

Then open:

- http://localhost:4000

### Common troubleshooting

1. Port already in use

```bash
docker compose down
# or find/kill process on port 4000/8080
```

2. YAML parse errors

- Usually indentation or unquoted special characters in `_config.yml` or `_data/*.yml`.
- Quote values containing `:`, `#`, or `&`.

3. Missing dependency/tool errors

- Re-run `bundle install`.
- Ensure ImageMagick is installed (required by configured image pipeline).

4. Site builds but style/scripts look wrong

- Check `url` and `baseurl` in `_config.yml`.
- Hard-refresh browser cache.

## 4. Editing Content

### A. Editing Homepage

#### Main control file

- `_pages/about.md` controls homepage content and section ordering.

It currently includes modular sections:

```liquid
{% include home/hero.liquid %}

...bio text...

{% include home/research_areas.liquid %}
{% include home/featured_publications.liquid %}
{% include home/recent_news.liquid %}
```

#### How to modify key homepage sections

1. Hero section

- Edit `_includes/home/hero.liquid`.
- Update headline, summary text, and CTA buttons.

2. Research section

- Edit `_includes/home/research_areas.liquid`.
- Add/remove cards based on current projects.

3. Featured publications section

- Edit `_includes/home/featured_publications.liquid` for structure.
- Actual featured items are controlled by `selected = {true}` in `_bibliography/papers.bib`.

### B. Adding/Editing Pages

Create a new Markdown file in `_pages/`, for example `_pages/lab.md`:

```markdown
---
layout: page
title: lab
permalink: /lab/
description: Research group overview
nav: true
nav_order: 8
---

## Lab Overview

This page summarizes people, projects, and facilities.

### Current Focus

- Robust control
- Power systems
- Wireless networked systems
```

Notes:

- `nav: true` puts the page in top navigation.
- `nav_order` controls menu ordering.

### C. Adding Publications

In this repo, the canonical publication source is:

- `_bibliography/papers.bib`

Add a new BibTeX entry like this:

```bibtex
@article{doe2026robust,
  title    = {Robust distributed control under communication uncertainty},
  author   = {Doe, Jane and Djouadi, S. M.},
  journal  = {IEEE Transactions on Automatic Control},
  volume   = {71},
  number   = {4},
  pages    = {1234--1248},
  year     = {2026},
  doi      = {10.1109/TAC.2026.1234567},
  pdf      = {doe2026robust.pdf},
  code     = {https://github.com/example/robust-control},
  selected = {true}
}
```

Required practical fields:

- `title`
- `author`
- `year`
- publication venue field (`journal` or `booktitle`)

Recommended fields (for richer output):

- `doi`, `pdf`, `code`, `selected`

Where each field appears:

- Full list on `/publications/` via `{% raw %}{% bibliography %}{% endraw %}`
- Homepage featured list if `selected = {true}`

### D. Adding News/Updates

Add a file in `_news/`, for example `_news/announcement_4.md`:

```markdown
---
layout: post
title: Keynote at Control Systems Workshop
date: 2026-04-01 09:00:00-0400
inline: true
related_posts: false
---

Delivered a keynote on robust control for renewable-rich power networks.
```

News appears:

- On `/news/` (`_pages/news.md` includes `news.liquid`)
- On homepage via `_includes/home/recent_news.liquid`

## 5. Customization

### A. Layout Changes

Important repository-specific note:

- There is no `_layouts/home.html` in this repo.
- Homepage layout behavior is handled by `_layouts/about.liquid` plus `_pages/about.md` and includes in `_includes/home/`.

If you were expecting `_layouts/home.html`, map changes as follows:

- Structural home layout changes -> `_layouts/about.liquid`
- Section-level content blocks -> `_includes/home/*.liquid`
- Page composition/order -> `_pages/about.md`

Example include reuse in any page/layout:

```liquid
{% include home/research_areas.liquid %}
```

### B. Styling

Main style files are in `_sass/`.

For your custom homepage UI, key styles are in:

- `_sass/_components.scss`

Existing classes already defined there include:

- `.home-hero`
- `.home-section`
- `.research-grid`
- `.research-card`
- `.hero-btn`

Typical changes:

- Colors: update CSS variables (theme) and section backgrounds
- Fonts/sizes: adjust heading/body sizes in component blocks
- Spacing: tune `margin`, `padding`, `gap` values

### C. Navigation Menu

Navigation in this repository is page-driven (not a static menu list in `_config.yml`):

- Add page to nav with frontmatter `nav: true`
- Position with `nav_order`

What `_config.yml` does control:

- Navbar behavior (`navbar_fixed`)
- Search toggle (`search_enabled`)
- Dark-mode toggle (`enable_darkmode`)
- Navbar social display (`enable_navbar_social`)

So for practical menu updates:

1. Create/edit page in `_pages/`
2. Set `nav` and `nav_order`
3. Adjust navbar feature flags in `_config.yml` only if needed

## 6. Optional Features

Configured in `_config.yml`.

### Dark mode

- `enable_darkmode: true`
- Toggle appears in header automatically.

### Search

- `search_enabled: true`
- Search button (`ctrl k`) shown in navbar.

### Google Scholar integration

- `jekyll-scholar` is configured under `scholar:`.
- Citation/badge toggles live in `enable_publication_badges`.
- Publication data source is `_bibliography/papers.bib`.

### Analytics

In `_config.yml`:

- `google_analytics` measurement ID field
- `enable_google_analytics` boolean
- Similar flags exist for Cronitor, Pirsch, OpenPanel

To enable Google Analytics:

1. Set `google_analytics: G-XXXXXXXXXX`
2. Set `enable_google_analytics: true`

## 7. Deployment

This repository is designed for GitHub-based deployment workflows.

### Standard update flow

```bash
git add .
git commit -m "Update homepage and publications"
git push origin main
```

### Verify deployment

1. Wait for GitHub Actions build/deploy to complete.
2. Open deployed site URL.
3. Validate:

- homepage sections render
- publications page includes new entries
- news page contains latest announcement
- no broken images or links

### Quick post-deploy checks

- Open browser dev tools console for runtime errors.
- Verify nav links and publication links.
- Confirm CSS changes are live (hard refresh if cached).

## 8. Best Practices

1. Keep content modular

- Prefer `_includes/home/*.liquid` components over large monolithic page files.

2. Use consistent formatting

- Keep frontmatter fields consistent across content types.
- Maintain BibTeX style consistency in `_bibliography/papers.bib`.

3. Test locally before pushing

- Always run Docker or Jekyll serve before commit.
- Check homepage, publications, and news pages after each non-trivial change.

4. Separate content from presentation

- Put text/content in Markdown/BibTeX.
- Put structure in layouts/includes.
- Put visual changes in SCSS.

5. Make small, reviewable commits

- Easier to debug and revert if needed.

## 9. Examples

### Example 1: A page

```markdown
---
layout: page
title: students
permalink: /students/
description: Current and former students
nav: true
nav_order: 6
---

## Current PhD Students

- Student A (topic)
- Student B (topic)

## Alumni

- Student C - now at ...
```

### Example 2: A publication (BibTeX)

```bibtex
@inproceedings{smith2026grid,
  title     = {Distributed resilient control for renewable-rich grids},
  author    = {Smith, Alex and Djouadi, S. M.},
  booktitle = {Proceedings of the American Control Conference},
  year      = {2026},
  pages     = {101--108},
  doi       = {10.23919/ACC.2026.7654321},
  selected  = {true}
}
```

### Example 3: A homepage section include

Create `_includes/home/students_highlight.liquid`:

```liquid
<section class="home-section">
  <h2>Students</h2>
  <ul>
    <li>PhD Student A - robust distributed control</li>
    <li>PhD Student B - cyber-physical security</li>
  </ul>
  <p class="section-link">
    <a href="{{ '/students/' | relative_url }}">See all students</a>
  </p>
</section>
```

Then include it in `_pages/about.md` where desired:

```liquid
{% include home/students_highlight.liquid %}
```

---

## Maintenance Checklist (Quick)

For any update:

1. Edit the right source file (`_pages`, `_news`, `_bibliography`, `_includes`, `_sass`).
2. Run locally (`docker compose up` or `bundle exec jekyll serve`).
3. Verify affected pages.
4. Commit and push.
5. Confirm deployment.
