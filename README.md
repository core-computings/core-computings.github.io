# CORE Documentation

Documentation website for [CORE](https://github.com/chuzcjoe/CORE), built with
Sphinx, MyST Markdown, and the PyData Sphinx Theme.

Website: https://core-computings.github.io/

## Local preview

With Python 3.12 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m sphinx -b html -W --keep-going docs _build/html
python -m http.server 8000 --directory _build/html
```

Open http://localhost:8000. Rebuild after editing the documentation.

## Editing

- `docs/index.md`: the initial, single-page documentation preview.
- `docs/conf.py`: Sphinx and theme settings.
- `docs/_static/custom.css`: visual customizations.
- `docs/_templates/core-nav.html`: navigation for the preview page.

To expand the site, add Markdown files under `docs/` and include them in a MyST
`toctree` in `docs/index.md`. Replace the preview's custom sidebar with the theme's
`sidebar-nav-bs` template in `html_sidebars` when adding page-based navigation.

## Deployment

In the repository's **Settings → Pages**, select **GitHub Actions** as the source.
`.github/workflows/docs.yml` builds pull requests and deploys pushes to `main`.
It can also be run manually from the Actions tab. Build warnings fail the workflow.
No CORE compilation, GPU, or GPU SDK is required to build this website.
