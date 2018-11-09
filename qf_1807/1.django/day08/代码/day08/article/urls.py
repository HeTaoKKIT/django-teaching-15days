
from django.conf.urls import url

from article import views

urlpatterns = [
    # 创建文章
    # 127.0.0.1:8080/article/add_art/
    url(r'^add_art/', views.add_art, name='add'),
    # 文章列表
    url(r'^art/', views.art, name='art_list'),
    # 文章删除（1）
    url(r'^del_art/',views.del_art, name='del_art'),
    # 文章删除（2）
    url(r'^del_art_id/(\d+)/', views.del_art_id, name='del_art_id'),
    # 文章编辑
    url(r'^edit_art/(\d+)/', views.edit_art, name='edit_art'),


    # 案例，接收多个参数
    url(r'^args/(\d+)/(\d+)/(\d+)/', views.args),
    url(r'^kargs/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.kargs),
    # 案例，过滤器
    url(r'^content/', views.content),

]