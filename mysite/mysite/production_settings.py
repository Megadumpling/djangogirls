# import all default settings
from .settings import *

import dj_database_url

#DATABASES = {
#	'default': dj_database_url.config()
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydatabase',
        'USER': 'sarahr6',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}


# Static asset configuration
STATIC_ROOT = 'staticfiles'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode
DEBUG = False
TEMPLATE_DEBUG = False