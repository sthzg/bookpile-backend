# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(verbose_name='first name', default=None, blank=True, null=True, max_length=40)),
                ('last_name', models.CharField(verbose_name='first name', default=None, blank=True, null=True, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('cover', models.ImageField(verbose_name='cover', null=True, upload_to='covers', blank=True, default=None)),
                ('subtitle', models.CharField(verbose_name='subtitle', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('authors', models.ManyToManyField(verbose_name='authors', to='service.Author', related_name='rel_author_book')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('book', models.OneToOneField(verbose_name='book', to='service.Book', related_name='rel_book_chapter')),
            ],
            options={
                'verbose_name': 'chapter',
                'verbose_name_plural': 'chapters',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
            ],
            options={
                'verbose_name': 'publisher',
                'verbose_name_plural': 'publishers',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(verbose_name='publisher', to='service.Publisher', related_name='rel_publisher_book', null=True, blank=True),
        ),
    ]
