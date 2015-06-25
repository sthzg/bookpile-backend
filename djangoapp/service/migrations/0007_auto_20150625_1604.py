# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_mybook'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='search_field',
            field=models.CharField(editable=False, verbose_name='search index', db_index=True, null=True, blank=True, max_length=80, default=None),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(verbose_name='last name', null=True, blank=True, max_length=40, default=None),
        ),
    ]
