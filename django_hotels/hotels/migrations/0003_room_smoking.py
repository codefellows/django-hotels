# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0002_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='smoking',
            field=models.BooleanField(default=False),
        ),
    ]
