
from django.conf.urls import url

from cart import views

urlpatterns = [
    # 添加到购物车
    url(r'add_cart/', views.add_cart, name='add_cart'),
    # 购物车页面
    url(r'^cart/', views.cart, name='cart'),
]

