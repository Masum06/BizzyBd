# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_div_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='div',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='slim/'),
        ),
    ]
