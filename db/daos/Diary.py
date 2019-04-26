#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 日记
    @author Philip
'''
from django.db import models
from db.daos.User import UserDao
from db.daos.Tag import TagDao

class DiaryDao(models.Model):
    # 作者
    author = models.ForeignKey(UserDao, on_delete = models.SET_NULL)

    # 标签
    tags = models.ManyToManyField(TagDao, null = True)
    
    # 标题
    title = models.CharField(max_length = 32, null = False)

    # 内容
    content = models.CharField(max_length = 384)

    # 日记日期
    date = models.DateTimeField(auto_now = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)