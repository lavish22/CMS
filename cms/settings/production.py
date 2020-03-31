from .base import *

DEBUG = False
ALLOWED_HOSTS= ['*']


SECRET_KEY = 'ose60*a_6-a9b2=!8oubq)f3(#_w8ofgkloytxwcnekun%zd9='
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


'''
# Uncomment this line to enable template caching
# Dont forget to change the LOCATION path, if changed just delete the cached files
CACHES = {
    "default": {
         "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
         "LOCATION": "/code/cache"
    }
}
'''

try:
    from .local import *
except ImportError:
    pass


#python3 manage.py check --deploy