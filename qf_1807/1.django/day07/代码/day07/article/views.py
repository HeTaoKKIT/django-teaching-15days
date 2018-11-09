from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from article.Artform import AddArtForm
from article.models import Article


def add_art(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')

    if request.method == 'POST':
        # 把提交的数据丢给表单AddArtForm做验证
        form = AddArtForm(request.POST, request.FILES)
        # is_valid()验证参数是否有效，如果参数验证成功，返回True，否则False
        if form.is_valid():
            # 表示字段验证成功
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            content = form.cleaned_data['content']
            icon = form.cleaned_data['icon']
            Article.objects.create(title=title,
                                   desc=desc,
                                   content=content,
                                   icon=icon)
            # 创建成功文章后，返回文章列表页面
            # return HttpResponseRedirect('/article/art/')
            # reverse('namespace:name')
            return HttpResponseRedirect(reverse('art:art_list'))
        else:
            # 表示字段验证失败，需要将错误信息返回给页面展示
            return render(request, 'add_article.html', {'form': form})


def art(request):
    if request.method == 'GET':
        # 文章列表页面
        page = int(request.GET.get('page', 1))
        # page = request.GET.get('page') if request.GET.get('page') else 1
        # 第一种: 使用切片完成分页
        # articles = Article.objects.all()[(page-1)*2: page * 2]
        # 第二种: Paginator
        # from django.core.paginator import Paginator
        articles = Article.objects.all()
        # 将所有数据按照每一页2条数据进行切块处理
        paginator = Paginator(articles, 2)
        # 获取分页中的第几页数据
        page = paginator.page(page)

        return render(request, 'art.html', {'page': page})

