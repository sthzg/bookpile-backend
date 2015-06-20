# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.utils.translation import ugettext_lazy as _
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import viewsets
from .apiserializers import *
from .models import Author, Book, Chapter, Document, Publisher


@api_view(('GET',))
def api_root(request, format=None):
    """ Provides a root view for the browsable api. 
    """
    return Response({
        'index': reverse('service-api:index', request=request, format=format),
        'authors': reverse('service-api:author-list', request=request, format=format),
        'books': reverse('service-api:book-list', request=request, format=format),
        'chapters': reverse('service-api:chapter-list', request=request, format=format),
        'publishers': reverse('service-api:publisher-list', request=request, format=format),
        'documents': reverse('service-api:document-list', request=request, format=format),
    })


class IndexApiView(APIView):
    """ Provides a Hello World endpoint to be overridden or trashed. 
    """
    def get(self, request):
        content = {'greeting': "Hello World"}
        serializer = IndexSerializer(content)
        return Response(serializer.data)


class AuthorApiView(viewsets.ModelViewSet):
    """ Provides a CRUD endpoint for author instances.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookApiView(viewsets.ModelViewSet):
    """ Provides a CRUD endpoint for book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChapterApiView(viewsets.ModelViewSet):
    """ Provides a CRUD endpoint for chapter instances.
    """
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class PublisherApiView(viewsets.ModelViewSet):
    """ Provides a CRUD endpoint for publisher instances.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class DocumentApiView(viewsets.ModelViewSet):
    """ Provides a CRUD endpoint for document instances.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

