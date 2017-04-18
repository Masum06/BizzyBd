"""
WSGI config for eonushilon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os, sys, site


# site.addsitedir('/home/alamin/.virtualenvs/bizzybd/lib/python3.5/site-packages/')

# Add the app's directory to the PYTHONPATH
sys.path.append('/mnt/340048A400486EC4/Dropbox/Programming/Django/bizzybd/bizzybd/bizzybd')
sys.path.append('/app')
# sys.path.append('/mnt/340048A400486EC4/Dropbox/Programming/Django/bizzybd/bizzybd')
# Activate your virtual env
# activate_env=os.path.expanduser("/home/.virtualenvs/bizzybd/bin/activate_this.py")






from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "settings.production"


application = get_wsgi_application()
