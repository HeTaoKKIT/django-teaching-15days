
from django.urls import path

from user import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('my_login/',views.my_login, name='my_login'),
    path('hindex/', views.hindex, name='hindex'),
    path('my_logout/', views.my_logout, name='my_logout'),
]
