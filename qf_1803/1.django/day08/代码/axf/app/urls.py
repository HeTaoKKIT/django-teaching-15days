
from django.conf.urls import url

from app import views

urlpatterns = [
    # 首页
    url(r'^home/', views.Home, name='home'),
    # 闪购超市
    url(r'^market/', views.Market, name='market'),
    url(r'^marketparams/(?P<typeid>\d+)/(?P<cid>\d+)/(?P<sid>\d+)/', views.MarketParams, name='marketparams'),
    # 添加购物车
    url(r'^addtocard/', views.AddToCard, name='addtocard'),
    # 删除购物车
    url(r'subtocard/', views.SubToCard, name='subtocard'),
    # 刷新商品的数量
    url(r'goodsnum/', views.GoodNum, name='goodsnum'),
    # 购物车
    url(r'cart/', views.Cart, name='cart'),
    # 修改购物车商品的选择状态
    url(r'changeCartStatus/', views.changeCartStatus, name='changeCartStatus'),
    # 计算价格
    url(r'goodsCount/', views.goodsCount, name='goodsCount'),

]

