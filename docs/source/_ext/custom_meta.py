from sphinx.util import logging
from nbconvert import HTMLExporter
import nbformat
from bs4 import BeautifulSoup
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
    notebook_path = app.env.doc2path(os.path.abspath("source/" +pagename), base=None)
    if notebook_path.endswith('.ipynb'):
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
                meta_list.append(f'\n<meta name="keywords" content="{keywords}" />')
            if description:
                meta_list.append(f'\n<meta name="description" content="{description}" />')

            context['metatags'] = "\n".join(meta_list)
    if notebook_path.endswith('.rst') and hasattr(doctree, 'traverse'):
        for node in doctree.traverse():
            if node.tagname == "meta":
                soup = BeautifulSoup(node.pformat(), 'html.parser')
                meta = soup.find('meta')
                if meta.get('name') == 'html_seo_title':
                    context['title'] = meta.get('content')

def setup(app):
    app.connect('html-page-context', html_page_context)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
