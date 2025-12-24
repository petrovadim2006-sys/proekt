``yaml
site_name: Pycowsay Documentation
site_url: https://vadim-petrovich.github.io/docs-ecosystem-project/
theme:
  name: material
  features:
    - navigation.tabs
    - navigation.sections
    - search.suggest
    - search.highlight

nav:
  - Главная: index.md
  - Учебник: tutorial.md
  - Руководства: how-to-guides.md
  - Справочник: reference.md
  - Архитектура: explanation.md

plugins:
  - search

markdown_extensions:
  - admonition
  - codehilite
  - toc:
      permalink: true