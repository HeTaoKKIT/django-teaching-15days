
import random

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from user.forms import UserRegisterForm
from user.models import User, UserToken
from utils.functions import login_required


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        # 用于创建用户
        # 1. 获取参数
        name = request.POST.get('name')
        password = request.POST.get('pw')
        password2 = request.POST.get('pw2')
        # 2. 校验参数是否完整
        if not all([name, password, password2]):
            msg = '请填写完整的参数'
            return render(request, 'register.html', {'msg': msg})
        # 3. 先判断数据库中是否存在该name用户
        if User.objects.filter(name=name).first():
            msg = '该账号已注册，请去登录'
            return render(request, 'register.html', {'msg': msg})
        # 4. 校验密码是否一致
        if password2 != password:
            msg = '密码不一致'
            return render(request, 'register.html', {'msg': msg})
        # 5. 注册
        User.objects.create(name=name, password=password)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        # 1. 获取参数
        name = request.POST.get('name')
        password = request.POST.get('pw')
        # 2. 验证数据完整性
        if not all([name, password]):
            msg = '请填写完整的登录信息'
            return render(request, 'login.html', {'msg': msg})
        # 3. 验证用户是否注册
        user = User.objects.filter(name=name).first()
        if not user:
            msg = '该账号没有注册，请去注册'
            return render(request, 'login.html', {'msg': msg})
        # 4. 校验密码
        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})
        # 重点
        # 请求: 请求是从浏览器发送请求的时候，传递给后端的。
        # 响应: 后端返回给浏览器的
        res = HttpResponseRedirect(reverse('user:index'))
        # set_cookie(key, value, max_age/expires)
        token = ''
        s='1234567890qwertyuiopasdfghjklzxcvbnm'
        for i in range(25):
            token += random.choice(s)
        res.set_cookie('token', token, max_age=6000)

        # 存token值
        user_token = UserToken.objects.filter(user=user).first()
        if not user_token:
            UserToken.objects.create(token=token, user=user)
        else:
            user_token.token = token
            user_token.save()
        return res


# @login_required
def index(request):
    if request.method == 'GET':
        # token = request.COOKIES.get('token')
        # # 查询标识符是否有效
        # user_token = UserToken.objects.filter(token=token).first()
        # if not user_token:
        #     # 查询不到信息，说明用户没有登录
        #     return HttpResponseRedirect(reverse('user:login'))
        return render(request, 'index.html')


@login_required
def logout(request):
    if request.method == 'GET':
        # 1. 删除浏览器cookie中的token参数
        res = HttpResponseRedirect(reverse('user:login'))
        res.delete_cookie('token')
        # 2. 删除UserToken中的数据
        token = request.COOKIES.get('token')
        UserToken.objects.filter(token=token).delete()

        return res


def form_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        data = request.POST
        # data: {'name':'111', 'pw': '222', 'pw2':'3333'}
        # 将页面中提交的参数交给form表单做验证
        form = UserRegisterForm(data)
        if form.is_valid():
            # 验证通过
            # 密码加密
            password = make_password(form.cleaned_data.get('pw'))
            # 注册账号
            User.objects.create(name=form.cleaned_data.get('name'),
                                password=password)
            return HttpResponseRedirect(reverse('user:index'))
        else:
            # 验证不同通过，可以从form中获取错误的信息
            errors = form.errors
            return render(request, 'register.html', {'errors': errors})



