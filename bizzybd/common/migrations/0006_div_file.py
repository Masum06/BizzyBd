# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20170228_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='div',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='filepicker/'),
        ),
    ]
