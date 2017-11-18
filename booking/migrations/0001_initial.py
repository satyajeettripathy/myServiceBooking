# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceType', models.CharField(max_length=200)),
                ('serviceInstruction', models.CharField(max_length=500)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('created_by', models.CharField(db_index=True, max_length=200)),
                ('updated_at', models.DateField(auto_now=True)),
                ('updated_by', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='booking.Customer'),
        ),
    ]