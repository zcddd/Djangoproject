# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserCMS     #导入模型类
# Register your models here.

class UserAdmin(admin.ModelAdmin):     #继承admin.ModelAdmin,创建模型管理类
    pass

admin.site.register(UserCMS,UserAdmin)      #将模型类与模型管理类注册到admin
