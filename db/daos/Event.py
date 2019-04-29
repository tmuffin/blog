#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 事件
    @author Philip
'''
from django.db import models
from db.daos.User import UserDao
from db.daos.Tag import TagDao

class EventDao(models.Model):
    # 作者
    author = models.ForeignKey(UserDao, on_delete = models.SET_NULL, null = False)

    # 标签
    tags = models.ManyToManyField(TagDao, null = True)

    # 事件名称
    title = models.CharField(max_length = 32, null = False)
    
    # 描述
    description = models.CharField(max_length = 80)
    
    # 内容
    content = models.CharField(max_length = 384)

    # 事件结束时间
    start = models.DateTimeField(auto_now = True)

    # 事件开始时间
    end = models.DateTimeField(auto_now = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)

    # 指向数据库
    class Meta: 
        app_label = 'blog'