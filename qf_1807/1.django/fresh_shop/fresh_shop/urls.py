"""fresh_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static

from fresh_shop import settings
from fresh_shop.settings import MEDIA_ROOT, MEDIA_URL
from django.views.static import serve

from goods import views

urlpatterns = [
    # 引入应用app中自己定义的路由文件urls.py
    url(r'user/', include('user.urls', namespace='user')),
    url(r'carts/', include('carts.urls', namespace='carts')),
    url(r'goods/', include('goods.urls', namespace='goods')),
    url(r'order/', include('order.urls', namespace='order')),

    url(r'^static/(?P<path>.*)$', serve, {"document_root": settings.STATICFILES_DIRS[0]}),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

    # 首页
    url(r'^$', views.index),
]
# 解析media文件中的静态资源
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

