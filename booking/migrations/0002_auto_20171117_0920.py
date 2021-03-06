# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('time', models.IntegerField(default=2)),
                ('cost_per_hr', models.IntegerField(default=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='appointment',
            name='serviceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Service'),
        ),
    ]
