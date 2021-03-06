# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-01 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170301_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='likes_most',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='who do you like most?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='likes_not',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='who do you like not at all?'),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='want_to_do',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='what do you want to do?'),
        ),
    ]
