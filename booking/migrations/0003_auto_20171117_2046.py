# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 19:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20171117_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='serviceType',
            new_name='service',
        ),
    ]