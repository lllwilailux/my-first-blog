# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='creatd_date',
            new_name='created_date',
        ),
    ]
