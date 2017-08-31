# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 02:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table', models.CharField(max_length=20)),
                ('column', models.CharField(max_length=20)),
                ('value', models.IntegerField(max_length=2)),
                ('label', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Spider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('intro', models.TextField()),
                ('project', models.CharField(max_length=100)),
                ('target_site', models.CharField(max_length=200)),
                ('type', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SpiderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loc', models.CharField(max_length=200)),
                ('status', models.IntegerField(max_length=2)),
                ('log', models.TextField()),
                ('edit_time', models.DateTimeField()),
                ('spider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.Spider')),
            ],
        ),
    ]
