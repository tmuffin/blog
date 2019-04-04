'''
    dao 附件
    @author Philip
'''
from django.db import models
import django.utils.timezone as timezone

# 内容
class Attach(models.Model):
    # 作者
    type = models.CharField(max_length = 60, null = False)

    # 作者
    author = models.CharField(max_length = 60, null = False)

    # 作者
    author = models.CharField(max_length = 60, null = False)

    # 保存日期
    created_at = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updated_at = models.DateTimeField(auto_now = True)