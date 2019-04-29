#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
    dao 附件
    @author Philip
'''
from django.db import models
from db.daos.File import FileDao
from db.daos.Diary import DiaryDao
from db.daos.Event import EventDao
from db.daos.Project import ProjectDao
from db.daos.Content import ContentDao

# 内容
class AttachDao(models.Model):
    # 标题
    title = models.CharField(max_length = 32, null = False)

    # 事件
    file = models.ForeignKey(FileDao, on_delete = models.SET_NULL, null = True)

    # 日志
    diary = models.ForeignKey(DiaryDao, on_delete = models.SET_NULL, null = True)

    # 内容
    event = models.ForeignKey(EventDao, on_delete = models.SET_NULL, null = True)

    # 项目
    project = models.ForeignKey(ProjectDao, on_delete = models.SET_NULL, null = True)

    # 内容
    content = models.ForeignKey(ContentDao, on_delete = models.SET_NULL, null = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)

    # 指向数据库
    class Meta: 
        app_label = 'blog'