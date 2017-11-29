# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_hotel_is_open'),
        ('employees', '0002_employee_currently_employed'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='hotel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='hotels.Hotel'),
            preserve_default=False,
        ),
    ]