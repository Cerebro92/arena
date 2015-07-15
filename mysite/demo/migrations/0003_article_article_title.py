# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150714_0246'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
