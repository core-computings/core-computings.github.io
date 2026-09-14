"""Sphinx configuration for the CORE documentation website."""

project = "CORE"
author = "CORE contributors"
copyright = "2026, CORE contributors"
extensions = ["myst_parser"]
root_doc = "index"
exclude_patterns = ["_build"]
templates_path = ["_templates"]
myst_heading_anchors = 3

html_theme = "pydata_sphinx_theme"
html_title = "CORE Documentation"
html_baseurl = "https://core-computings.github.io/"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_sidebars = {"**": ["core-nav.html"]}
html_theme_options = {
    "logo": {"text": "CORE"},
    "navbar_center": [],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "CORE on GitHub",
            "url": "https://github.com/chuzcjoe/CORE",
            "icon": "fa-brands fa-github",
        }
    ],
    "secondary_sidebar_items": ["page-toc", "edit-this-page"],
    "use_edit_page_button": True,
    "show_prev_next": True,
    "footer_start": ["copyright"],
    "footer_end": ["theme-version"],
}
html_context = {
    "github_user": "core-computings",
    "github_repo": "core-computings.github.io",
    "github_version": "main",
    "doc_path": "docs",
}


def add_chapter_breadcrumbs(app, pagename, templatename, context, doctree):
    """Include toctree chapter captions in the page's full navigation path."""
    from sphinx import addnodes

    relations = app.env.collect_relations()
    if pagename not in relations or pagename == app.config.root_doc:
        return

    ancestry = []
    child = pagename
    while relations[child][0] is not None:
        parent = relations[child][0]
        ancestry.append((parent, child))
        child = parent

    breadcrumbs = []
    for parent, child in reversed(ancestry):
        if parent != app.config.root_doc:
            breadcrumbs.append({
                "link": app.builder.get_relative_uri(pagename, parent),
                "title": app.env.titles[parent].astext(),
            })
        for tree in app.env.get_doctree(parent).findall(addnodes.toctree):
            if child in tree.get("includefiles", []) and tree.get("caption"):
                breadcrumbs.append({"link": None, "title": tree["caption"]})
                break
    context["parents"] = breadcrumbs


def setup(app):
    app.connect("html-page-context", add_chapter_breadcrumbs)
