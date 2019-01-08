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
    # 添加拓展信息
    path('add_stu_info/', views.add_stu_info),
    # 通过学生名称查找电话
    path('sel_phone_by_stu/', views.sel_phone_by_stu),
    path('sel_phone_by_stu2/', views.sel_phone_by_stu2),
    # 通过拓展表查找学生信息
    path('sel_stu_by_info/', views.sel_stu_by_info),
    # on_delete演示
    path('on_delete_stu/', views.on_delete_stu),
    # 添加班级信息
    path('add_grade/', views.add_grade),
    # 分配班级
    path('stu_grade/', views.stu_grade),
    # 通过学生查询班级
    path('sel_grade_by_stu/', views.sel_grade_by_stu),
    # 通过班级查询学生
    path('sel_stu_by_grade/', views.sel_stu_by_grade),
    # 添加课程信息
    path('add_course/', views.add_course),
    # 添加中间表的信息
    path('add_s_c/', views.add_s_c),
    # 访问首页
    path('index/', views.index),
]
