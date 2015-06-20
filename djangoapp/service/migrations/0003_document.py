# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('service', '0002_auto_20150620_2242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('object_id', models.PositiveIntegerField()),
                ('snippet_type', models.CharField(max_length=25, verbose_name='type', default=None, choices=[('review', 'review'), ('pro', 'pro'), ('con', 'con'), ('note', 'note'), ('summary', 'summary')])),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='rel_user_snippets', verbose_name='user', default=None)),
            ],
            options={
                'verbose_name': 'document',
                'verbose_name_plural': 'documents',
            },
        ),
    ]
