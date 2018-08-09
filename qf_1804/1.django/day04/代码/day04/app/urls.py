
from django.conf.urls import url

from app import views

urlpatterns = [
    # 127.0.0.1:8080/app/helloWorld/
    url(r'helloWorld/', views.hello),
    # 查询所有的学生信息
    url(r'selStudent/', views.selStu),
    # 查询age=15的学生信息
    url(r'filterStudent/', views.filterStu),
    # 增加数据
    url(r'addStudent/', views.addStu),
    # 删除数据
    url(r'delStudent/', views.delStudent),
    # 修改数据
    url(r'updateStudent/', views.updateStudent),
    # 一对一，关联查询
    url(r'OneToOneSelect/', views.oneToOneSelect),
    # 一对多，关联查询
    url(r'OneToManySelect/', views.OneToManySelect),
    # 添加班级
    url(r'addGrade/', views.addGrade),
    # 多对多，关联蹿下
    url(r'ManyToManySelect/', views.ManyToManySelect),
    # 添加课程
    url(r'addCource/', views.addCourse),
    # 返回页面，学生信息
    url(r'selStu/', views.selStus, name='sel_stu'),
    url(r'deleteStu/', views.deleteStu),
    url(r'updateStu/', views.updateStu),
    url(r'addStuCourse/(\d+)/', views.addStuCourse),
]
