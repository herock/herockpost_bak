# -*- encoding: utf-8 -*-
# This is your configuration file.  Please write valid python!
# See http://posativ.org/acrylamid/conf.py.html

LANG = 'en'
# ENCODING = 'utf-8'

SITENAME = 'Herock Post'
SLOGAN = 'Blog让独处更有趣'
WWW_ROOT = 'http://www.herockpost.com/'

AUTHOR = 'herock'
EMAIL = 'herock@gmail.com'

FILTERS = ['markdown+codehilite(css_class=highlight)', 'hyphenate', 'h1']
VIEWS = {
    '/': {'filters': 'summarize', 'view': 'index',
          'pagination': '/page/:num'},

    '/:year/:month/:day/:slug/': {'view': 'entry'},

    '/tag/:name/': {'filters': 'summarize', 'view': 'tag',
                    'pagination': '/tag/:name/:num'},

    '/:year/': {'view': 'archvie'},
    '/:year/:month/': {'view': 'archvie'},
    '/:year/:month/:day/': {'view': 'archvie'},

    # per tag Atom or RSS feed. Just uncomment to generate them.

    # '/tag/:name/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atompertag'},
    # '/tag/:name/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rsspertag'},

    '/atom/': {'filters': ['h2', 'nohyphenate'], 'view': 'atom'},
    '/rss/': {'filters': ['h2', 'nohyphenate'], 'view': 'rss'},

    '/articles/': {'view': 'articles'},

    '/sitemap.xml': {'view': 'sitemap'},
    '/search/': {'view': 'search', 'filters': 'strip+pre'},


    # Here are some more examples

    # # '/:slug/' is a slugified url of your static page's title
    # '/:slug/': {'view': 'page'}

    # # '/atom/full/' will give you a _complete_ feed of all your entries
    # '/atom/full/': {'filters': 'h2', 'view': 'atom', 'num_entries': 1000},

    # # a feed containing all entries tagges with 'python'
    # '/rss/python/': {'filters': 'h2', 'view': 'rss',
    #                  'if': lambda e: 'python' in e.tags}

    # # a full typography features entry including MathML and Footnotes
    # '/:year/:slug': {'filters': ['typography', 'Markdown+Footnotes+MathML'],
    #                  'view': 'entry'}
}

THEME = 'theme'
ENGINE = 'acrylamid.templates.jinja2.Environment'
DATE_FORMAT = '%d.%m.%Y, %H:%M'
DEPLOYMENT = {
    'blog': 'rsync -ruv $OUTPUT_DIR root@192.155.83.165:/home/imom0/www/herockpost/blog/'
}
