from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from user.forms import UserRegisterForm, UserLoginForm
from user.models import Article


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        data = request.POST
        # 校验form表单传递的参数
        form = UserRegisterForm(data)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            return HttpResponseRedirect(reverse('user:login'))
        else:
            return render(request, 'register.html', {'errors': form.errors})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        data = request.POST
        form = UserLoginForm(data)
        if form.is_valid():
            # 使用随机标识符也叫做签名token
            user = auth.authenticate(username=form.cleaned_data.get('username'),
                                     password=form.cleaned_data.get('password'))
            if user:
                # 登录, 向request.user属性赋值，默认为AnyouseUser，赋值为登录系统的用户对象
                # 1. 向页面的cookie中设置sessionid值，(标识符)
                # 2. 向django_session表中设置对应的标识符
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:index'))
            else:
                return render(request, 'login.html', {'msg': '密码错误'})
        else:
            return render(request, 'login.html', {'errors': form.errors})



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@login_required()
def logout(request):
    if request.method == 'GET':
        # 研究logout实现的功能？
        auth.logout(request)
        return HttpResponseRedirect(reverse('user:login'))


def add_article(request):
    if request.method == 'GET':
        return render(request, 'articles.html')

    if request.method == 'POST':
        # 获取数据
        img = request.FILES.get('img')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # 创建文章
        Article.objects.create(img=img,
                               title=title,
                               desc=desc)
        return HttpResponse('创建图片成功')


def show_article(request, id):
    if request.method == 'GET':
        article = Article.objects.get(pk=id)
        return render(request, 'show_articles.html', {'article': article})


def articles(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        # 查询所有文章对象，并进行分页
        articles = Article.objects.all()
        # 将所有文章进行分页，每一页最多三条数据
        paginator = Paginator(articles, 3)
        # 获取哪一页的文章信息
        arts = paginator.page(page)

        return render(request, 'arts.html', {'arts': arts})
