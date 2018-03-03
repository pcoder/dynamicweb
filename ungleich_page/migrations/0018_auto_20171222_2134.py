# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-22 21:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('ungleich_page', '0017_auto_20171219_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_service', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_serviceitem', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungelichcontactussection',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungelichcontactussection', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungelichpicture',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungelichpicture', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungelichtextsection',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungelichtextsection', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichcustomeritem',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichcustomeritem', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheader',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichheader', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheaderitem',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichheaderitem', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheaderwithbackgroundimageslider',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichheaderwithbackgroundimageslider', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheaderwithbackgroundimageslideritem',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichheaderwithbackgroundimageslideritem', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheaderwithbackgroundvideoslideritem',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichheaderwithbackgroundvideoslideritem', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichheaderwithbackgroundvideoslideritem',
            name='video',
            field=filer.fields.file.FilerFileField(blank=True, help_text='Leaving this blank will make the image as the background.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ungleich_header_item_video', to='filer.File'),
        ),
        migrations.AlterField(
            model_name='ungleichhtmlonly',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichhtmlonly', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='ungleichsimpleheader',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='ungleich_page_ungleichsimpleheader', serialize=False, to='cms.CMSPlugin'),
        ),
    ]