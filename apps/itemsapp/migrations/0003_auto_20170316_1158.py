# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsapp', '0002_auto_20170315_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
