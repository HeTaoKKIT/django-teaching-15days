
from django.conf.urls import url

from app import views


urlpatterns = [
    url(r'^stu/', views.index, name='index'),
    # url(r'^del_stu/(\d+)/', views.del_stu, name='del_stu'),
    url(r'^del_stu/(?P<s_id>\d+)/', views.del_stu, name='del_stu'),
]