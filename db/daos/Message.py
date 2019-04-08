'''
    dao 消息
    @author Philip
'''

from django.db import models

# 消息
class Message(models.Model):
    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)