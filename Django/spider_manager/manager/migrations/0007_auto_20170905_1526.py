# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20170904_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spiderstatus',
            name='operation_time',
            field=models.TimeField(),
        ),
    ]
