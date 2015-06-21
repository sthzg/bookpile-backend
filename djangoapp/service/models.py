# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import six
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_pgjson.fields import JsonBField


class TimestampedMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(
        _('created'),
        auto_now_add=True
    )

    modified = models.DateTimeField(
        _('last modified'),
        auto_now=True
    )


class Author(TimestampedMixin):
    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')

    first_name = models.CharField(
        _('first name'),
        max_length=40,
        blank=True,
        null=True,
        default=None
    )

    last_name = models.CharField(
        _('first name'),
        max_length=40,
        blank=True,
        null=True,
        default=None
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Publisher(TimestampedMixin):
    class Meta:
        verbose_name = _('publisher')
        verbose_name_plural = _('publishers')

    name = models.CharField(
        _('name'),
        max_length=60,
        blank=False,
        null=False
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return '{}'.format(self.name)


class Book(TimestampedMixin):
    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')

    title = models.CharField(
        _('title'),
        max_length=200,
        blank=False,
        null=False
    )

    cover = models.ImageField(
        _('cover'),
        upload_to='covers',
        blank=True,
        null=True,
        default=None
    )

    subtitle = models.CharField(
        _('subtitle'),
        max_length=200,
        blank=False,
        null=False
    )

    authors = models.ManyToManyField(
        'Author',
        verbose_name=_('authors'),
        related_name='rel_author_book',
        blank=False,
        null=False,
    )

    publisher = models.ForeignKey(
        'Publisher',
        verbose_name=_('publisher'),
        related_name='rel_publisher_book',
        blank=True,
        null=True
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return '{}'.format(self.title)


class Chapter(TimestampedMixin):
    class Meta:
        verbose_name = _('chapter')
        verbose_name_plural = _('chapters')

    title = models.CharField(
        _('title'),
        max_length=200,
        blank=False,
        null=False
    )

    book = models.ForeignKey(
        'Book',
        related_name='rel_book_chapter',
        verbose_name=_('book')
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return '{}'.format(self.title)


class Document(TimestampedMixin):
    class Meta:
        verbose_name = _('document')
        verbose_name_plural = _('documents')

    DOCUMENT_TYPES = (
        ('review', _('review')),
        ('pro', _('pro')),
        ('con', _('con')),
        ('note', _('note')),
        ('summary', _('summary')),
    )

    #: The owner of the document.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='rel_user_snippets',
        blank=True,
        null=False,
        default=None
    )

    #: Every document may relate to different targets, e.g. to books, 
    #: chapters, authors, or even other documents.
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    #: The document type specifies which fields the document will provide 
    #: for users to enter.
    document_type = models.CharField(
        _('type'),
        max_length=25,
        choices=DOCUMENT_TYPES,
        blank=False,
        null=False,
        default=None
    )

    #: The actual content of the document, stored in a JSONB field.
    data = JsonBField(
        _('document data'),
        blank=True,
        null=True,
        default=None
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return 'document {}'.format(self.pk)


class MyBook(TimestampedMixin):
    """ An instance belonging to each user to store individual data on a book. 

    Whenever a user contributes data to a book an instance of `MyBook` 
    will be created. It relates the `user` to that `book` and makes it the
    central node all user-related book data (reviews, chapter summaries, 
    but also additional images and private notes) is connected to.
    """
    class Meta:
        verbose_name = _('my book')
        verbose_name_plural = _('my books')

    user = settings.AUTH_USER_MODEL

    book = models.ForeignKey(
        'Book',
        verbose_name=_('book'),
        related_name='rel_book_mybook',
        blank=False,
        null=False,
        default=None
    )

    @six.python_2_unicode_compatible
    def __str__(self):
        return '{} documents for {}'.format(self.user.get_username(), self.book)

