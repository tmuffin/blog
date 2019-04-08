'''
    dao 权限
    @author Philip
'''
from django.db import models

# 权限
class Permission(models.Model):
    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)