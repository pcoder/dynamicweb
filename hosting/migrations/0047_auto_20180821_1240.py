# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-08-21 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0046_usercarddetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostingorder',
            name='cc_brand',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='usercarddetail',
            name='brand',
            field=models.CharField(max_length=128),
        ),
    ]
