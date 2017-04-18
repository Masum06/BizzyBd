# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_website_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='div',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Theme'),
        ),
        migrations.AddField(
            model_name='page',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='common.Theme'),
        ),
    ]
