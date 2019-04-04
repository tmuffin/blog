'''
    dao 角色权限
    @author Philip
'''

from django.db import models
import django.utils.timezone as timezone

# 标签
class RolePermissions (models.Model):
  # 标签名称
  name = models.CharField(max_length = 20, null = False)

  # 标签颜色
  color = models.CharField(max_length = 80, null = True)

  # 标签描述
  description = models.CharField(max_length = 60, null = True)