"""day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path

from app import views

urlpatterns = [
    # http://127.0.0.1:8080/admin/
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8080/hello/
    path('hello/', views.hello),
    # 插入学生信息
    # http://127.0.0.1:8080/add_stu/
    path('add_stu/', views.add_stu),
    # 删除学生信息
    path('del_stu/', views.del_stu),
    # 更新学生信息
    path('up_stu/', views.up_stu),
    # 查询学生信息
    path('sel_stu/', views.sel_stu),
]
