from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from goods.models import GoodsCategory


def goods_category_list(request):
    if request.method == 'GET':
        # 返回商品分类对象
        categorys = GoodsCategory.objects.all()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_list.html', {'categorys': categorys, 'types': types})


def goods_category_detail(request, id):
    if request.method == 'GET':
        # 返回商品分类对象，和分类枚举信息
        category = GoodsCategory.objects.filter(pk=id).first()
        types = GoodsCategory.CATEGORY_TYPE
        return render(request, 'goods_category_detail.html',
                      {'category': category, 'types': types})

    if request.method == 'POST':
        # 获取上传商品分类图片
        img = request.FILES.get('category_front_image')
        if img:
            # GoodsCategory.objects.filter().update()
            category = GoodsCategory.objects.filter(pk=id).first()
            category.category_front_image = img
            category.save()
            return HttpResponseRedirect(reverse('goods:goods_category_list'))
        else:
            error = '图片必填'
            return render(request, 'goods_category_detail.html', {'error': error})


def goods_list(request):
    if request.method == 'GET':
        # TODO: 查看所有的商品信息，并在goods_list.html页面中解析
        return render(request, 'goods_list.html')


def goods_add(request):
    if request.method == 'GET':
        # TODO: 页面中刷新分类信息
        return render(request, 'goods_detail.html')

    if request.method == 'POST':
        # TODO: 验证商品信息的完整性，数据的保存
        pass
