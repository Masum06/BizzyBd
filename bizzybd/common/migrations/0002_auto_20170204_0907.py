# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='website',
            old_name='user',
            new_name='owner',
        ),
    ]
