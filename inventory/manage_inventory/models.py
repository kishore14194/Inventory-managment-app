# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    product_id = models.CharField(unique=True, max_length=100)
    product_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product'


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, db_column='product_id')
    vendor = models.CharField(max_length=100)
    mrp = models.IntegerField()
    batch_number = models.IntegerField()
    batch_date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)


    class Meta:
        db_table = 'product_detail'
