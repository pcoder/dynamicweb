# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-03-28 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0044_vmdetail_hdd_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vmdetail',
            old_name='disk_size',
            new_name='ssd_size',
        ),
    ]
