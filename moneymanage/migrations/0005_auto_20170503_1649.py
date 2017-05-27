# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 16:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanage', '0004_bank'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='fixed',
            new_name='fixed_max',
        ),
        migrations.AddField(
            model_name='bank',
            name='fixed_min',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='bank',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='gold_price',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='sav_list',
            name='sav_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='stock',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]