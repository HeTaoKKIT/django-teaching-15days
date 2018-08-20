from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import UserModel, UserTicketModel


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