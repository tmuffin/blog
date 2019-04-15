'''
    dao 文件类型
    @author Philip
'''
from django.db import models

class FileTypeDao(models.Model):
    # 文件类型
    type = models.CharField(max_length = 32, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)