'''
    dao 事件
    @author Philip
'''
from django.db import models
from . import User, Tag

class Event(models.Model):
    # 作者
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = False)

    # 标签
    tags = models.ManyToManyField(Tag, null = True)

    # 事件名称
    name = models.CharField(max_length = 32, null = False)
    
    # 描述
    description = models.CharField(max_length = 64)
    
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