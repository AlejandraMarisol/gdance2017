# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-10-22 23:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='tipo_role',
        ),
    ]
