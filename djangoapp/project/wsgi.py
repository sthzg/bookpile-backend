"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from settings.utils import get_env_variable

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.{}".format(
    get_env_variable('DJ_PROJECT_CURRENT_ENV')))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
