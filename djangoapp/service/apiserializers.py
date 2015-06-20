# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from rest_framework import serializers
from .models import Author, Book, Chapter, Document, Publisher


__all__ = [
    'IndexSerializer',
    'AuthorSerializer',
    'BookSerializer',
    'ChapterSerializer',
    'DocumentSerializer',
    'PublisherSerializer',
]


class IndexSerializer(serializers.Serializer):
    greeting = serializers.CharField(max_length=100)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
