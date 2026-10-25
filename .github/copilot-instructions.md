# UTK laboratory publishing copy

Use the existing Jekyll 4, Ruby 3.3.5, Liquid, Sass, Bootstrap, jekyll-scholar, and ImageMagick setup. Do not redesign the site architecture. Read `AGENTS.md`, `START_HERE.md`, and `PUBLISHING.md`.

This copy targets `https://web.eecs.utk.edu/~mdjouadi/`. Its isolated workflow builds an upload package only. The existing GitHub Pages source and live site must remain unchanged.

```sh
python bin/validate_site.py
npm ci
npx prettier . --check
JEKYLL_ENV=production bundle exec jekyll build --config _config.yml,_config.utk.yml --destination _site-utk
python bin/package_utk.py --built _site-utk --output dist
```

Use a new or empty output directory. Do not commit generated output or dependencies. The final public directory contains rendered pages and their actual dependencies; it does not need Ruby or Jekyll on the university server.
