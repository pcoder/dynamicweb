# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-07-01 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import utils.mixins


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0024_dclcalculatorpluginmodel_vm_templates_to_show'),
        ('hosting', '0044_hostingorder_vm_pricing'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cores', models.IntegerField(default=0)),
                ('memory', models.IntegerField(default=0)),
                ('hdd_size', models.IntegerField(default=0)),
                ('ssd_size', models.IntegerField(default=0)),
                ('vm_template', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='datacenterlight.VMTemplate')),
            ],
            bases=(utils.mixins.AssignPermissionsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='hostingorder',
            name='order_detail',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hosting.OrderDetail'),
        ),
    ]
