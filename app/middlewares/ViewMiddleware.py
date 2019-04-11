'''
    middleware 视图验权
    @author Philip
'''
from django.shortcuts import redirect
# 视图中间件
class ViewMiddleware():
    # request 过滤
    def process_request(self, request):
        if request.session['user']:
            return request
        else:
            return redirectToLogin(request)

# 重定向
def redirectToLogin(request):
    host = request.get_host()
    port = request.get_port()
    path = request.get_full_path()

    redirect_url = request.scheme + "://" + host + ":" + port + path

    return redirect("http://raddeana.tech?redirect_url=" + redirect_url)