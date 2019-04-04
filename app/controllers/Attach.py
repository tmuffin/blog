'''
    controller 附件
    @author Philip
'''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import Controller

class Attach(Controller):
    def queryOneByForeignKeyId(self, request):
        value = request.GET['value']
        key = request.GET['key']

        dict = {}
        dict[key] = value

        attachs = self.dto.all(dict)
        return HttpResponse(attachs)