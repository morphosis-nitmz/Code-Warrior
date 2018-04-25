# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-25 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20180425_1356'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-score', 'total_time']},
        ),
        migrations.AddField(
            model_name='user',
            name='total_time',
            field=models.IntegerField(default=0),
        ),
    ]
