# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-05-06 23:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosting', '0035_virtualmachineplan_opennebula_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtualmachineplan',
            name='opennebula_id',
            field=models.IntegerField(null=True),
        ),
    ]
