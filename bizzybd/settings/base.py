"""
Django settings for bizzybd project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2w--azb79o55y=#u7c+al2+dnzqd1w)kp6xrfx0=1hd$*+mbfw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'django.contrib.sites',
    'captcha',  # apt-get -y install libz-dev libjpeg-dev libfreetype6-dev python-dev
    # 'django_hosts',
    'subdomains',
    'common',
    'home',
    'cards',
)

MIDDLEWARE_CLASSES = (
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    # 'django_hosts.middleware.HostsRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'django_hosts.middleware.HostsResponseMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bizzybd.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "server_static")

# media files. Uploaded by user
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#  python social auth settings
# https://console.developers.google.com/
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "177712972981-vdr72075acg8rm971huo4ghf1lmfr1j5.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "B13ABzt25MmYHFUUS5Y3b4VA"

# https://developers.facebook.com/apps/?action=create
SOCIAL_AUTH_FACEBOOK_KEY = '1739192396395315'
SOCIAL_AUTH_FACEBOOK_SECRET = "cbaad4d849411bd27f2b279e883af6fd"
# required to get email from facebook.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'fields': 'id,name,email', }
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# SESSION_COOKIE_DOMAIN = '.bizzybdlocal.com'
# SESSION_COOKIE_DOMAIN = 'bizzybdid'


SITE_ID = 1

ROOT_URLCONF = 'subdomain.urls'

# # A dictionary of urlconf module paths, keyed by their subdomain.
SUBDOMAIN_URLCONFS = {

    None: 'bizzybd.urls',  # no subdomain, e.g. ``example.com``
    'www': 'myproject.urls.frontend',
    'api': 'myproject.urls.api',
    'cards': 'cards.urls',
    '.': 'subdomain.urls',

}
