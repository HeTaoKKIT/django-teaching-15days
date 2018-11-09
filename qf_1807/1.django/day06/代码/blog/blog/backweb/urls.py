from django.conf.urls import url

from backweb import views

urlpatterns = [
    # 127.0.0.1:8090/backweb/login/
    url(r'^login/', views.login),
]