from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ose60*a_6-a9b2=!8oubq)f3(#_w8ofgkloytxwcnekun%zd9='

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
    'django_extensions',             #python3 manage.py shell_plus --ipython 
    'wagtail.contrib.styleguide',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# Uncomment this line to enable template caching
# Dont forget to change the LOCATION path, if changed just delete the cached files
CACHES = {
    "default": {
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": "/Users/shahzeb/cms/cache"
    }
}


try:    
    from .local import *
except ImportError:
    pass




