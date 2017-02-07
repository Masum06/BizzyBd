# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('div1', models.CharField(blank=True, max_length=300, null=True)),
                ('div2', models.CharField(blank=True, max_length=300, null=True)),
                ('div3', models.CharField(blank=True, max_length=300, null=True)),
                ('div4', models.CharField(blank=True, max_length=300, null=True)),
                ('div5', models.CharField(blank=True, max_length=300, null=True)),
                ('div6', models.CharField(blank=True, max_length=300, null=True)),
                ('div7', models.CharField(blank=True, max_length=300, null=True)),
                ('div8', models.CharField(blank=True, max_length=300, null=True)),
                ('div9', models.CharField(blank=True, max_length=300, null=True)),
                ('div10', models.CharField(blank=True, max_length=300, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
