'''
    dao 文件
    @author Philip
'''
from django.db import models
from . import FileType, Tag

# 文件
class File(models.Model):
    # 文件类型
    type = models.ForeignKey(FileType, on_delete = models.SET_NULL, null = False)

    # 文件名称
    name = models.CharField(max_length = 64, null = False)

    # 文件地址
    path = models.CharField(max_length = 256, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)