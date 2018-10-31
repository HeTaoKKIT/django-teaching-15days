
from django.conf.urls import url

from user import views

urlpatterns = [
    # 创建用户，并给用户分配权限
    url(r'^add_user_permission/', views.add_user_permission, name='add_user_permission'),
    # 用户名为coco用户,有查看用户列表权限 才能访问如下的视图函数
    url(r'^index/', views.index, name='index'),
    # 创建组，并分配组的权限
    url(r'^add_group_permission/', views.add_group_permission, name='add_group_permission'),
    # 给coco用户，分配审查组
    url(r'^add_user_group/', views.add_user_group, name='add_user_group'),
    # 查看用户的权限
    url(r'show_user_permission/', views.show_user_permission, name='show_user_permission'),
    # 登录
    url(r'^login/', views.login, name='login'),
    url(r'^my_index/', views.my_index, name='my_index'),
    url(r'^new_index/', views.new_index, name='new_index'),
]