#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 项目
    @author Philip
'''
from django.db import models
from . import UserDao, TagDao

class ProjectDao(models.Model):
    # 作者
    author = models.ForeignKey(UserDao, on_delete = models.SET_NULL, null = False)

    # 标签
    tags = models.ManyToManyField(TagDao, null = True)

    # 项目描述
    description = models.CharField(max_length = 80)

    # 项目标题
    title = models.CharField(max_length = 32, null = False)

    # 开始日期
    start = models.DateField(auto_noew = true)

    # 完成日期
    end = models.DateField(auto_noew = true)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)