# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanage', '0006_sav_list_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='name',
            new_name='stock_name',
        ),
    ]