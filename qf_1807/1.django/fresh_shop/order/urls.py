
from django.conf.urls import url

from order import views

urlpatterns = [
    # 结算
    url(r'^place_order/', views.place_order, name='place_order'),
    # 下单
    url(r'^make_order/', views.make_order, name='make_order'),
    # 订单详情
    url(r'^user_order/', views.user_order, name='user_order'),
]