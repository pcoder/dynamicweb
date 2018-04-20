# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-12 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('datacenterlight', '0018_auto_20180403_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSFaviconExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extended_object', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='cms.Page')),
                ('favicon', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='cms_favicon_image', to='filer.File')),
                ('public_extension', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='draft_extension', to='datacenterlight.CMSFaviconExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]