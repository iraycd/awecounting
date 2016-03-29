# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 11:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0017_auto_20160124_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_transaction', to='inventory.InventoryAccount'),
        ),
    ]
