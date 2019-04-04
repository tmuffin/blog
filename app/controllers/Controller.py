'''
    controller 基类
    @author Philip
'''
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class Controller:
    dto = None

    def __init__(self, dto):
        self.dto = dto

    # 批量查询
    @login_required
    def query(request):
        dict = request.GET()

        pageSize = dict['pageSize']
        pageIndex = dict['pageIndex']

        del dict['pageSize']
        del dict['pageIndex']

        allData = Book.objects.all(dict)
        paginator = Paginator(allData, pageSize)

        data = []
    
        try:
            print(page)
            data = paginator.page(pageSize)
        except PageNotAnInteger:
            data = []
        except EmptyPage:
            data = []

        json = {
            total: sizeof,
            data: data
        }

        return HttpResponse(json)

    # 查询一个对象
    @login_required
    def queryOne(request):
        dict = request.GET
        data = self.dto.get(dict)

        return HttpResponse(data)
        
    # 创建
    @login_required
    def create(request):
        dict = request.POST
        data = self.dto.get(dict)

        return HttpResponse(data)

    # 更新
    @login_required
    def update(request):
        dict = request.POST
        data = self.dto.get(dict)

        return HttpResponse(data)

    # 批量删除
    @login_required
    def delete(request):
        ids = request.GET['ids']
        
        return HttpResponse(data)


    # 删除一个对象
    @login_required
    def deleteOne(request):
        id = request.GET['id']
        return HttpResponse(data)