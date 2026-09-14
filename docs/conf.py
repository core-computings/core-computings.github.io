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
html_sidebars = {"**": ["sidebar-nav-bs"], "index": ["core-nav.html"]}
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
    "show_prev_next": False,
    "footer_start": ["copyright"],
    "footer_end": ["theme-version"],
}
html_context = {
    "github_user": "core-computings",
    "github_repo": "core-computings.github.io",
    "github_version": "main",
    "doc_path": "docs",
}
