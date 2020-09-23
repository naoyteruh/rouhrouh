# -*- coding: utf-8 -*-
import os
import sys
import re
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.template.loader import add_to_builtins
import socket
from logging_filters import skip_suspicious_operations

# if socket.gethostname() == 'pc-ekilibr':
DEBUG = True
TEMPLATE_DEBUG = True
# else:
#     DEBUG = False
#     TEMPLATE_DEBUG = False

gettext = lambda s: s

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(PROJECT_DIR)
PREFIX_DIR = os.path.realpath(os.path.join(PROJECT_DIR, '..'))
APPS_DIR = os.path.realpath(os.path.join(PREFIX_DIR, 'apps'))
sys.path.append(APPS_DIR)


ADMINS = (
 ('yoan', 'naoy.teruh@gmail.com'),
 ('yo', 'naoy.teruh@gmail.com')
)

# if socket.gethostname() == 'pc-ekilibr':
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'var/boilerplate.db',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
# else:
#     #EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#     EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
#     EMAIL_HOST = 'mail.gandi.net'
#     EMAIL_PORT = 465
#     EMAIL_HOST_USER = 'yoan.huret@ekilibr-informatique.net'
#     EMAIL_HOST_PASSWORD = 'coyote$59#'

#     #EMAIL_HOST = 'smtp.gmail.com'
#     #EMAIL_PORT = 587
#     #EMAIL_HOST_USER = 'naoy.teruh@gmail.com'
#     #EMAIL_HOST_PASSWORD = 'freeman59'

#     EMAIL_TIMEOUT = 5
#     EMAIL_USE_TLS = True
#     SEND_BROKEN_LINK_EMAILS = False
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#             'NAME': 'rouhrouh',                      # Or path to database file if using sqlite3.
#             'USER': 'postgres',
#             'PASSWORD': 'coyote$59',
#             'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
#             'PORT': '5432',                      # Set to empty string for default.
#         }
#     }

MANAGERS = ADMINS

#DEFAULT_CHARSET='iso-8859-1'
#DEFAULT_CHARSET='utf-8'

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['.ekilibr-informatique.net']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Europe/Paris'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
# LANGUAGES = (
#     'fr-fr',
# )
LANGUAGE_CODE = 'fr-fr'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PREFIX_DIR, 'medias')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/medias/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PREFIX_DIR, 'static')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

COMPRESS_ROOT = STATIC_ROOT
COMPRESS_URL = STATIC_URL

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PREFIX_DIR, 'apps', 'core', 'static'),
    os.path.join(PREFIX_DIR, 'apps', 'home', 'static'),
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    #'django.core.context_processors.static',
    'django.core.context_processors.request',
    #'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    #'core.context_processors.user',
    #'blog.context_processors.debug',
    #'core.context_processors.quotation',
    #'blog.context_processors.userJson',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '_iy779#z8wfe_j%9jft+^#!gi)(qpkes#zflklrllc#++w$@i('

# Precharge des tags dans tous les templates
add_to_builtins('django.contrib.staticfiles.templatetags.staticfiles')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'cms.middleware.page.CurrentPageMiddleware',
    #'cms.middleware.user.CurrentUserMiddleware',
    #'cms.middleware.toolbar.ToolbarMiddleware',
    #'cms.middleware.language.LanguageCookieMiddleware',
    #'cms.middleware.multilingual.MultilingualURLMiddleware'
    'django.middleware.locale.LocaleMiddleware',
    #'dcms.customer_middleware.CustomerMiddleware',
)

ROOT_URLCONF = 'core.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'core.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PREFIX_DIR, 'apps', 'core', 'templates', 'core'),
    os.path.join(PREFIX_DIR, 'apps', 'home', 'templates', 'home'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # Debut cms                             # django CMS itself
    'mptt',                               # utilities for implementing a modified pre-order traversal tree
    'menus',                              # helper for model independent hierarchical website navigation
    'south',                              # intelligent schema and data migrations
    'sekizai',                            # for javascript and css management
    # Fin cms
    'compressor',
    #'social.apps.django_app.default',
    'core',
    'home',
    #'sorl.thumbnail',
    'easy_thumbnails',
    'stdimage'
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        # Define filter
        'skip_suspicious_operations': {
           '()': 'django.utils.log.CallbackFilter',
           'callback': skip_suspicious_operations,
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/debug.log',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false', 'skip_suspicious_operations'],
            # 'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Social Auth 
#AUTHENTICATION_BACKENDS = (
    #'social.backends.open_id.OpenIdAuth',
    #'social.backends.google.GoogleOpenId',
    #'social.backends.google.GoogleOAuth2',
    #'social.backends.google.GoogleOAuth',
    #'social.backends.twitter.TwitterOAuth',
    #'social.backends.facebook.FacebookOAuth2',
    #'django.contrib.auth.backends.ModelBackend',
    # cms
    #'auth.auth_backends.BlogUserModelBackend',
#)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '...'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '8XSGCRu5wD5vCWnD3FDhcEod'
SOCIAL_AUTH_FACEBOOK_KEY = '...'
SOCIAL_AUTH_FACEBOOK_SECRET = '...'

LOGIN_URL = '/auth/connexion/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)