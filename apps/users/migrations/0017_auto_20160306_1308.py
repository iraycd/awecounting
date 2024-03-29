# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax', '0004_partytaxpreference'),
        ('users', '0016_auto_20160305_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysetting',
            name='invoice_default_tax_scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_invoice_tax_scheme', to='tax.TaxScheme'),
        ),
        migrations.AddField(
            model_name='companysetting',
            name='purchase_default_tax_scheme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_purchase_tax_scheme', to='tax.TaxScheme'),
        ),
    ]
