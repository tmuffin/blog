# -*- coding: utf-8 -*-
#from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

# 首页
def home (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "home.html", context)

# 博客
def blog (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "blog.html", context)

# 航海
def voyage (request):
  context = {}
  context["env"] = settings.PY_ENV
  return render(request, "voyage.html", context)
