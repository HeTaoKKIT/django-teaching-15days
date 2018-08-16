# 先写导入python自带的库
# 再写第三方提供的库
# 最后写自己定义的包或则库

from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from app import views

router = SimpleRouter()
router.register('student', views.StudentSource)

urlpatterns = [
    url(r'hello/', views.hello, name='hello')
]
urlpatterns += router.urls