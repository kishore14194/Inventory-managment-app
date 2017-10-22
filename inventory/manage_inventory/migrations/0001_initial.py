# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 14:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, unique=True)),
                ('product_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(max_length=100)),
                ('mrp', models.IntegerField()),
                ('batch_number', models.IntegerField()),
                ('batch_date', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('product', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='manage_inventory.Product')),
            ],
            options={
                'db_table': 'product_detail',
            },
        ),
    ]
