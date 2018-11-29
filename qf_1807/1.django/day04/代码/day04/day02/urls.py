"""day02 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 访问Http://127.0.0.1:8000/add_stu/
    # 新增学生数据
    url(r'^add_stu/', views.add_stu),
    # 删除学生数据
    # 访问Http://127.0.0.1:8000/del_stu/
    url(r'^del_stu/', views.del_stu),
    # 修改学生数据
    # 访问Http://127.0.0.1:8000/up_stu/
    url(r'^up_stu/', views.up_stu),
    # 查询学生数据
    url(r'^sel_stu/', views.sel_stu),
    # 插入拓展数据
    url(r'^add_stu_info/', views.add_stu_info),
    # 通过学生查询拓展表信息
    url(r'^sel_info_by_stu/', views.sel_info_by_stu),
    # 通过电话号码查询学生信息
    url(r'^sel_stu_by_info/', views.sel_stu_by_info),
    # 添加班级
    url(r'^add_grade/', views.add_grade),
    # 通过学生查询班级
    url(r'^sel_grade_by_stu/', views.sel_grade_by_stu),
    # 添加课程
    url(r'^add_cou/', views.add_cou),
    # 添加/删除课程和学生的关联关系
    url(r'^stu_cou/', views.stu_cou),

    # 返回首页index.html页面
    url(r'^index/', views.index),
]
