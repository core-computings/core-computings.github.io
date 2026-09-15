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

Each topic is an independent Markdown file, grouped by chapter:

```text
docs/
├── index.md                     # Homepage and chapter navigation
├── getting-started/             # Shared setup and first run
├── vulkan/                      # Main documentation section
│   ├── overview.md
│   ├── context-and-device.md
│   ├── buffers-and-images.md
│   ├── commands-and-sync.md
│   ├── descriptors-and-pipelines.md
│   ├── compute.md
│   ├── rendering.md
│   ├── swapchain-and-presentation.md
│   ├── examples.md
│   └── testing-and-performance.md
├── opengl/overview.md           # Reserved backend section
├── opengles/overview.md         # Reserved backend section
├── opencl/overview.md           # Reserved backend section
├── metal/overview.md            # Reserved backend section
├── development/                 # Project-wide guides
├── conf.py                      # Sphinx and theme settings
├── _static/custom.css
└── _templates/core-nav.html     # Sidebar generated from the toctrees
```

To add a topic, create a Markdown file and list its path (without `.md`) in the
matching `toctree` in `docs/index.md`. Each `:caption:` defines a chapter. The
entry order controls the sidebar order. No HTML or Python edits are needed.
The first `# Heading` is the page title; `##` headings form its right-hand TOC.
See `docs/development/documentation.md` for a complete example.

## Deployment

In the repository's **Settings → Pages**, select **GitHub Actions** as the source.
`.github/workflows/docs.yml` builds pull requests and deploys pushes to `main`.
It can also be run manually from the Actions tab. Build warnings fail the workflow.
No CORE compilation, GPU, or GPU SDK is required to build this website.
