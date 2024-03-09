"""Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
"""
# pylint: disable=invalid-name,redefined-builtin

# import os
# import sys

# sys.path.append(os.path.abspath('python/python-basic-cert/reverse_and_swap'))
# sys.path.append(os.path.abspath('python/python-basic-cert/implement_multiset'))
# sys.path.append(os.path.abspath('python/simple_array_sum'))
# sys.path.append(os.path.abspath('python/compare_the_triplets'))

author = 'Xander Harris'
autoyaml_root = "."
autoyaml_doc_delimiter = "###"
autoyaml_comment = "#"
autoyaml_level = 10
autoyaml_safe_loader = False
copyright = '2024, Xander Harris'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    '.venv/*',
    '.tmp/*',
    '.pytest_cache/*',
    '.venv/',
]

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_favicon',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.githubpages',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.autoyaml',
    'sphinxemoji.sphinxemoji',
]

favicons = [
    {
        "sizes": "16x16",
        "href": "img/ansible-16x16.png",
    },
    {
        "sizes": "32x32",
        "href": "img/ansible-32x32.png",
    },
    {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "img/ansible-180x180.png",  # use a local file in _static
    },
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']
html_theme = 'sphinx_nefertiti'
html_theme_options = {
    'logo': 'img/ansible-180x180.png',
    'repository_url': 'https://github.com/edwardtheharris/ansible-k8s-ca',
    'repository_name': 'ansible k8s ca',
    "style": "blue",
}
myst_dmath_double_inline = True
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_title_to_header = True
project = 'Ansible Certificate Authority'
release = '0.0.1'
show_authors = True
source_suffix = {
    '.md': 'markdown'
}
templates_path = ['_templates']
