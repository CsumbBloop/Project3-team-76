# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-14 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album23',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=500)),
                ('album_logo', models.CharField(max_length=1000)),
                ('album_logo2', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='Album22',
        ),
    ]
