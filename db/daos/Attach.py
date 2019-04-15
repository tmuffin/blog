'''
    dao 附件
    @author Philip
'''
from django.db import models
from . import FileDao, EventDao, ProjectDao, DiaryDao

# 内容
class AttachDao(models.Model):
    # 事件
    file = models.ForeignKey(FileDao, on_delete = models.SET_NULL, null = True)

    # 日志
    diary = models.ForeignKey(DiaryDao, on_delete = models.SET_NULL, null = True)

    # 内容
    event = models.ForeignKey(EventDao, on_delete = models.SET_NULL, null = True)

    # 项目
    project = models.ForeignKey(ProjectDao, on_delete = models.SET_NULL, null = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)