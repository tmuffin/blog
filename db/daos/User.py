'''
    dao 用户
    @author Philip
'''
from django.db import models
from . import RoleDao

class UserDao(models.Model):
    # id
    id = models.CharField(max_length = 16, primary_key = True)

    # 名称
    name = models.CharField(max_length = 32, null = False)

    # 昵称
    nickname = models.CharField(max_length = 32, null = False)

    # 头像
    avatar = models.CharField(max_length = 128, null = True)

    # 邮箱
    email = models.CharField(max_length = 128, null = True)

    # 电话号码
    phone = models.CharField(max_length = 32, null = True)

    # 角色
    role = models.ForeignKey(RoleDao, on_delete = models.SET_NULL, null = False)