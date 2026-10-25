# Edit the laboratory website

The site uses the existing Jekyll/al-folio template. Most content changes require only Markdown or YAML; no build-system or template changes are needed.

| What to change                      | File or folder                                                                                       |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Laboratory introduction             | [\_pages/about.md](_pages/about.md)                                                                  |
| Home hero and buttons               | [\_includes/home/hero.liquid](_includes/home/hero.liquid)                                            |
| People names, roles, order, groups  | [\_data/people.yml](_data/people.yml)                                                                |
| Individual biographies              | [\_includes/people/](_includes/people/) - one named Markdown file per person                         |
| Alumni and historical affiliations  | [\_includes/people/alumni.md](_includes/people/alumni.md)                                            |
| Research-theme project pages        | [\_projects/](_projects/)                                                                            |
| Research overview                   | [\_pages/research.md](_pages/research.md)                                                            |
| Publications                        | [\_bibliography/papers.bib](_bibliography/papers.bib)                                                |
| News                                | [\_news/](_news/)                                                                                    |
| Contact and teaching                | [\_pages/contact.md](_pages/contact.md), [\_pages/teaching.md](_pages/teaching.md)                   |
| Shared layout and responsive styles | [\_sass/\_layout.scss](_sass/_layout.scss), [\_sass/\_components.scss](_sass/_components.scss)       |
| Colors and typography               | [\_sass/\_variables.scss](_sass/_variables.scss), [\_sass/\_typography.scss](_sass/_typography.scss) |
| Optional features and site identity | [\_config.yml](_config.yml)                                                                          |

## People

Edit a person's named Markdown file under `_includes/people/`. The paragraph before `<!--more-->` is always visible. Additional paragraphs after that marker appear in an accessible, native disclosure. Keep the marker on its own line. The director biography is fully displayed. Photos are optional; no placeholder portraits are generated.

Names, degree fields, and appointments belong in `_data/people.yml`. Update both the roster role and the biography when an appointment changes. Current students and alumni remain separate. The latest laboratory-provided `People_bio.txt` was used for this revision; Hemanta Ban is listed in Electrical Engineering.

## Research themes

Edit a Markdown file under `_projects/`. Its `title`, `description`, and `importance` front matter determine the research cards on both Home and Projects, so there is one source for their labels and summaries. The Markdown body is the detailed theme page. Add a new file in the same format to add another theme; retain established routes when changing existing files. The longer research overview is in `_pages/research.md`.

Use verified funded-project topics to revise these research themes rather than adding a separate funding or awards section. The supplied UTK grants page, including the detailed query URL, remained unreadable through this session's tools. New grant-derived topics must wait for readable official records or an owner-provided list; the displayed themes currently describe the already sourced research.

## Layout and loading

The site footer shows only **© Networked Systems Laboratory**. Its markup is in `_includes/footer.liquid`, using the laboratory title from `_config.yml`. Theme licensing and source attribution remain in the repository's LICENSE and README.

The existing Bootstrap grid, navigation, bibliography, dark mode, and Jekyll layouts remain. System fonts avoid external font downloads. Material Design assets, math rendering, image zoom, Masonry, and scrolling animations are off by default. Set `math: true`, `code: true`, or `academic_icons: true` in a page's front matter when it needs those features. Optional legacy styles can be enabled with `enable_extended_styles` in `_config.yml`.

## Save and publish the UTK copy

Edit this copy's content files, then rebuild and package using [PUBLISHING.md](PUBLISHING.md). Upload only the generated `utk-upload/` contents to the account's `~/webhome/`. The default URL is `https://web.eecs.utk.edu/~mdjouadi/`.

The original `../control-group/` source and GitHub Pages website remain unchanged. This copy's build-only workflow runs on the isolated UTK branch and does not publish to Pages.

For local source checks, use the locked formatter from the original source, or install it here:

```sh
python bin/validate_site.py
npm ci
npx prettier . --check
```

The retained Docker setup can preview this copy when Docker is installed. Publication facts and their limits remain documented in [CONTENT_SOURCES.md](CONTENT_SOURCES.md).
