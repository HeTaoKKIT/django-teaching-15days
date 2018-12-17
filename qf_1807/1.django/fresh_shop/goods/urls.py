
from django.conf.urls import url

from goods import views

urlpatterns = [
    # 首页
    # 127.0.0.1:8080/goods/index/
    url(r'^index/', views.index, name='index'),
    # 商品详情
    url(r'^detail/(\d+)/', views.detail, name='detail'),
]