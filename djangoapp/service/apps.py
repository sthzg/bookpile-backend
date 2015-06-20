# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ServiceConfig(AppConfig):
    name = 'service'
    verbose_name = _("Bookpile")
