'''
    controller 内容
    @author Philip
'''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class Content:
    def query (self, request):
        return HttpResponse({})
    def save (self, request):
        return HttpResponse({})
    def update (self, request):
        return HttpResponse({})
    def remove (self, request):
        return HttpResponse({})
