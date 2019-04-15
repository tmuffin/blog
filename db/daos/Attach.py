'''
    dao 附件
    @author Philip
'''
from django.db import models
from . import File, Event, Project, Diary

# 内容
class Attach(models.Model):
    # 事件
    file = models.ForeignKey(File, on_delete = models.SET_NULL, null = True)

    # 日志
    diary = models.ForeignKey(Diary, on_delete = models.SET_NULL, null = True)

    # 内容
    event = models.ForeignKey(Event, on_delete = models.SET_NULL, null = True)

    # 项目
    project = models.ForeignKey(Project, on_delete = models.SET_NULL, null = True)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)