# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 18:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itemsapp', '0001_initial'),
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_items', to='usersapp.Profile'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='items', to='itemsapp.Tag'),
        ),
    ]