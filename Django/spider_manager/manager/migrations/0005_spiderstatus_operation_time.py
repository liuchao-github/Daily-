# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_remove_dict_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiderstatus',
            name='operation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
