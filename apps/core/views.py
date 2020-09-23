# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from datetime import datetime

class SiteSitemap(Sitemap):
    def __init__(self, names):
        self.names = names
    def items(self):
        return self.names
    def changefreq(self, obj):
        return 'weekly'
    def priority(self, obj):
        return '1.0'
    def lastmod(self, obj):
        return datetime.now()
    def location(self, obj):
        return reverse(obj)
