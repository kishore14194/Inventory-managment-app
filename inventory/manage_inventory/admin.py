# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Product, ProductDetail


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']

admin.site.register(Product, ProductAdmin)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ['product', 'vendor', 'quantity', 'status']


admin.site.register(ProductDetail, ProductDetailAdmin)