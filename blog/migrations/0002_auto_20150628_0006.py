# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.CharField(verbose_name='Enter content', max_length=1000000),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_title',
            field=models.CharField(verbose_name='Enter title', max_length=100),
        ),
    ]
