# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opiekun', '0002_auto_20160604_1002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupa',
            options={'verbose_name_plural': 'grupy'},
        ),
        migrations.AlterModelOptions(
            name='opiekun',
            options={'verbose_name_plural': 'opiekunowie'},
        ),
        migrations.AddField(
            model_name='grupa',
            name='rocznik',
            field=models.IntegerField(default=2013),
            preserve_default=False,
        ),
    ]
