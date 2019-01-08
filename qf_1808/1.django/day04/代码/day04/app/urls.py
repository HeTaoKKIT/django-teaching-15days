
from django.urls import path, re_path

from app import views

urlpatterns = [
    # 127.0.0.1:8080/app/index/
    # re_path('index/(\d+)/', views.index),
    path('index/<int:id>/',views.index),
    path('name/<str:name>/', views.get_name),
    # path('float/<float:uid>/', views.get_float),  # 没有float类型
    path('get_uuid/', views.get_uuid),
    path('uuid/<uuid:uid>/', views.g_uuid),
    path('path/<path:path>/', views.get_path),

    # 接收多个参数
    # path('params/<int:year>/<int:month>/<int:day>/', views.params),
    # re_path('params/(\d+)/(\d+)/(\d+)/', views.params)
    re_path('params/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.params)
]