'''
    dao 附件
    @author Philip
'''
from django.db import models
# 内容
class Attach(models.Model):
    # 附件类型
    fileType = models.CharField(max_length = 30, null = False)

    # 所有人
    owner = models.CharField(max_length = 30, null = False)

    # 文件保存路径
    path = models.CharField(max_length = 120, null = False)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)