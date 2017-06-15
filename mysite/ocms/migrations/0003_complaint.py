# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-14 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('ocms', '0002_auto_20170614_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_desc', models.CharField(default='code', max_length=50)),
                ('complaint_number', models.CharField(blank=True, editable=False, max_length=16, unique=True)),
                ('Complaint_Type', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='dept_name', chained_model_field='dept_name', on_delete=django.db.models.deletion.CASCADE, to='ocms.Complaint_Type')),
                ('dept_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ocms.Department')),
            ],
        ),
    ]
