from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

from user.models import MyUser, TokenUser
from utils.functions import get_cookie_token


def index(request):
    # 返回随机值到cookie中
    res = HttpResponse('hello')
    # key表示设置的名称，value表示设置的值， max_age表示多少秒后过期，
    # expires表示datetime类型的日期，表示多久后过期
    res.set_cookie('token', '123123', 6000)
    # res.delete_cookie('token')

    return res


def get_token(request):
    # COOKIES: 传递客户端中的cookie内容
    # GET：获取http GET请求中传递的参数。如: 127.0.0.1:80/xxx/?id=1
    # POST: 获取http POST请求中传递的参数
    # FILES: 获取页面中传递的图片文件
    # path: 获取当前请求的ULR路径
    # method：获取请求方式
    if request.method == 'GET':
        token = request.COOKIES.get('token')
        # 做令牌是否有效的校验
        return HttpResponse('获取令牌')


def register(request):
    if request.method == 'GET':
        # GET 访问http://127.0.0.1:8000/register/
        return render(request, 'register.html')

    if request.method == 'POST':
        # 1. 先获取注册的账号和密码和确认密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # 2. 判断用户名是否已经被注册过
        user = MyUser.objects.filter(username=username).first()
        if user:
            # 已经存在该账号
            err_name = '该账号已被注册，请换一个账号注册'
            # return HttpResponse(err_name)
            return render(request, 'register.html', {'err_name': err_name})
        # 3. 判断密码和确认密码是否相同
        if password and password2:
            if password != password2:
                err_pwd = '密码和确认密码不一致，请修改密码'
                data = {
                    'err_pwd': err_pwd
                }
                return render(request, 'register.html', data)
        else:
            err_pwd = '密码不能为空'
            return render(request, 'register.html', {'err_pwd': err_pwd})

        # 4. 如果用户名不存在，且密码和确认密码相同，则实现注册，保存数据
        user = MyUser()
        user.username = username
        user.password = password
        user.save()
        # return render(request, 'login.html')
        # 实现跳转到登录页面
        return HttpResponseRedirect('/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 1. 获取登录提交的用户名和密码
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 2. 查询数据库中用户名和密码对应的用户对象
        user = MyUser.objects.filter(username=username,
                                     password=password).first()
        if not user:
            err = '用户名或者密码错误'
            return render(request, 'login.html', {'err': err})
        # 3. 登录操作
        # 给与登录成功的标识符（令牌），存在于cookie中
        res = HttpResponseRedirect('/my_index/')
        token = get_cookie_token()
        res.set_cookie('token', token, 6000)
        # 向TokeUser表中插入或更新数据
        token_user = TokenUser.objects.filter(user=user).first()
        # token_user = TokenUser.objects.filter(user_id=user.id).first()
        if token_user:
            token_user.token = token
            token_user.save()
        else:
            TokenUser.objects.create(token=token, user=user)
        # 4. 跳转到首页
        return res


def my_index(request):
    if request.method == 'GET':
        # 登录后才能访问index.html页面
        # 没有登录不让访问index.html，而是访问login.html页面
        # token = request.COOKIES.get('token')
        # if token == '123123':
        #     return render(request, 'index.html')
        # else:
        #     return HttpResponseRedirect('/login/')
        token = request.COOKIES.get('token')
        # 判断token是否有效
        token_user = TokenUser.objects.filter(token=token).first()
        if token_user:
            return render(request, 'index.html')
        else:
            return HttpResponseRedirect('/login/')
