from django.conf.urls import url

from home import views

urlpatterns = [
    # 首页
    url(r'index/', views.index, name='index'),
    # 闪购页面
    url(r'market/', views.market, name='market'),
    url(r'market_params/(?P<typeid>\d+)/(?P<cid>\d+)/(?P<sid>\d+)/', views.marketParms, name='market_params'),
    # 添加商品
    url(r'add_to_cart/', views.add_to_card, name='add_to_card'),
    # 删除商品
    url(r'sub_to_cart/', views.sub_to_cart, name='sub_to_cart'),
    # 刷新闪购页面商品初始值
    url(r'refresh_goods/', views.refresh_goods, name='refresh_goods'),
    # 购物车
    url(r'cart/', views.cart, name='cart'),
    # 改变购物车中商品的勾选状态
    url(r'change_cart_goods/', views.change_cart_goods, name='change_cart_goods'),
    # 计算总价
    url(r'goods_count/', views.goods_count, name='goods_count'),
    # 改变购物车中所有商品的勾选状态
    url(r'change_all_cart_goods/', views.change_all_cart_goods, name='change_all_cart_goods'),
]