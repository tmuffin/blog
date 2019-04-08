'''
    dao 事件
    @author Philip
'''
from django.db import models

class Event(models.Model):
    # 标签
    tags = models.CharField(max_length = 80)

    # 事件名称
    name = models.CharField(max_length=20)
    
    # 描述
    description = models.CharField(max_length=50)
    
    # 内容
    content = models.CharField(max_length=300)

    # 事件结束时间
    start = models.DateField()

    # 事件开始时间
    end = models.DateField()

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)