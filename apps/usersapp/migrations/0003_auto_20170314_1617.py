# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 21:17
from __future__ import unicode_literals

import apps.usersapp.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0002_auto_20170313_2344'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('objects', apps.usersapp.models.ProfileManager()),
            ],
        ),
    ]
