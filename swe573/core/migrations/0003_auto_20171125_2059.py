# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 20:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_post_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['start_date']},
        ),
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(blank=True, default=datetime.date(2017, 11, 25), verbose_name='EndDate'),
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(blank=True, default=datetime.date(2017, 11, 25), verbose_name='StartDate'),
        ),
    ]
