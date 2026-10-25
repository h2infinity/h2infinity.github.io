---
layout: about
title: Home
permalink: /
subtitle: Systems, control, and computation · University of Tennessee, Knoxville
description: Networked Systems Laboratory — research in robust and distributed control, nonlinear dynamics, and connected engineering systems.

selected_papers: false # rendered in a custom homepage section below
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # rendered in a custom homepage section below
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

{% include home/hero.liquid %}

The **Networked Systems Laboratory**, led by [Professor Seddik M. Djouadi]({{ '/people/' | relative_url }}), studies how interconnected dynamical systems can be modeled, coordinated, and controlled under uncertainty. Based in the Min H. Kao Department of Electrical Engineering and Computer Science at the University of Tennessee, Knoxville, our work connects mathematical control theory with energy, communications, fluid dynamics, and autonomous systems.

Our mission is to develop useful models and decision methods for systems whose components share limited information and face uncertain disturbances. Recent contributions include cluster-based reduced-order models, distributed optimal control, and learning methods for power-grid security assessment. Explore our [research]({{ '/research/' | relative_url }}) and [publications]({{ '/publications/' | relative_url }}) for the methods, applications, and supporting papers.

{% include home/research_areas.liquid %}

{% include home/featured_publications.liquid %}

{% include home/recent_news.liquid %}
