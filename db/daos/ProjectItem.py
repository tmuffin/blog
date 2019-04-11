'''
    dao 项目子项
    @author Philip
'''
from django.db import models
from . import Project

class ProjectItem (models.Model):
    # 作者
    project = models.ForeignKey(Project, on_delete = models.SET_NULL, null = False)

    # 子项标题
    title = models.CharField(max_length = 32)

    # 子项内容
    content = models.CharField(max_length = 80)

    # 保存日期
    createdAt = models.DateTimeField(auto_now = True)
    
    # 最后修改日期
    updatedAt = models.DateTimeField(auto_now = True)