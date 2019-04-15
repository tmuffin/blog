'''
    dao 标签
    @author Philip
'''

from django.db import models

# 标签
class TagDao(models.Model):
  # 标签名称
  name = models.CharField(max_length = 32, null = False)

  # 标签颜色
  color = models.CharField(max_length = 32, null = True)

  # 标签描述
  description = models.CharField(max_length = 80, null = True)

  # 保存日期
  createdAt = models.DateTimeField(auto_now = True)
  
  # 最后修改日期
  updatedAt = models.DateTimeField(auto_now = True)