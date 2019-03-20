# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

# 机器人页面
def index (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "index.html", context)
