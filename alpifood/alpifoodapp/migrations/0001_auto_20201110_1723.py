# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-11-10 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alpifoodapp', 'add_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='category',
            field=models.IntegerField(choices=[(1, 'Starter'), (2, 'Main course'), (3, 'Dessert')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Cooking'), (2, 'Ready'), (3, 'On the way'), (4, 'Delivered'), (5, 'Accepted')]),
        ),
    ]
