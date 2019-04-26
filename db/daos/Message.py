#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 消息
    @author Philip
'''

from django.db import models
from . import UserDao

# 消息
class MessageDao(models.Model):
    # 作者
    author = models.ForeignKey(UserDao, on_delete = models.SET_NULL, null = False)

    # 标题
    title = models.CharField(max_length = 32, null = False)

    # 内容
    content = models.CharField(max_length = 384, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)