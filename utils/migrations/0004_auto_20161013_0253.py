# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-13 02:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0003_userbillingaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbillingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_addresses', to=settings.AUTH_USER_MODEL),
        ),
    ]