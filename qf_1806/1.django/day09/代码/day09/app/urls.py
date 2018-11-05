from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from app import views

# 获取路由对象
router = SimpleRouter()

# 127.0.0.1:8080/app/article/[id]/
router.register('article', views.ArticleView)

urlpatterns = [
    url(r'^all_article/', views.all_article)
]
# 设置访问路由地址
urlpatterns += router.urls
