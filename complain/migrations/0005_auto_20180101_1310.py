# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-01 12:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0004_auto_20180101_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complain',
            name='code',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='govt_agency',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='message',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='status',
        ),
        migrations.RemoveField(
            model_name='complain',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='govt_agency',
            name='address',
        ),
        migrations.RemoveField(
            model_name='govt_agency',
            name='department',
        ),
        migrations.RemoveField(
            model_name='govt_agency',
            name='name',
        ),
        migrations.RemoveField(
            model_name='govt_agency',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='govt_agency',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='govt_agency_access',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='govt_agency_access',
            name='user',
        ),
    ]
