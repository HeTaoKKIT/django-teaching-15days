
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import UserModel, UserTicketModel
from utils.functions import random_ticket


def mine(request):
    if request.method == 'GET':
        return render(request, 'mine/mine.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # 获取图片， enctype, MEDIA_URL, MEDIA_ROOT
        icon = request.FILES.get('icon')

        # 验证所有参数是否填写完整
        if not all([username, password, email, icon]):
            error = {'msg': '参数不能为空'}
            return render(request, 'user/user_register.html', error)
        # 验证用户是否被注册过
        user = UserModel.objects.filter(username=username)
        if user:
            error = {'msg': '该用户名已注册，请去登陆'}
            return render(request, 'user/user_register.html', error)
        # 创建用户
        UserModel.objects.create(username=username,
                                 password=make_password(password),
                                 email=email,
                                 icon=icon)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验参数
        if not all([username, password]):
            error = {'msg': '请填写完整的信息'}
            return render(request, 'user/user_login.html', error)
        # 校验用户名是否存在
        user = UserModel.objects.filter(username=username).first()
        if not user:
            error = {'msg': '该用户没有注册，请去注册'}
            return render(request, 'user/user_login.html', error)
        # 校验密码
        if not check_password(password, user.password):
            error = {'msg': '密码错误'}
            return render(request, 'user/user_login.html', error)

        # 用户名和密码验证成功，向cookie中和userticket表中存随机的字符串
        # 1. 向cookie中设值
        res = HttpResponseRedirect(reverse('user:mine'))
        ticket = random_ticket()
        out_time = datetime.now() + timedelta(days=1)
        res.set_cookie('ticket', ticket, expires=out_time)
        # 2. 向usertiket表中添加数据
        UserTicketModel.objects.create(user=user,
                                       ticket=ticket,
                                       out_time=out_time)

        return res


def logout(request):
    if request.method == 'GET':
        # 删除cookie中的值
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('ticket')
        # res.set_cookie(key, value, max_age=0)
        return res
