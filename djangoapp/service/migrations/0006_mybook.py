# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_document_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='last modified', auto_now=True)),
                ('book', models.ForeignKey(related_name='rel_book_mybook', to='service.Book', verbose_name='book', default=None)),
            ],
            options={
                'verbose_name_plural': 'my books',
                'verbose_name': 'my book',
            },
        ),
    ]
