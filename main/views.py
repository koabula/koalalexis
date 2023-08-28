from django.shortcuts import render,redirect
from django.contrib import messages
import time
# 认证模块
from django.contrib import auth

# 对应数据库
from django.contrib.auth.models import User

from .models import invitecode

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def register(request):
    return render(request,'main/register.html')

def newusr(request):
    usrname=request.POST['usrname']
    pwd=request.POST['pwd']
    inputcode=request.POST['invitecode']
    post={}
    if invitecode.objects.filter(code=inputcode):
        User.objects.create_user(username=usrname,password=pwd)
        return redirect("/")
    else:
        post["msg"]="注册失败"
        return render(request,'message.html',{'post':post})