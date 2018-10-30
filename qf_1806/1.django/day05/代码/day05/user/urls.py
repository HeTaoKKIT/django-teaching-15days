
from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 首页
    url(r'index/', views.index, name='index'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),

    # 使用form表单验证注册参数
    url(r'^form_register/', views.form_register, name='form_register'),

]