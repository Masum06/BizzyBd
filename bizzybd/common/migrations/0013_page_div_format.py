# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_page_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='div_format',
            field=models.TextField(blank=True, null=True),
        ),
    ]
