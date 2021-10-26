#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import datetime

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# -- Project information -----------------------------------------------------

project = 'Project Raijin'
author = 'Project Raijin Developers & Contributors'
copyright = f'2021-{datetime.datetime.now().year}, {author}'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_nb',
]

# Define what extensions will parse which kind of source file
source_suffix = {
    '.myst': 'myst-nb',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_documatt_theme'

# Logo & Title
html_logo = '_static/images/logos/GeoCAT_Final_Logos-01.svg'
html_title = ''

# Favicon
html_favicon = '_static/images/icons/favicon.ico'

# Permalinks Icon
html_permalinks_icon = '<i class="bi bi-link"></i>'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']

# HTML sphinx_bootstrap_theme Theme-specific Options
html_theme_options = {

}

# # Disable sidebars on all Portal Pages
# html_sidebars = {
#     '**': [],
# }


# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ('http', 'https', 'mailto')
jupyter_execute_notebooks = 'off'

# CUSTOM SCRIPTS ==============================================================

# Copy root files into content pages ------------------------------------------
