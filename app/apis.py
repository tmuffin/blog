import urllib.request
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

from db.models import Type
from db.models import ChatRecord

def getTypes (request):
  per_page = request.GET["per_page"]
  curr_page = request.GET["curr_page"]
  name = request.GET["name"]

  types = Types.objects.filter(name__contains = name)
  paginator = Paginator(types, per_page)
      
  response = {
    "list": paginator.page(curr_page),
    "per_page": per_page,
    "curr_page": curr_page,
    "count": paginator.count,
    "name": name
  }
  
  return HttpResponse(response)

def addType (request):
  name = request.POST["name"]
  keywords = request.POST["keywords"]

  if name == None:
    response = {
      "errorMsg": "类型名称不可为空",
    }

    return HttpResponseNotAllowed(response)

  if keywords == None:
    keywords = ""

  add = Type(name = name, keywords = keywords)
  add.save()
  add.id

  response = {
    id: add.id
  }

  return HttpResponse(response)

def updateType (request):
  id = request.POST["id"]
  name = request.POST["name"]
  keywords = request.POST["keywords"]

  if id == None:
    response = {
      errorMsg: "类型id不可为空"
    }

    return HttpResponseNotAllowed(response)

  if name == None:
    response = {
      errorMsg: "类型名称不可为空"
    }

    return HttpResponseNotAllowed(response)

  type = Type.objects.get(id = id)
  type.name = name
  type.keywords = keywords
  type.save()

  response = {
    "msg": "更新类型成功"
  }

  return HttpResponse(response)

def deleteTypes (request):
  ids = request.POST["ids"]

  if ids == None:
    response = {
      "errorMsg": "ids不可为空"
    }

    return HttpResponseNotAllowed(response)

  for id in ids:
    Type.objects.filter(id = id).delete()

  response = {
    "msg": "删除成功"
  }

  return HttpResponse(response)



def getChatRecords (request):
  per_page = request.GET["per_page"]
  curr_page = request.GET["curr_page"]
  type = request.GET["type"]
  start_at = request.GET["start_at"]
  end_at = request.GET["end_at"]

  types = ChatRecord.objects.filter(type__contains = type).filter(create_at__gte = start_at).filter(type__lte = end_at)
  paginator = Paginator(types, per_page)
      
  response = {
    "list": paginator.page(curr_page),
    "per_page": per_page,
    "curr_page": curr_page,
    "count": paginator.count,
    "name": name
  }
  
  return HttpResponse(response)

def sendMessage (request):
  id = request.META["REMOTE_ADDR"]
  content = request.POST["content"]

  if content == None:
    response = {
      "errorMsg": "消息内容不可为空",
    }

    return HttpResponseNotAllowed(response)

  add = ChatRecord(id = id, content = content)
  add.save()
  add.id

  response = {
    id: add.id
  }

  return HttpResponse(response)
