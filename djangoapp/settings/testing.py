# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from settings.dev import *


SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False
CELERY_ALWAYS_EAGER = True
CELERY_ENABLED = False

MEDIA_ROOT = "/tmp"

EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
    "anon": None,
    "user": None,
    "import-mode": None,
    "import-dump-mode": None,
}
