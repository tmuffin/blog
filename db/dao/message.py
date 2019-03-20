'''
    dao 消息
    @author Philip
'''

from django.db import models
import django.utils.timezone as timezone

# 消息
class Message(models.Model):
    # 聊天者的ip
    ip = models.CharField(max_length = 15, null = False)

    # 消息内容
    content = models.CharField(max_length = 80, null = False)

    # 消息类型
    type = models.ForeignKey(Type, on_delete = models.DO_NOTHING, null = True)

    # 保存日期
    create_at = models.DateTimeField(default = timezone.now)

    # 最后修改日期
    update_at = models.DateTimeField(auto_now = True)