# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from settings.base import *
from settings.utils import get_env_variable


SECRET_KEY = get_env_variable('DJ_PROJECT_DEV_SECRET_KEY')
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += [
]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../public/static')

MEDIA_ROOT = os.path.join(BASE_DIR, '../public/media')
MEDIA_URL = '/media/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DJ_PROJECT_DEV_DB_NAME'),
        'USER': get_env_variable('DJ_PROJECT_DEV_DB_USER'),
        'PASS': get_env_variable('DJ_PROJECT_DEV_DB_PASS'),
        'HOST': '',
        'PORT': ''
    }
}

SERVER_EMAIL = get_env_variable('DJ_PROJECT_DEV_SERVER_EMAIL')
EMAIL_BACKEND = get_env_variable('DJ_PROJECT_DEV_EMAIL_BACKEND')
EMAIL_HOST = get_env_variable('DJ_PROJECT_DEV_EMAIL_HOST')
EMAIL_PORT = get_env_variable('DJ_PROJECT_DEV_EMAIL_PORT')
EMAIL_HOST_USER = get_env_variable('DJ_PROJECT_DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('DJ_PROJECT_DEV_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = get_env_variable('DJ_PROJECT_DEV_EMAIL_USE_TLS')

# Django Cors Headers
CORS_ORIGIN_WHITELIST = (
    '{}://{}:{}'.format(
        get_env_variable('DJ_PROJECT_DEV_FRONTEND_PROTO'),
        get_env_variable('DJ_PROJECT_DEV_FRONTEND_HOST'),
        get_env_variable('DJ_PROJECT_DEV_FRONTEND_PORT'),
    )
)

# Celery
CELERY_ENABLE_UTC = True
BROKER_URL = 'amqp://{}:{}@{}:{}//'.format(
    get_env_variable('DJ_PROJECT_DEV_CELERY_USER'),
    get_env_variable('DJ_PROJECT_DEV_CELERY_PASS'),
    get_env_variable('DJ_PROJECT_DEV_CELERY_HOST'),
    get_env_variable('DJ_PROJECT_DEV_CELERY_PORT')
)
CELERY_RESULT_BACKEND = 'amqp://'
CELERY_TIMEZONE = 'Europe/Vienna'
CELERY_TASK_RESULT_EXPIRES = "600"
CELERYD_TASK_LOG_FORMAT = 'ERROR'
CELERYD_CONCURRENCY = 1
CELERYD_NODES = "w1"
