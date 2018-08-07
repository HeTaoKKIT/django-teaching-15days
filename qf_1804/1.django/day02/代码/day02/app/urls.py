
from django.conf.urls import url

from app import views

urlpatterns = [
    # 127.0.0.1:8080/app/helloWorld/
    url(r'helloWorld/', views.hello),
    # 查询所有的学生信息
    url(r'selStudent/', views.selStu),
    # 查询age=15的学生信息
    url(r'filterStudent/', views.filterStu),
]
