from techhire.settings import *

# Override settings for testing
DEBUG = False
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': ':memory:',
}

DEFAULT_CHARSET = 'utf-8'