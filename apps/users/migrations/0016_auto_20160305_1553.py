# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 10:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='used_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='used_pin', to='users.Company'),
        ),
    ]
