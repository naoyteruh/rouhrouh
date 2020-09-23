import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/superman/.virtualenvs/ekiLibr/local/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/home/superman/.virtualenvs/ekiLibr/projects/boilerplate')

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/home/superman/.virtualenvs/ekiLibr/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

