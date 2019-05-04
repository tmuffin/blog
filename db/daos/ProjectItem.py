#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 项目子项
    @author Philip
'''
from django.db import models
from db.daos.Project import ProjectDao

class ProjectItem(models.Model):
    # 项目
    project = models.ForeignKey(ProjectDao, on_delete = models.SET_NULL, null = False)

    # 子项标题
    title = models.CharField(max_length = 32)

    # 子项内容
    content = models.CharField(max_length = 128)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)

    # 指向数据库
    class Meta: 
        app_label = 'blog'