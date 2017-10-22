# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .utils import format_inventory
from .models import ProductDetail, Product


class InventoryActiveList(APIView):
    def get(self, request, format=None):
        all_pro = ProductDetail.objects.filter(status=True)
        active_products_list = []
        for one in all_pro:
            active_products = {}
            active_products['product_id'] = one.product.product_id
            active_products['product_name'] = one.product.product_name
            active_products['mrp'] = one.mrp
            active_products['batch_number'] = one.batch_number
            active_products['batch_date'] = str(one.batch_date)
            active_products['quantity'] = one.quantity
            active_products['status'] = one.status
            active_products_list.append(active_products)

        product_list = {"status": "success", "data": active_products_list}
        return HttpResponse(json.dumps(product_list))

class InventoryNotActive(APIView):
    def get(self, request, format=None):
        all_pro = ProductDetail.objects.filter(status=False)
        not_active_products_list = []
        for one in all_pro:
            not_active_products = {}
            not_active_products['product_id'] = one.product.product_id
            not_active_products['product_name'] = one.product.product_name
            not_active_products['mrp'] = one.mrp
            not_active_products['batch_number'] = one.batch_number
            not_active_products['batch_date'] = str(one.batch_date)
            not_active_products['quantity'] = one.quantity
            not_active_products['status'] = one.status
            not_active_products_list.append(not_active_products)

        product_list = {"status": "success", "data": not_active_products_list}
        return HttpResponse(json.dumps(product_list))


class InventoryAdd(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product_name = data.get('product_name')
        try:
            product = Product.objects.get(product_id=product_id)
        except:
            product = Product.objects.create(product_id=product_id, product_name=product_name)
            product.save()

        try:
            product_detail_obj = format_inventory(product, data)
            add_product = ProductDetail(**product_detail_obj)
            add_product.save()
        except :
            return HttpResponse(json.dumps({"status":"fail", "data": "Failed to add Inventory"}))

        return HttpResponse("added")

class InventoryApprove(APIView):
    def post(self, request, format=None):
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = Product.objects.get(product_id=product_id)
        active_users = ProductDetail.objects.filter(product=product, status=False)
        if not active_users:
            product_activate = {"status": "fail", "data": "No product to activate"}
            return HttpResponse(json.dumps(product_activate))

        if active_users:
            for product in active_users:
                product.status = True
                product.save()
        product_activate = {"status": "success", "data": product_id + " is activated"}
        return HttpResponse(json.dumps(product_activate))

class DeleteProduct(APIView):
    def delete(self, request, format=None):
        print request.body
        return HttpResponse("pass")