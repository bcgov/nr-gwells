"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import datetime
import logging.config
from pathlib import Path

import requests

from gwells import database
from gwells.settings.base import get_env_variable

BASE_DIR = str(Path(__file__).parents[2])

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# The SECRET_KEY is provided via an environment variable in OpenShift
SECRET_KEY = get_env_variable(
    'DJANGO_SECRET_KEY',
    # safe value used for development when DJANGO_SECRET_KEY might not be set
    '9e4@&tw46$l31)zrqe3wi+-slqm(ruvz&se0^%9#6(_w3ui!c0'
)

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = get_env_variable(
    'SESSION_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_SECURE = get_env_variable('CSRF_COOKIE_SECURE', 'False') == 'True'
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = get_env_variable('DJANGO_DEBUG', 'False') == 'True'

# Additional Documents Feature Flag
ENABLE_ADDITIONAL_DOCUMENTS = get_env_variable(
    'ENABLE_ADDITIONAL_DOCUMENTS', 'False', strict=True) == 'True'

# Controls app context
APP_CONTEXT_ROOT = get_env_variable('APP_CONTEXT_ROOT', 'gwells')

FIXTURES_DIR = '/'.join([BASE_DIR, APP_CONTEXT_ROOT, 'fixtures'])

# Fixtures dirs
FIXTURES_DIRS = [FIXTURES_DIR]

# GeoDjango External Library Paths
# When running containerised, GDAL_LIBRARY_PATH and GEOS_LIBRARY_PATH -**MUST**- be specified.
# For running locally, if you've configured you local system correctly, CUSTOM_GDAL_GEOS may be set to False.
if get_env_variable('CUSTOM_GDAL_GEOS', 'True', strict=False, warn=False) == 'True':
    GDAL_LIBRARY_PATH = get_env_variable(
        'GDAL_LIBRARY_PATH', '/usr/local/lib/libgdal.so')
    GEOS_LIBRARY_PATH = get_env_variable(
        'GEOS_LIBRARY_PATH', '/usr/local/lib/libgeos_c.so')

# django-settings-export lets us make these variables available in the templates.
# This eleminate the need for setting the context for each and every view.
SETTINGS_EXPORT = [
    # To temporarily disable additional documents feature
    'ENABLE_ADDITIONAL_DOCUMENTS',
    # This allows for moving the app around without code changes
    'APP_CONTEXT_ROOT',
    'FIXTURES_DIRS'
]

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = [
    'GET',
    'OPTIONS'
]

if DEBUG:
    CORS_ALLOW_METHODS = [
        'DELETE',
        'GET',
        'OPTIONS',
        'PATCH',
        'POST',
        'PUT',
    ]

# Application definition
INSTALLED_APPS = (
    # 'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'django.contrib.staticfiles',
    'debug_toolbar',
    'django.contrib.postgres',
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    'gwells',
    'crispy_forms',
    'formtools',
    'registries',
    'wells',
    'submissions',
    'aquifers',
    'django_filters',
    'django_extensions',
    'drf_multiple_model',
    'reversion',
    'django.contrib.gis',
)

MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'gwells.middleware.GWellsRequestParsingMiddleware'
)

ROOT_URLCONF = 'gwells.urls'
INTERNAL_IPS = '127.0.0.1'

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
}

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
                'django_settings_export.settings_export',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'
# 2018/04/19: According to the documentation, bootstrap4 is still in alpha:
# http://django-crispy-forms.readthedocs.io/en/latest/install.html?highlight=bootstrap4
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': database.config()
}

# Re-use database connections, leave connection alive for 5 mimutes
CONN_MAX_AGE = 120

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# if APP_CONTEXT_ROOT:
#     STATIC_URL = '/' + APP_CONTEXT_ROOT + '/'
# else:
#     STATIC_URL = '/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_DIR = (
#     os.path.join(BASE_DIR, 'staticfiles')
# )

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'debug': {
            'format':
                '%(levelname)s %(asctime)s %(filename)s[%(lineno)d]:%(module)s::%(funcName)s %(message)s'
        }
    },
    'handlers': {
        'console_handler': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'debug',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        '': {
            'handlers': ['console_handler'],
            'propagate': True,
            'level': 'DEBUG'
        },
    }
}


try:
    url = get_env_variable('SSO_AUTH_HOST') + '/realms/' + get_env_variable("SSO_REALM")
    res = requests.get(url)
    public_key = res.json()['public_key']
    if len(public_key) <= 0:
        public_key = get_env_variable('SSO_PUBKEY', "")
except:
    public_key = get_env_variable('SSO_PUBKEY', "")


SIMPLE_JWT = {
    'ALGORITHM': 'RS256',
    'VERIFYING_KEY': ("-----BEGIN PUBLIC KEY-----\n" +
                      public_key +
                      "\n-----END PUBLIC KEY-----"),
    'AUDIENCE': None,
    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'username',
    'USER_ID_CLAIM': 'preferred_username',
}


DRF_RENDERERS = ['rest_framework.renderers.JSONRenderer', ]
# Turn on browsable API if "DEBUG" set
if DEBUG:
    DRF_RENDERERS.append('rest_framework.renderers.BrowsableAPIRenderer')

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': DRF_RENDERERS,
    'DEFAULT_PERMISSION_CLASSES': (
        'gwells.permissions.ReadOnlyPermission',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'gwells.authentication.JwtOidcAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 30,
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100000/hour',
        'user': '200000/hour'
    },
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v1',
}

LOGIN_URL = '/gwells/accounts/login/'
LOGIN_REDIRECT_URL = '/gwells/search'

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'JWT',
            'in': 'header'
        }
    }
}

ADD_REVERSION_ADMIN = True


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'apps.smtp.gov.bc.ca'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'no-reply@gov.bc.ca'
EMAIL_HOST_PASSWORD = ''


# It can be very useful to disable migrations when testing. This piece of code allows one to disable
# migrations by specifying an environemnt variable DISABLE_MIGRATIONS. Used in conjunction with
# --keepdb, a developer can run mosts unit tests, and run them fast.
#
# e.g.: DISABLE_MIGRATIONS=DISABLE_MIGRATIONS python manage.py test\
#  submissions.tests.TestWellSubmissionListSerializer --keepdb
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None


if get_env_variable('DISABLE_MIGRATIONS', None, strict=False, warn=False) == 'DISABLE_MIGRATIONS':
    MIGRATION_MODULES = DisableMigrations()

# WHITENOISE_INDEX_FILE = True
APPEND_SLASH = True
