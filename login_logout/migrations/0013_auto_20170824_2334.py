# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-24 23:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_logout', '0012_auto_20161105_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activationuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 23, 34, 20, 915347)),
        ),
    ]
