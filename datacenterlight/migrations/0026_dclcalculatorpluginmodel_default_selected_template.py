# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-09-27 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0025_dclnavbarpluginmodel_show_login_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='dclcalculatorpluginmodel',
            name='default_selected_template',
            field=models.CharField(default='Devuan Ascii', help_text='Write the name of the template that you need selected as default when the calculator loads', max_length=128, null=True),
        ),
    ]
