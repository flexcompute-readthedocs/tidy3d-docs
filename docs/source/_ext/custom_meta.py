from sphinx.util import logging
from nbconvert import HTMLExporter
import nbformat
import os
import sys
import re

logger = logging.getLogger(__name__)

def html_page_context(app, pagename, templatename, context, doctree):
    '''
    This function is called by Sphinx when generating HTML pages.
    It updates the 'title' variable in the HTML context dictionary
    with the value of the 'html_title' configuration option.
    '''
    logger.debug('Updating HTML page context')
    print("HELLO-------------------->")
    notebook_path = app.env.doc2path(os.path.abspath("source/" +pagename), base=None)
    if not notebook_path.endswith('.ipynb'):
        return
    # print(list(context.keys()))
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        html_exporter = HTMLExporter()
        (html_body, resources) = html_exporter.from_notebook_node(nb)
        # Modify the HTML title tag to use the notebook's metadata
        metadata = nb['metadata']
        title = metadata.get('title', '')
        description = metadata.get('description', '')
        keywords = metadata.get('keywords', '')
        print(title,description,keywords)
        meta_list = []
        if title:
            context['title'] = title
        if keywords:
            meta_list.append(f'\n<meta itemprop="keywords" content="{keywords}" />')
        if description:
            meta_list.append(f'\n<meta name="description" content="{description}" />')

        context['metatags'] = "\n".join(meta_list)

def setup(app):
    app.connect('html-page-context', html_page_context)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
