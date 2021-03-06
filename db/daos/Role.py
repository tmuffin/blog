#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 角色
    @author Philip
'''
from django.db import models
from db.daos.Permission import PermissionDao

class RoleDao(models.Model):
    # 角色名称
    name = models.CharField(max_length = 16)

    # 权限
    permission = models.ManyToManyField(PermissionDao, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)

    # 指向数据库
    class Meta: 
        app_label = 'blog'