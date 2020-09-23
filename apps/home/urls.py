# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url


urlpatterns = patterns('home.views',
	# API
    url(r'^get_stats$', 'get_stats', name='get_stats'),
    url(r'^delete$', 'delete', name='delete'),
    # GET
    url(r'^consult/(?P<identifier>[^/]*)/$', 'consult', name='consult'),
    url(r'^confirm/(?P<identifier>[^/]*)/$', 'confirm', name='confirm'),
    url(r'^edit/(?P<identifier>[^/]*)/$', 'edit', name='edit'),        
    url(r'^unsubscribe/(?P<identifier>[^/]*)/$', 'unsubscribe', name='unsubscribe'),    
    url(r'^', 'homepage', name='homepage'),
)