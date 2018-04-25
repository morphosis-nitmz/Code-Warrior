# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-25 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180424_0227'),
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
