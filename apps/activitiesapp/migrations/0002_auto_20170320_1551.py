# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-20 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activitiesapp', '0001_initial'),
        ('itemsapp', '0001_initial'),
        ('usersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='usersapp.Address'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='usersapp.Profile'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bid', to='itemsapp.Item'),
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to='usersapp.Profile'),
        ),
        migrations.AddField(
            model_name='review',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewed', to='itemsapp.Item'),
        ),
    ]
