# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_companysetting_discount_on_voucher_row'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companysetting',
            old_name='discount_on_voucher_row',
            new_name='discount_on_each_invoice_particular',
        ),
        migrations.RenameField(
            model_name='companysetting',
            old_name='discount_on_voucher',
            new_name='single_discount_on_whole_invoice',
        ),
        migrations.AddField(
            model_name='companysetting',
            name='discount_on_each_purchase_particular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companysetting',
            name='invoice_default_tax_application_type',
            field=models.CharField(blank=True, choices=[(b'no', b'No Tax'), (b'inclusive', b'Tax Inclusive'), (b'exclusive', b'Tax Exclusive')], default=b'inclusive', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companysetting',
            name='purchase_default_tax_application_type',
            field=models.CharField(blank=True, choices=[(b'no', b'No Tax'), (b'inclusive', b'Tax Inclusive'), (b'exclusive', b'Tax Exclusive')], default=b'inclusive', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='companysetting',
            name='single_discount_on_whole_purchase',
            field=models.BooleanField(default=True),
        ),
    ]
