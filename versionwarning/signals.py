# -*- coding: utf-8 -*-

from docutils import nodes
import json
import os

from .banner import VersionWarningBanner

STATIC_PATH = os.path.join(os.path.dirname(__file__), '_static')


def process_version_warning_banner(app, doctree, fromdocname):
    """
    Insert an ``admonition`` with a custom/general message.
    """

    banner = VersionWarningBanner(app, doctree)
    for document in doctree.traverse(nodes.document):
        banner = banner.get_banner_node()
        if isinstance(banner, nodes.Admonition):
            document.insert(0, banner)


def generate_versionwarning_data_json(app, **kwargs):
    """
    Generate the ``versionwarning-data.json`` file.

    This file is included in the output and read by the AJAX request when
    accessing to the documentation and used to compare the live versions with
    the curent one.

    Besides, this file contains meta data about the project, the API to use and
    the banner itself.
    """

    # In Sphinx >= 1.8 we use ``config-initied`` signal which comes with the
    # ``config`` object and in Sphinx < 1.8 we use ``builder-initied`` signal
    # that doesn't have the ``config`` object and we take it from the ``app``
    config = kwargs.pop('config', None)
    if config is None:
        config = app.config

    data = json.dumps({
        'meta': {
            'api_url': config.versionwarning_api_url,
        },
        'banner': {
            'html': config.versionwarning_banner_html,
            'id_div': config.versionwarning_banner_id_div,
            'body_default_selector': config.versionwarning_body_default_selector,
            'body_extra_selector': config.versionwarning_body_extra_selector,
        },
        'project': {
            'slug': config.versionwarning_project_slug,
        },
        'version': {
            'slug': config.version,
        },
    })

    data_path = os.path.join(STATIC_PATH, 'data')
    if not os.path.exists(data_path):
        os.mkdir(data_path)

    with open(os.path.join(data_path, 'versionwarning-data.json'), 'w') as f:
        f.write(data)

    # Add the path where ``versionwarning-data.json`` file and
    # ``versionwarning.js`` are saved
    config.html_static_path.append(STATIC_PATH)