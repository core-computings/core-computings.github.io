# Writing documentation

Each topic lives in its own Markdown file. The left sidebar groups these pages
into chapters; headings inside a page appear in the right sidebar.

## Add a page

Create a file in the relevant chapter directory, for example
`docs/getting-started/android.md`:

````markdown
# Android setup

A short introduction to this topic.

## Requirements

Describe the required tools.

## Build

```bash
./scripts/run.sh -t arm64-v8a
```
````

## Add it to the navigation

In `docs/index.md`, add `getting-started/android` to the **Get started**
`toctree`. Entries appear in the same order as the sidebar links. The first
heading in the Markdown file becomes the link title.

````markdown
```{toctree}
:hidden:
:caption: Get started
:maxdepth: 1

getting-started/installation
getting-started/first-example
getting-started/android
```
````

To add a chapter, add another `toctree` with its own `:caption:` and page list.
Use relative Markdown links, such as `[Installation](../getting-started/installation.md)`,
to link between topics. Sphinx converts them to website URLs.

## Preview and publish

From the documentation repository root, with its virtual environment activated:

```bash
python -m sphinx -b html -W --keep-going docs _build/html
python -m http.server 8000 --directory _build/html
```

Open `http://localhost:8000`. Push to `main` to publish; pull requests build the
documentation for validation without deploying it.
