
from django.conf.urls import url

from app import views

urlpatterns = [
    # 127.0.0.1:8080/app/index/
    url(r'^index/', views.index),
    url(r'^all_stu/', views.all_stu),
]