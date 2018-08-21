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

]