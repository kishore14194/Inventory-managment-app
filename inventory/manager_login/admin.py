from __future__ import unicode_literals

from django.contrib import admin

from .models import UserLogin


class UserLoginAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'is_dept_manager', 'is_store_manager']

admin.site.register(UserLogin, UserLoginAdmin)

