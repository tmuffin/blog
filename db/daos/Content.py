'''
    dao 内容
    @author Philip
'''
from django.db import models
import django.utils.timezone as timezone

# 内容
class Content(models.Model):
    # 类型
    type = models.CharField(max_length = 15, null = True)

    # 作者
    author = models.CharField(max_length = 60, null = False)

    # 标题
    title = models.CharField(max_length = 30, null = False)

    # 关键字
    keywords = models.CharField(max_length = 30, null = False)

    # 标签
    tags = models.CharField(max_length = 30, null = False)

    # 内容
    content = models.CharField(max_length = 80, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)