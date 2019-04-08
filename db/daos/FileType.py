'''
    dao 文件类型
    @author Philip
'''
from django.db import models

class FileType(models.Model):
    # 文件类型
    name = models.CharField(max_length=20)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)