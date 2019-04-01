'''
    dao 消息
    @author Philip
'''

from django.db import models
import django.utils.timezone as timezone

# 消息
class Message(models.Model):
    