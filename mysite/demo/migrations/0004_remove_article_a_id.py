# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_article_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='a_id',
        ),
    ]
