from django.contrib import auth
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Permission, Group
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserLoginForm
from user.models import MyUser
from utils.functions import check_permissions


def add_user_permission(request):
    if request.method == 'GET':
        # 1. 创建用户
        user = MyUser.objects.create_user(username='coco', password='123456')
        # 2. 指定刚创建的用户，并分配给它权限（新增用户权限， 查看用户权限）
        permissions = Permission.objects.filter(codename__in=['add_my_user',
                                                              'all_my_user']
                                                ).all()
        for permission in permissions:
            # 多对多的添加
            user.user_permissions.add(permission)
        # 3. 删除刚创建的用户的新增用户权限
        # user.user_permissions.remove(权限对象)

        return HttpResponse('创建用户权限成功')


@check_permissions
def index(request):
    # coco用户有查看用户列表权限，才能访问index函数。使用装饰器去写
    if request.method == 'GET':
        return render(request, 'index.html')


def add_group_permission(request):
    if request.method == 'GET':
        # 创建超级管理员(所有权限)、创建普通管理员（修改/查看权限）
        group = Group.objects.create(name='审核组')

        ps = Permission.objects.filter(codename__in=['change_my_user_username',
                                                     'change_my_user_password',
                                                     'all_my_user']).all()
        # 给组添加权限
        for permission in ps:
            group.permissions.add(permission)

        return HttpResponse('创建组权限成功')


def add_user_group(request):
    if request.method == 'GET':
        # 给coco用户分配审查组
        user = MyUser.objects.get(username='coco')
        group = Group.objects.get(name='审核组')
        # 分配组
        user.groups.add(group)

        return HttpResponse('用户分配组成功')


def show_user_permission(request):
    if request.method == 'GET':
        user = MyUser.objects.get(username='coco')
        return render(request, 'permissions.html', {'user': user})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'],
                                     password=form.cleaned_data['password'])
            if user:
                # request.user赋值，赋值为登录用户对象
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:my_index'))
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html', {'errors': form.errors})


def my_index(request):
    if request.method == 'GET':
        # 当前登录系统用户
        user = request.user
        # 获取当前用户对应组的权限
        user.get_group_permissions()
        # 获取当前用户的所有权限
        user.get_all_permissions()
        # 判断是否有某个权限
        user.has_perm('应用app名.权限名')
        return render(request, 'my_index.html')


@permission_required('user.delete_myuser')
def new_index(request):
    if request.method == 'GET':
        return HttpResponse('需要权限才能查看')
