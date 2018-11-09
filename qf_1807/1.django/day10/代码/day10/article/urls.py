
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from article import views


# 生成路由对象
router = SimpleRouter()
# 路由管理资源art
# 127.0.0.1:8090/api/article/art/
# 127.0.0.1:8090/api/article/art/1/  DELETE
router.register('art', views.ArticleView)

urlpatterns = [
    url(r'list/', views.list_art),
]
# router.urls生成资源对应的路由地址
urlpatterns += router.urls
