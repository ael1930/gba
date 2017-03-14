# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20161215_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='invested',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='trade',
            name='profitLoss',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
