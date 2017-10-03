# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from models import UserCMS

# Create your views here.
def welcome(request):
   nowtime=datetime.datetime.now()
   return render(request,'welcome.html',{
       "nowtime":nowtime,
    })


def index(request):
    if request.method == "POST":    #如果提交
        username = request.POST.get("username","")   #进行赋值
        password = request.POST.get("password","")   #进行赋值
        user_cms = UserCMS()
        user_cms.username=username
        user_cms.password=password
        user_cms.save( )
        return HttpResponseRedirect(reverse("list"))    #重定向到url.py的list
    else:
        return render(request,'index.html',{})

def list(request):
    all_user = UserCMS.objects.all()    #添加所有用户对象
    return render(request,'list.html',{
        "all_user":all_user    #传递用户对象
    })

def delete(request):
    if request.method == "POST":    #判断方法是不是POST
        username = request.POST.get("username","")  #
        password = request.POST.get("password","")
        USER_CMS = UserCMS()
        deluser = UserCMS.objects.filter(username=username,password=password)
        deluser.delete()
        return HttpResponseRedirect(reverse("list"))
    else:
        return render(request,'index.html',{})

def logout(request):
    nowtime=datetime.datetime.now()
    return render(request,'logout.html',{
         "nowtime":nowtime,
    })

