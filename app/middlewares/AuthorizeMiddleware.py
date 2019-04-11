'''
    middleware 登陆
    @author Philip
'''

import re
import requests
from db.daos.User import User

# 视图中间件
class ViewMiddleware():
    # request 过滤
    def process_request(self, request):
        token = request.GET['token']
        
        if token:
            res = requests.get("http://raddeana.tech/api/token", params = { "token" = token }, timeout = 10)

            if res.status_code == 200:
                user = res.json()
                dor = User.create(user)

                if dor:
                    request.
        
        return request

# 重定向
def redirectToLogin(request):
    host = request.get_host()
    port = request.get_port()
    path = request.get_full_path()

    redirect_url = request.scheme + "://" + host + ":" + port + path

    return redirect("http://raddeana.tech?redirect_url=" + redirect_url)