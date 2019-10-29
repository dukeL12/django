"""untitled4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse

from user import models


def index(request):
    print(request)
    print(type(request))
    return HttpResponse('hello magedu')

def login(request):
    if request.method=='GET':
        return render(request,'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        mysql_pwd = models.User.objects.filter(name=user).values('id','name','email','password')
        # print(mysql_pwd[0]["password"])
        if mysql_pwd[0]["password"]==pwd:
            # print(mysql_pwd[0]["password"])
            print(1)
            students_list = models.student.objects.all().values('sno','sname','cno')
            print(students_list)


            # return redirect('/Test/',{"students_list":students_list})
            return render(request, 'Test.html',{"students_list":students_list})
        else:
            print(request.method)
            msg = "用户名或密码错误"
            return render(request, 'login.html',{"msg":"用户名或密码错误"})
        # print(user,pwd)
        # return render(request, 'login.html')
def Test(request):
    return render(request, 'Test.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('Test/', Test),
    path('', index)

]
