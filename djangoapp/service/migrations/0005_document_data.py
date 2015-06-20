# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20150620_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='data',
            field=django_pgjson.fields.JsonBField(default=None, blank=True, verbose_name='document data', null=True),
        ),
    ]
