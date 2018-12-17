
from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url(r'register/', views.register, name='register'),
    # 登录
    url(r'login/', views.login, name='login'),
    # 注销

    # 用户中心
    url(r'user_center/', views.user_center, name='user_center'),
    # 用户收货地址
    url(r'user_site/', views.user_site, name='user_site'),

]