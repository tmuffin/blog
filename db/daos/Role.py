'''
    dao 角色
    @author Philip
'''
from django.db import models
from . import Permission

class Role (models.Model):
    # 角色名称
    name = models.CharField(max_length = 16)

    # 权限
    permission = models.ManyToManyField(Permission, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)