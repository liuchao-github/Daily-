# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_spiderstatus_operation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spider',
            name='target_site',
            field=models.CharField(max_length=500),
        ),
    ]
