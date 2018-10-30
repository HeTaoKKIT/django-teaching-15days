
from django.conf.urls import url

from user import views


urlpatterns = [
    # 注册，使用django自带的User模型
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 首页
    url(r'^index/', views.index, name='index'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),
    # 上传文章
    url(r'^add_article/', views.add_article, name='add_article'),
    # 查看文章
    url(r'^show_article/(\d+)/', views.show_article, name='show_article'),
    # 文章列表
    url(r'^articles/', views.articles, name='articles'),
]
