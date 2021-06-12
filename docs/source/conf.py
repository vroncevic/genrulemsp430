# -*- coding: utf-8 -*-

project = u'gen_rule'
copyright = u'2016, Vladimir Roncevic <elektron.ronca@gmail.com>'
author = u'Vladimir Roncevic <elektron.ronca@gmail.com>'
version = u'1.0'
release = u'https://github.com/vroncevic/gen_rule/releases'
extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
language = None
exclude_patterns = []
pygments_style = None
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'gen_ruledoc'
latex_elements = {}
latex_documents = [(
    master_doc, 'gen_rule.tex', u'gen\\_rule Documentation',
    u'Vladimir Roncevic \\textless{}elektron.ronca@gmail.com\\textgreater{}',
    'manual'
)]
man_pages = [(
    master_doc, 'gen_rule', u'gen_rule Documentation', [author], 1
)]
texinfo_documents = [(
    master_doc, 'gen_rule', u'gen_rule Documentation',
     author, 'gen_rule', 'One line description of project.',
     'Miscellaneous'
)]
epub_title = project
epub_exclude_files = ['search.html']
