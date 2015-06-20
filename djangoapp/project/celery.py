# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from settings.utils import get_env_variable


cur_env = get_env_variable('DJ_PROJECT_CURRENT_ENV')

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 'settings.{}'.format(cur_env)
)

app = Celery('project')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
