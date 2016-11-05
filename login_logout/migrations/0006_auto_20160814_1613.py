# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 13:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login_logout', '0005_auto_20160808_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='new_password',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='activationuser',
            name='key_expires',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 13, 13, 58, 869948, tzinfo=utc)),
        ),
    ]
