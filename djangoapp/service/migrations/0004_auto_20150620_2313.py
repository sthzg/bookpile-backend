# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_document'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='snippet_type',
            new_name='document_type',
        ),
    ]
