# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-20 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='portfolio_pic',
            new_name='profile_pic',
        ),
    ]
