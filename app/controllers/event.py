'''
    controller 事件
    @author Philip
'''
from django.http import HttpResponse

class Event:
    def query (self, request):
        return HttpResponse({})
    def save (self, request):
        return HttpResponse({})
    def update (self, request):
        return HttpResponse({})
    def remove (self, request):
        return HttpResponse({})