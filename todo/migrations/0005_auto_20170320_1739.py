# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-20 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170320_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(default='No_Label'),
        ),
    ]
