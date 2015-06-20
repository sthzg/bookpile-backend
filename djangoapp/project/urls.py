# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

"""
.. note::

    Notice that you probably won't use all of the packages that are configured 
    here. E.g. if you use django_oauth_toolkit then rest_framework_jwt will 
    not be necessary. Remove unnecessary urls for your service and also check 
    settings.py to remove all apps, settings and middleware for packages that 
    your setup doesn't use.

"""

urlpatterns = [

    # Provided by rest_framework
    url(                                                            # /api-auth/
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    # Provided by rest_framework_jwt
    url(                                                      # /api-token-auth/
        r'^api-token-auth/',
        'rest_framework_jwt.views.obtain_jwt_token'
    ),

    # Provided by rest_framework_swagger
    url(                                                           # /apidocs/*/
        r'^apidocs/',
        include('rest_framework_swagger.urls')
    ),

    # This are urls provided by our actual service
    url(                                                            # /api/v1/*/
        r'^api/v1/',
        include('service.apiurls', namespace='service-api')
    ),

    url(                                                                   # /*/
        r'^',
        include('service.urls', namespace='service')
    ),

    # Provided by django.contrib.admin
    url(                                                             # /admin/*/
        r'^admin/',
        include(admin.site.urls)
    ),
]

if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(                                                         # /media/*/
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),

        url(
            r'',
            include('django.contrib.staticfiles.urls')
        ),
    ) + urlpatterns
