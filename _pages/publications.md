---
layout: page
permalink: /publications/
title: Publications
description: Recent journal articles, conference papers, and clearly identified preprints.
nav: true
nav_order: 3
code: true
---

Recent publications and representative earlier work by Professor Djouadi and collaborators. Each entry links to a DOI, publisher, or academic repository. This is a curated bibliography, rather than a complete career publication list. Records checked October 24, 2026.

[Published papers](#published-papers) · [Preprints](#preprints) · [Historical faculty bibliography](https://web.eecs.utk.edu/~mdjouadi/publications.html)

{% include bib_search.liquid %}

## Published papers

<div class="publications">
{% bibliography --query @*[publication_status=published]* %}
</div>

## Preprints

The following are arXiv manuscripts. An arXiv DOI identifies a repository record and does not indicate peer-reviewed publication. Related manuscripts are listed separately by their arXiv identifiers.

<div class="publications">
{% bibliography --query @*[publication_status=preprint]* %}
</div>
