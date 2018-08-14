
import random
from datetime import datetime, timedelta

# from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from backweb.models import AType, Article, User, Permission, Role


def login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 验证用户名和密码是否正确
        user = auth.authenticate(request,
                              username=username,
                              password=password)
        # 验证用户成功
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('backweb:index'))
        else:
            return HttpResponseRedirect(reverse('backweb:login'))


def index(request):
    if request.method == 'GET':
        # 第一种方式：使用切片实现分页
        # page_num = request.GET.get('page', 1)
        # start_art = 1 * (int(page_num) - 1)
        # end_art = 1 * int(page_num)
        # articles = Article.objects.all()[start_art:end_art]
        # 第二种方式
        page_num = int(request.GET.get('page', 1))
        articles = Article.objects.all()
        paginator = Paginator(articles, 5)
        page = paginator.page(page_num)

        return  render(request, 'backweb/index.html', {'page': page})


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('backweb:login'))


def addArt(request):
    if request.method == 'GET':
        types = AType.objects.all()
        return render(request, 'backweb/article_detail.html', {'types': types})
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        a_type = request.POST.get('a_type')
        content = request.POST.get('content')
        img = request.FILES.get('img')

        Article.objects.create(title=title, desc=desc, atype_id=a_type,
                               content=content, image_url=img)

        return HttpResponseRedirect(reverse('backweb:index'))


def my_register(request):
    if request.method == 'GET':
        return render(request, 'backweb/register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 先验证用户是否注册过
        user = User.objects.filter(username=username).exists()
        if user:
            error = '用户名已注册，请直接登录'
            return render(request, 'backweb/register.html', {'error': error})
        else:
            # 两次密码正确
            if password2 == password1:
                User.objects.create(username=username, password=password1)
                return HttpResponseRedirect(reverse('backweb:my_login'))
            else:
                error = '两次密码不正确'
                return render(request, 'backweb/register.html', {'error': error})


def my_login(request):
    if request.method == 'GET':
        return render(request, 'backweb/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password).first()
        if user:
            # 账号密码正确
            # 第一步，cookie中设置
            res = HttpResponseRedirect(reverse('backweb:index'))
            s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
            session_id = ''
            for i in range(20):
                session_id += random.choice(s)
            out_time = datetime.now() + timedelta(days=1)
            res.set_cookie('session_id', session_id, expires=out_time)
            # 第二步。服务端存cookie中设的值
            user.session_id = session_id
            user.out_time = out_time
            user.save()

            return res
        else:
            error = '用户名或者密码错误'
            return render(request, 'backweb/login.html', {'error': error})


def my_logout(request):
    if request.method == 'GET':
        # 删除服务端的session_id值
        user = request.user
        user.session_id = ''
        user.save()
        # 删除cookie中的session_id值
        res = HttpResponseRedirect(reverse('backweb:my_login'))
        res.delete_cookie('session_id')
        return res


def addUser(request):
    if request.method == 'GET':
        return render(request, 'backweb/add_user.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.filter(username=username)
        if user:
            error = '该员工账号已添加'
            return render(request, 'backweb/add_user.html', {'error': error})
        else:
            if password1 == password2:
                User.objects.create(username=username, password=password1)
                # 创建用户成功，返回用户列表
                return HttpResponseRedirect(reverse('backweb:users'))
            else:
                error = '两次密码不一样'
                return render(request, 'backweb/add_user.html', {'error': error})


def listUser(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'backweb/users_list.html', {'users': users})

def rolePer(request):
    if request.method == 'GET':
        permissions = Permission.objects.all()
        return render(request, 'backweb/role_permission.html', {'permissions': permissions})
    if request.method == 'POST':

        role_name = request.POST.get('role_name')
        pers = request.POST.getlist('pers')

        role = Role.objects.create(r_name=role_name)
        for per in pers:
            p = Permission.objects.filter(p_name=per).first()
            role.r_p.add(p)
        return HttpResponseRedirect(reverse('backweb:users'))


def roleUser(request):
    if request.method == 'GET':
        users = User.objects.all()
        roles = Role.objects.all()
        return render(request, 'backweb/user_role.html',
                      {'roles': roles, 'users': users})
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        role_id = request.POST.get('role_id')
        user = User.objects.get(id=user_id)
        user.u_r_id = role_id
        user.save()
        return HttpResponseRedirect(reverse('backweb:users'))