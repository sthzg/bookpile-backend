"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOG_DIR = os.path.join(BASE_DIR, '../logs')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_nose',
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger',
    'service',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'oauth2_provider.backends.OAuth2Backend',
    'django.contrib.auth.backends.ModelBackend',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '_staticdir'),
    os.path.join(BASE_DIR, '_bowerdir'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '_templatedir'),
)

LOCALE_PATHS = (
    os.path.abspath(os.path.join(BASE_DIR, 'locale')),
)

ROOT_URLCONF = 'project.urls'
WSGI_APPLICATION = 'project.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Vienna'
USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_X_FORWARDED_HOST = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'misc': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'misc.log'),
            'mode': 'a',
            'formatter': 'verbose'
        },
        'file_requests': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'requests.log'),
            'mode': 'a',
            'formatter': 'verbose'
        },
        'file_db': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'db.log'),
            'mode': 'a',
            'formatter': 'verbose'
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'security.log'),
            'mode': 'a',
            'formatter': 'verbose'
        },
        'service': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'service.log'),
            'mode': 'a',
            'formatter': 'verbose'
        },
        'celery_task_logger': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'celery_tasks.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 2,
            'formatter': 'verbose'
        },
        'celery_logger': {
            'level': 'INFO',
            'filters': None,
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'celery.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 2,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'misc': {
            'handlers': ['misc'],
            'level': 'INFO',
            'propagate': False
        },
        'django.request': {
            'handlers': ['file_requests'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['file_db'],
            'level': 'INFO',
            'propagate': False
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': False,
        },
        'service': {
            'handlers': ['service'],
            'level': 'INFO',
            'propagate': False,
        },
        'celery': {
            'handlers': ['celery_logger'],
            'level': 'INFO',
            'propagate': True},
        'celery.task': {
            'handlers': ['celery_task_logger'],
            'level': 'INFO',
            'propagate': True
        },
    },
}

# Django Cors Headers
CORS_ORIGIN_WHITELIST = (
    'django-oauth-toolkit.herokuapp.com',
)

CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)

CORS_ALLOW_HEADERS = (
    'x-requested-with',
    'content-type',
    'accept',
    'origin',
    'authorization',
    'x-csrftoken'
)

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication', 
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

# Django Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
