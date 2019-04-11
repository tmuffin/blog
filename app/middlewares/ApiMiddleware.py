'''
    middleware api 验权
    @author Philip
'''
from django.http import HttpResponse

class ApiMiddleware():
    # request 过滤
    def process_request(self, request):
        if request.session['user']:
            return request
        else:
            return HttpResponse(status = 401)