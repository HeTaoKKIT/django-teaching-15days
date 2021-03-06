
from django.conf.urls import url

from carts import views

urlpatterns = [
    # 购物车页面
    url(r'^cart/', views.cart, name='cart'),
    # 加入购物车
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    # 计算购物车中添加商品数量
    url(r'^count_cart/', views.count_cart, name='count_cart'),
    # 修改购物车中商品的勾选状态和商品数量
    url(r'^change_cart/', views.change_cart, name='change_cart'),
    # 删除购物车中的商品
    url(r'^del_cart/(\d+)/', views.del_cart, name='del_cart'),
]