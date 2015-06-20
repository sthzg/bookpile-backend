# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from .views import *


urlpatterns = [
    url(                                                                     # /
        '^$', 
        IndexView.as_view(), 
        name='index'
    ),

    # Endpoint to test access by logged in user 
    url(                                                              # /secure/
        r'^secure/$',
        secret_page,
        name='secret_page'
    ),

]
