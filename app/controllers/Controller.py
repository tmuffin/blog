'''
    controller 基类
    @author Philip
'''
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required

class Controller:
    dto = None

    def __init__(self, dto):
        self.dto = dto

    # 批量查询
    @login_required
    def query(self, request):
        dict = request.GET.dict()

        pageSize = dict['pageSize']
        pageIndex = dict['pageIndex']

        data = self.dto.query(dict, {
            'pageSize': pageSize,
            'pageIndex': pageIndex
        })

        if data == False:
            return HttpResponse(status = 501)
        else:
            return JsonResponse(data)

    # 查询一个对象
    @login_required
    def queryOne(self, request):
        dict = request.GET.dict()
        data = self.dto.queryOne(dict)

        if data == False:
            return HttpResponse(status = 501)
        elif data == None:
            return HttpResponse(status = 404)
        else:
            return JsonResponse(data)
        
    # 创建
    @login_required
    def create(self, request):
        dict = request.POST.dict()
        data = self.dto.create(dict)

        if data == False:
            return HttpResponse(status = 501)
        else:
            return JsonResponse(data)

    # 更新
    @login_required
    def update(self, request):
        dict = request.POST.dict()
        data = self.dto.update(dict)

        if data == False:
            return HttpResponse(status = 501)
        else:
            return JsonResponse(data)

    # 批量删除
    @login_required
    def delete(self, request):
        ids = request.GET.dict()['ids'].split(',')
        data = self.dto.delete(ids)
        
        if data == False:
            return HttpResponse(status = 501)
        else:
            return JsonResponse(data)


    # 删除一个对象
    @login_required
    def deleteOne(self, request):
        dict = request.GET()
        data = self.dto.deleteOne(dict)

        if data == False:
            return HttpResponse(status = 501)
        else:
            return JsonResponse(data)