'''
    标签
    @author Philip
'''

from django.db import models
import django.utils.timezone as timezone

# 标签
class Tag (models.Model):
  # 类型名称
  name = models.CharField(max_length = 20, null = False)

  # keywords
  keywords = models.CharField(max_length = 80, null = True)