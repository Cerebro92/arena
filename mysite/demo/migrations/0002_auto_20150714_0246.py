# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('a_id', models.IntegerField()),
                ('author_name', models.CharField(max_length=50)),
                ('article_content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
