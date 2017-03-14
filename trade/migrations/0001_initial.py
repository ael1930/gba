# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        ('match', '0002_auto_20161126_1728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invested', models.DecimalField(decimal_places=2, max_digits=5)),
                ('profitLoss', models.DecimalField(decimal_places=2, max_digits=5)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='login', to='market.Market')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match', to='match.Match')),
            ],
        ),
    ]
