
from django.conf.urls import url

from article import views

urlpatterns = [
    # 创建文章
    # 127.0.0.1:8080/article/add_art/
    url(r'^add_art/', views.add_art, name='add'),
    # 文章列表
    url(r'^art/', views.art, name='art_list'),

]