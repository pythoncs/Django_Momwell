# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commodityapp', '0006_shopcart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='commodity_nums',
            field=models.IntegerField(default=1, null=True, verbose_name='商品数量'),
        ),
    ]
