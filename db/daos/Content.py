'''
    dao 内容
    @author Philip
'''
from django.db import models
from . import User, Tag

# 内容
class Content(models.Model):
    # 作者
    author = models.ForeignKey(User, on_delete = models.SET_NULL, null = False)

    # 关键字
    keywords = models.CharField(max_length = 64, null = False)

    # 标签
    tags = models.ManyToManyField(Tag, null = True)

    # 标题
    title = models.CharField(max_length = 32, null = False)

    # 内容
    content = models.CharField(max_length = 8192, null = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)