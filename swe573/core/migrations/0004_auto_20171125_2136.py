# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 21:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171125_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='EndDate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='StartDate'),
        ),
    ]
