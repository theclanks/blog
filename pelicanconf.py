#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The_Clanks'
SITENAME = u'Othni Blog'
SITEURL = 'http://theclanks.github.io/blog'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'pt'

THEME = './themes/themes/tuxlite_tbs'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
          ('Blogalizado', 'http://www.blogalizado.com.br/'),
          ('NixCraft', 'http://www.cyberciti.biz/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/theclanks'),)

DISQUS_SITENAME = 'othniblog'

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
