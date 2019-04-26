#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 权限
    @author Philip
'''
from django.db import models

# 权限以增删改查, curd, 1-1-1-1
# 权限
class PermissionDao(models.Model):
    # 权限对象
    object = models.CharField(max_length = 32, null = False)

    # 权限级别
    permission = models.IntegerField(null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)