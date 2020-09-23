from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
admin.autodiscover()
from core.views import SiteSitemap

sitemaps = {
    'pages': SiteSitemap(['accueil']),
}

urlpatterns = patterns('',
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^home/', include('home.urls')),
    url(r'^$', include('home.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {'sitemaps': sitemaps}),
    (r'^sitemap-(?P<section>.+)\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name="media"),
)

if settings.DEBUG:
    urlpatterns+= patterns('')  \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
