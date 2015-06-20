# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _
from rest_framework import routers
from service import apiviews


urlpatterns = [
    url(r'^$', apiviews.api_root),
    url(r'^index/$', apiviews.IndexApiView.as_view(), name='index'),
]

router = routers.SimpleRouter()
router.register(r'authors', apiviews.AuthorApiView)
router.register(r'books', apiviews.BookApiView)
router.register(r'chapters', apiviews.ChapterApiView)
router.register(r'documents', apiviews.DocumentApiView)
router.register(r'publishers', apiviews.PublisherApiView)
urlpatterns += router.urls

