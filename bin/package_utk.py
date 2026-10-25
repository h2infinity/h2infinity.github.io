"""Export a validated UTK build with only the files used by the website."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
from urllib.parse import unquote, urlsplit
import zipfile

from validate_site import Page, ROOT, built_check, source_check

ORIGIN = "https://web.eecs.utk.edu"
BASEURL = "/~mdjouadi"
NAME = "Networked-Systems-Laboratory-UTK-upload"


def local_target(reference, parent, build):
    url = urlsplit(reference)
    if url.scheme or url.netloc:
        if f"{url.scheme}://{url.netloc}" != ORIGIN:
            return None
        if not (url.path == BASEURL or url.path.startswith(BASEURL + "/")):
            return None
    path = unquote(url.path)
    if not path:
        return None
    if path.startswith("/"):
        assert path == BASEURL or path.startswith(BASEURL + "/"), f"Path escapes UTK base: {reference}"
        target = build / path[len(BASEURL):].lstrip("/")
    else:
        target = parent / path
    target = target.resolve()
    assert target.is_relative_to(build), f"Path escapes build: {reference}"
    if target.is_dir():
        target /= "index.html"
    assert target.is_file(), f"Missing upload dependency: {reference}"
    return target


def collect_files(build):
    files = set(build.rglob("*.html"))
    for name in ("robots.txt", "sitemap.xml", "sitemap.xsl", "feed.xml"):
        if (build / name).is_file():
            files.add(build / name)
    pending = list(files)
    while pending:
        path = pending.pop()
        references = []
        if path.suffix == ".html":
            page = Page()
            page.feed(path.read_text(encoding="utf-8"))
            references = page.links
        elif path.suffix == ".css":
            text = path.read_text(encoding="utf-8")
            references = [m.group(1).strip(" \t\n\"'") for m in re.finditer(r"url\(([^)]+)\)", text)]
            references += re.findall(r'@import\s+[\"\']([^\"\']+)', text)
        elif path.suffix == ".js":
            text = path.read_text(encoding="utf-8")
            references = re.findall(r'(?:from\s+|import\s*\(?\s*)[\"\'](\.?\.?/[^\"\']+)', text)
        for reference in references:
            target = local_target(reference, path.parent, build)
            if target and target not in files:
                files.add(target)
                pending.append(target)
    return files


def package(build, output):
    build, output = build.resolve(), output.resolve()
    assert build.is_dir() and not output.is_relative_to(build), "Output must be outside the build"
    assert not output.exists() or not any(output.iterdir()), "Use an empty output directory to avoid stale files"
    source_check()
    built_check(build, BASEURL, ORIGIN)
    files = collect_files(build)
    upload = output / "utk-upload"
    upload.mkdir(parents=True)
    for source in sorted(files):
        relative = source.relative_to(build)
        target = upload / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(ROOT / "LICENSE", upload / "LICENSE")
    built_check(upload, BASEURL, ORIGIN)
    collect_files(upload)  # Also check CSS font/image dependencies in the trimmed copy.
    for name in ("robots.txt", "sitemap.xml", "feed.xml"):
        text = (upload / name).read_text(encoding="utf-8")
        assert ORIGIN + BASEURL in text and "h2infinity.github.io" not in text, f"Wrong publishing URL in {name}"
    records = []
    archive_path = output / f"{NAME}.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(upload.rglob("*")):
            if not path.is_file():
                continue
            relative = path.relative_to(upload).as_posix()
            assert not relative.endswith((".map", ".scss", ".md", ".rb", ".yml")), f"Source file in upload: {relative}"
            content = path.read_bytes()
            records.append({"path": relative, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()})
            info = zipfile.ZipInfo(relative, (2026, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content, compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(archive_path) as archive:
        assert archive.testzip() is None and "index.html" in archive.namelist()
        assert len(archive.namelist()) == len(records)
        for record in records:
            assert hashlib.sha256(archive.read(record["path"])).hexdigest() == record["sha256"]
    digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    (output / f"{NAME}.zip.sha256").write_text(f"{digest}  {archive_path.name}\n", encoding="utf-8")
    (output / "upload-manifest.json").write_text(json.dumps({
        "website": ORIGIN + BASEURL + "/", "destination": "~/webhome/",
        "files": records, "file_count": len(records), "zip_sha256": digest,
    }, indent=2) + "\n", encoding="utf-8")
    shutil.copyfile(ROOT / "PUBLISHING.md", output / "UTK-UPLOAD-INSTRUCTIONS.md")
    print(f"UTK upload ready: {len(records)} files; {archive_path.stat().st_size:,} ZIP bytes; SHA-256 {digest}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--built", type=Path, default=ROOT / "_site-utk")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    package(args.built, args.output)
