# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-05 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_paytransactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paytransactions',
            name='sale_id',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.CASCADE, to='sales.Sale'),
        ),
    ]