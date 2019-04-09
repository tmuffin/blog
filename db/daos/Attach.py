'''
    dao 附件
    @author Philip
'''
from django.db import models
from . import File

# 内容
class Attach(models.Model):
    # 文件
    file = models.ForeignKey(File, on_delete = models.SET_NULL, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)