# Networked Systems Laboratory

Academic laboratory website led by Professor Seddik M. Djouadi at the University of Tennessee, Knoxville. Customized from the existing [al-folio](https://github.com/alshedivat/al-folio) Jekyll template; its layouts, components, styles, dark mode, navigation, and bibliography system are retained.

**Start editing:** [START_HERE.md](START_HERE.md) links directly to every content file. People biographies are in [\_includes/people/](_includes/people/), the roster is in [\_data/people.yml](_data/people.yml), and Home/Projects research cards share the theme files in [\_projects/](_projects/).

## Content

- `_pages/about.md`: laboratory homepage
- `_includes/home/`: existing hero, research cards, featured papers, and news components
- `_pages/research.md` and `_projects/`: research themes with source links
- `_pages/profiles.md`, `_data/people.yml`, and `_includes/people/`: faculty, current students, and alumni
- `_bibliography/papers.bib`: 14 published papers and five separately labeled preprints
- `_news/`: dated publication and preprint announcements
- `_config.yml`: site identity and theme configuration
- `.github/workflows/deploy.yml`: Jekyll build, validation, and GitHub Pages deployment

## Maintenance and publication

See [CONTENT_SOURCES.md](CONTENT_SOURCES.md) for verification details and the laboratory-provided biography source, [PUBLISHING.md](PUBLISHING.md) for deployment instructions, and [VALIDATION.md](VALIDATION.md) for checks performed in this session.

The repository is `h2infinity/h2infinity.github.io`. GitHub Pages publishes at `https://h2infinity.github.io/` after the deployment checks pass. See [PUBLISHING.md](PUBLISHING.md) for deployment details. The existing local `_site/` directory is old output and must not be uploaded as this revision.

## Local preview

```sh
docker compose up --build
```

Visit `http://localhost:8080`. See [PUBLISHING.md](PUBLISHING.md) for native Ruby builds, project repository base paths, and GitHub Pages setup.

## Attribution

Built with [Jekyll](https://jekyllrb.com/) and the [al-folio theme](https://github.com/alshedivat/al-folio). Original theme licensing is retained in [LICENSE](LICENSE). Template demonstrations and unused sample content have been removed; the existing framework, components, and styles are retained.
