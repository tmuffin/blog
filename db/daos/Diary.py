'''
    dao 日记
    @author Philip
'''
from django.db import models

class Diary (models.Model):
    # 标签
    tags = models.CharField(max_length = 80)
    
    # 内容
    content = models.CharField(max_length = 300)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)