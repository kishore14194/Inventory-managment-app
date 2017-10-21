# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# class UserLogin(models.Model):
#     user_id = models.ForeignKey(User, db_column='user_id')
#     name = models.CharField(max_length=80, blank=True, null=True)
#     email = models.EmailField(max_length=75, blank=True)
#     is_dept_manager = models.BooleanField(default=False)
#     is_store_manager = models.BooleanField(default=False)
#
#     class Meta:
#         db_table = 'user_login'