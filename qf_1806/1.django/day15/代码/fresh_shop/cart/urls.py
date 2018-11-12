
from django.conf.urls import url

from cart import views

urlpatterns = [
    # 加入购物车
    url(r'add_cart/', views.add_cart, name='add_cart'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 结算
    url(r'place_order/', views.place_order, name='place_order'),
]