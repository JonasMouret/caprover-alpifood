"""caprover specific django settings"""

import os

from django.core.exceptions import ImproperlyConfigured

from .settings import BASE_DIR

# key and debugging settings should not changed without care
SECRET_KEY = os.environ.get("CR_SECRET_KEY") or ImproperlyConfigured("CR_SECRET_KEY not set")

FACEBOOK_APP_ID = os.environ.get("CR_FACEBOOK_APP_ID") or ImproperlyConfigured("CR_FACEBOOK_APP_ID not set")
FACEBOOK_APP_SECRET = os.environ.get("CR_FACEBOOK_APP_SECRET") or ImproperlyConfigured("CR_FACEBOOK_APP_SECRET not set")
STRIPE_API_KEY = os.environ.get("CR_STRIPE_API_KEY") or ImproperlyConfigured("CR_STRIPE_API_KEY not set")

if os.environ.get('CAPROVER'):
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False
APPEND_SLASH=False 

# allowed hosts get parsed from a comma-separated list
hosts = os.environ.get("CR_HOSTS") or ImproperlyConfigured("CR_HOSTS not set")
try:
    ALLOWED_HOSTS = hosts.split(",")
except:
    raise ImproperlyConfigured("CR_HOSTS could not be parsed")

# Database
if os.environ.get("CR_USESQLITE"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
else:
    name = os.environ.get("CR_DB_NAME") or ImproperlyConfigured("CR_DB_NAME not set")
    user = os.environ.get("CR_DB_USER") or ImproperlyConfigured("CR_DB_USER not set")
    password = os.environ.get("CR_DB_PASSWORD") or ImproperlyConfigured("CR_DB_PASSWORD not set")
    host = os.environ.get("CR_DB_HOST") or ImproperlyConfigured("CR_DB_HOST not set")
    port = os.environ.get("CR_DB_PORT") or ImproperlyConfigured("CR_DB_PORT not set")

    DATABASES = {
        "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": name,
        "USER": user,
        "PASSWORD": password,
        "HOST": host,
        "PORT": port,
        }
    }


# Facebook configuration
SOCIAL_AUTH_FACEBOOK_KEY = FACEBOOK_APP_ID
SOCIAL_AUTH_FACEBOOK_SECRET = FACEBOOK_APP_SECRET

# Static Files
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

# Media Files
MEDIA_ROOT= os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
