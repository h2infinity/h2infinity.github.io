"""Validate laboratory source content, and optionally a fresh Jekyll build."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"Missing front matter: {path}"
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def bibliography():
    """Read balanced brace-delimited entries without splitting nested titles."""
    text = (ROOT / "_bibliography/papers.bib").read_text(encoding="utf-8")
    entries = {}
    for match in re.finditer(r"@(\w+)\{([^,]+),", text):
        kind, key = match.groups()
        pos, depth = match.end(), 1
        end = pos
        while depth and end < len(text):
            if text[end] == "{":
                depth += 1
            elif text[end] == "}":
                depth -= 1
            end += 1
        assert depth == 0, f"Unbalanced BibTeX: {key}"
        body = text[pos:end - 1]
        fields = {}
        cursor = 0
        while cursor < len(body):
            field = re.search(r"(\w+)\s*=\s*\{", body[cursor:])
            if not field:
                assert not body[cursor:].strip(" \n\r\t,"), f"Invalid BibTeX: {key}"
                break
            start = cursor + field.end()
            stop, level = start, 1
            while level and stop < len(body):
                if body[stop] == "{":
                    level += 1
                elif body[stop] == "}":
                    level -= 1
                stop += 1
            assert level == 0, f"Unbalanced field in {key}"
            fields[field.group(1)] = body[start:stop - 1]
            cursor = stop
        assert key not in entries, f"Duplicate citation key: {key}"
        entries[key] = (kind, fields)
    assert entries, "Empty bibliography"
    return entries


def source_check():
    config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
    assert config["title"] == "Networked Systems Laboratory"
    assert config["url"] == "https://web.eecs.utk.edu"
    assert config["baseurl"] == "/~mdjouadi"
    override = yaml.safe_load((ROOT / "_config.utk.yml").read_text(encoding="utf-8"))
    assert override["url"] == config["url"] and override["baseurl"] == config["baseurl"]
    exclusions = [p.rstrip("/") for p in config["exclude"]]

    def excluded(path):
        return any(path == e or path.startswith(e + "/") for e in exclusions)

    paths = [p for folder in ("_pages", "_projects", "_news")
             for p in (ROOT / folder).glob("*.md")
             if not excluded(p.relative_to(ROOT).as_posix())]
    routes = set()
    for path in paths:
        data = frontmatter(path)
        layout = data.get("layout")
        assert (ROOT / f"_layouts/{layout}.liquid").exists(), f"Unknown layout: {path}"
        if data.get("permalink"):
            assert data["permalink"] not in routes, f"Duplicate route: {path}"
            routes.add(data["permalink"])
        text = path.read_text(encoding="utf-8")
        for bad in ("Albert Einstein", "example_pdf", "your cool projects", "Write your biography", "hban29"):
            assert bad not in text, f"Template content in {path}: {bad}"
        assert "\ufffd" not in text and "?cole" not in text, f"Text encoding error: {path}"
        for include in re.findall(r"{%\s*include\s+([\w/.-]+)", text):
            assert (ROOT / "_includes" / include).exists(), f"Missing include: {include}"
        for route in re.findall(r"['\"](/[^'\"]*/)['\"]\s*\|\s*relative_url", text):
            assert route in routes or any(frontmatter(p).get("permalink") == route for p in paths), f"Unknown route: {route}"
    assert (ROOT / "assets/img/djouadi.jpg").exists()
    assert (ROOT / "assets/img/favicon.svg").exists()
    assert config["collections"]["publications"]["output"] is False
    entries = bibliography()
    dois = set()
    for key, (kind, fields) in entries.items():
        for required in ("title", "author", "year", "doi", "html", "publication_status"):
            assert fields.get(required), f"Missing {required}: {key}"
        assert re.fullmatch(r"10\.\d{4,9}/\S+", fields["doi"]), f"Invalid DOI: {key}"
        assert fields["doi"].lower() not in dois, f"Duplicate DOI: {key}"
        dois.add(fields["doi"].lower())
        if fields["publication_status"] == "preprint":
            assert kind == "misc" and fields.get("arxiv") and "Preprint" in fields["note"]
        else:
            assert fields["publication_status"] == "published"
            assert fields.get("journal") or fields.get("booktitle"), f"Missing venue: {key}"
    roster = yaml.safe_load((ROOT / "_data/people.yml").read_text(encoding="utf-8"))
    members = [member for group in roster["groups"] for member in group["members"]]
    assert len({member["id"] for member in members}) == len(members), "Duplicate person ID"
    for member in members:
        assert (ROOT / "_includes" / member["bio"]).is_file(), f"Missing biography: {member['name']}"
        assert "\ufffd" not in (ROOT / "_includes" / member["bio"]).read_text(encoding="utf-8")
        if member.get("image"):
            assert member.get("alt"), f"Missing portrait alt text: {member['name']}"
            assert (ROOT / "assets/img" / member["image"]).is_file()
    nav = sorted((frontmatter(p)["nav_order"], frontmatter(p)["title"]) for p in paths if frontmatter(p).get("nav"))
    assert len({n for n, _ in nav}) == len(nav), "Duplicate navigation order"
    preprints = sum(f["publication_status"] == "preprint" for _, f in entries.values())
    print(f"Source checks passed: {len(paths)} content files; {len(entries) - preprints} published papers; {preprints} preprints.")
    print("Navigation: Home, " + ", ".join(title for _, title in nav))


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.images = [], set(), []
        self.scripts, self.styles = [], []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for attr in ("href", "src"):
            if attrs.get(attr):
                self.links.append(attrs[attr])
        if attrs.get("srcset"):
            self.links.extend(part.strip().split()[0] for part in attrs["srcset"].split(",") if part.strip())
        if tag == "img":
            self.images.append(attrs)
        if tag == "script" and attrs.get("src"):
            self.scripts.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.styles.append(attrs.get("href", ""))


def built_check(destination, baseurl, origin=""):
    destination = destination.resolve()
    baseurl = baseurl.rstrip("/")
    for route in ("index.html", "research/index.html", "people/index.html", "publications/index.html", "projects/index.html", "contact/index.html"):
        assert (destination / route).is_file(), f"Missing generated page: {route}"
    parsed = {}
    for file in destination.rglob("*.html"):
        page = Page()
        text = file.read_text(encoding="utf-8")
        page.feed(text)
        parsed[file] = page
        assert "{{" not in text and "{%" not in text, f"Unrendered Liquid: {file}"
        if origin:
            assert f'rel="canonical" href="{origin}{baseurl}/' in text, f"Incorrect canonical URL: {file}"
    for file, page in parsed.items():
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith("/"):
                assert not baseurl or path == baseurl or path.startswith(baseurl + "/"), f"Link escapes project base: {href} in {file}"
                target = destination / path[len(baseurl):].lstrip("/")
            else:
                target = file.parent / path if path else file
            if target.is_dir():
                target = target / "index.html"
            target = target.resolve()
            assert target.is_relative_to(destination), f"Link escapes site: {href}"
            assert target.exists(), f"Broken local link: {href} in {file.relative_to(destination)}"
            if url.fragment and target in parsed:
                assert unquote(url.fragment) in parsed[target].ids, f"Broken anchor: {href}"
    home = (destination / "index.html").read_text(encoding="utf-8")
    pubs = (destination / "publications/index.html").read_text(encoding="utf-8")
    assert "Networked Systems Laboratory" in home
    assert "Recent Publications" in home
    for key in bibliography():
        assert key in pubs, f"Bibliography entry omitted by query: {key}"
    for entry, (_, fields) in bibliography().items():
        if fields.get("selected") == "true":
            assert entry in home, f"Featured paper missing: {entry}"
    assert not (destination / "blog").exists(), "Template blog was published"
    assert not (destination / "books").exists(), "Template book collection was published"
    assert not (destination / "assets/json/resume.json").exists(), "Template resume was published"
    people = (destination / "people/index.html").read_text(encoding="utf-8")
    roster = yaml.safe_load((ROOT / "_data/people.yml").read_text(encoding="utf-8"))
    for group in roster["groups"]:
        for member in group["members"]:
            assert member["id"] in parsed[destination / "people/index.html"].ids, f"Missing person: {member['name']}"
    assert "Electrical Engineering" in people and "alumni" in people
    projects = (destination / "projects/index.html").read_text(encoding="utf-8")
    assert "funded-projects" not in projects and "Funding &amp; projects" not in projects, "Removed funding section was rendered"
    for file in (ROOT / "_projects").glob("*.md"):
        title = frontmatter(file)["title"]
        assert title in projects and title in home, f"Research theme omitted: {title}"
    home_page = parsed[destination / "index.html"]
    for resource in home_page.scripts + home_page.styles:
        assert not any(unused in resource for unused in ("mdb.min", "mathjax", "polyfill", "masonry", "medium-zoom", "fonts.googleapis")), f"Unused home dependency: {resource}"
    assert "main-content" in home_page.ids
    print(f"Fresh build checks passed: {len(parsed)} HTML pages and their local links.")
    print(f"Home resources: {len(home_page.scripts)} scripts; {len(home_page.styles)} stylesheets; main CSS {(destination / 'assets/css/main.css').stat().st_size:,} bytes.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--built", type=Path)
    parser.add_argument("--baseurl", default="")
    parser.add_argument("--origin", default="")
    args = parser.parse_args()
    source_check()
    if args.built:
        built_check(args.built, args.baseurl, args.origin)
