
from django.conf.urls import url

from app import views

urlpatterns = [
    # 首页
    url(r'^home/', views.Home, name='home'),
    # 闪购超市
    url(r'^market/', views.Market, name='market'),
    url(r'^marketparams/(?P<typeid>\d+)/(?P<cid>\d+)/(?P<sid>\d+)/', views.MarketParams, name='marketparams'),
]

