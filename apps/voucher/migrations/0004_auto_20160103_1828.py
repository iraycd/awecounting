# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0003_auto_20160103_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashreceiptrow',
            name='discount',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
