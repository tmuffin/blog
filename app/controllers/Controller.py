'''
    controller 基类
    @author Philip
'''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class Controller:
    dto = None

    def __init__(self, dto):
        self.dto = dto

    # 批量查询
    def query(request):
        dict = request.GET

        pageSize = dict['pageSize']
        pageIndex = dict['pageIndex']

        del dict['pageSize']
        del dict['pageIndex']



    # 查询一个对象
    def queryOne(request):
        dict = request.GET
        data = self.dto.get(dict)

        return HttpResponse(data)
        
    # 创建
    def create(request):
        dict = request.POST

        data = self.dto.get(dict)

        return HttpResponse(data)

    # 更新
    def update(request):
        dict = request.POST

        data = self.dto.get(dict)

        return HttpResponse(data)

    # 批量删除
    def delete(request):
        ids = request.GET['ids']


    # 删除一个对象
    def deleteOne(request):
        id = request.GET['id']
        