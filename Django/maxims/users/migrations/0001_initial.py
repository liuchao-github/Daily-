# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DpMember',
            fields=[
                ('memberId', models.IntegerField(primary_key=True, serialize=False)),
                ('pic', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('contribution', models.IntegerField()),
                ('contrReview', models.CharField(max_length=20)),
                ('contrShop', models.CharField(max_length=20)),
                ('contrPic', models.CharField(max_length=20)),
                ('contrInfo', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('levels', models.CharField(max_length=255)),
                ('regtime', models.CharField(max_length=255)),
                ('follows', models.IntegerField()),
                ('fans', models.IntegerField()),
                ('interactive', models.IntegerField()),
                ('review', models.IntegerField()),
                ('favourite', models.IntegerField()),
                ('checkin', models.IntegerField()),
                ('picture', models.IntegerField()),
                ('mylist', models.IntegerField()),
                ('post', models.IntegerField()),
                ('birthday', models.CharField(max_length=50)),
                ('loveState', models.CharField(max_length=50)),
                ('jobs', models.CharField(max_length=50)),
                ('birthplace', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MfwMember',
            fields=[
                ('memberId', models.IntegerField(primary_key=True, serialize=False)),
                ('pic', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=20)),
                ('vip', models.IntegerField()),
                ('duo', models.IntegerField()),
                ('zhiluren', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('follows', models.IntegerField()),
                ('fans', models.IntegerField()),
                ('profile', models.TextField()),
                ('review', models.CharField(max_length=225)),
                ('contribution', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='OrMember',
            fields=[
                ('memberId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('badge', models.CharField(max_length=20)),
                ('follows', models.IntegerField()),
                ('fans', models.IntegerField()),
                ('reviewNum', models.IntegerField()),
                ('regtime', models.CharField(max_length=50)),
                ('actionZone', models.CharField(max_length=100)),
                ('workPlace', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('favorite', models.CharField(max_length=255)),
                ('firWritten', models.IntegerField()),
                ('pic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaMember',
            fields=[
                ('memberId', models.IntegerField(primary_key=True, serialize=False)),
                ('pic', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=100)),
                ('regtime', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
                ('photos', models.CharField(max_length=10)),
                ('potints', models.CharField(max_length=10)),
                ('levels', models.CharField(max_length=10)),
                ('badges', models.CharField(max_length=10)),
            ],
        ),
    ]
