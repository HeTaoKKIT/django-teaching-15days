from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse

from carts.models import ShoppingCart
from goods.models import Goods


def cart(request):
    if request.method == 'GET':
        # 返回购物车中的数据，不用区分登录和没有登录的情况
        # 因为所有数据只需从session中取值即可
        session_goods = request.session.get('goods')
        data = []
        if session_goods:
            for se_goods in session_goods:
                goods = Goods.objects.filter(pk=se_goods[0]).first()
                nums = se_goods[1]
                price = goods.shop_price * se_goods[1]
                data.append([goods, nums, price])
        # 需要将结构, 返回给页面
        #  [[商品对象，商品数量，商品价格], [商品对象，商品数量，商品价格]...]
        return render(request, 'cart.html', {'goods_all': data})


def add_cart(request):
    if request.method == 'POST':
        # 保存到session中
        # 1. 获取前端ajax提交的商品goods_id，商品数量nums
        # 2. 组装存储到session中的数据结构
        # [[goods_id, nums, is_select], [goods_id, nums, is_select]...]
        # 3. 如果加入到session中的商品已经存在于session中，则更新nums字段
        goods_id = int(request.POST.get('goods_id'))
        nums = int(request.POST.get('nums'))
        # 组装存储的结构，[商品id值，商品数量，商品选择状态]
        goods_list = [int(goods_id), int(nums), 1]
        # 判断session中是否保存了购物车数据
        # {‘goods’: [[id, nums, 1], [id, nums, 1]}
        session_goods = request.session.get('goods')
        if session_goods:
            # 修改
            flag = False
            for goods in session_goods:
                # goods为 [goods_id, nums, is_select]
                if goods[0] == goods_id:
                    goods[1] += nums
                    flag = True
            # 添加
            if not flag:
                session_goods.append(goods_list)
            request.session['goods'] = session_goods
            # session中保存的商品的个数
            goods_count = len(session_goods)
        else:
            # 第一次添加商品到session中时，保存键值对
            # 键为goods，值为[[goods_id, nums, is_select]]
            request.session['goods'] = [goods_list]
            goods_count = 1

        return JsonResponse({'code': 200,
                             'msg': '请求成功',
                             'goods_count': goods_count})


def count_cart(request):
    if request.method == 'GET':
        # [[goods_id, nums, is_select], [goods_id, nums, is_select]...]
        session_goods = request.session.get('goods')
        count = len(session_goods) if session_goods else 0
        return JsonResponse({'code': 200, 'msg': '请求成功', 'count':count})


def change_cart(request):
    if request.method == 'POST':
        # 获取前端ajax传递的goods_id，is_select, nums
        goods_id = int(request.POST.get('goods_id'))
        is_select = request.POST.get('is_select')
        nums = request.POST.get('nums')
        # 获取session中商品的信息
        session_goods = request.session.get('goods')
        for goods in session_goods:
            # goods: [goods_id, nums, is_select]
            if goods_id == goods[0]:
                # 修改session中的商品的数量和选择状态
                goods[1] = int(nums) if nums else goods[1]
                goods[2] = int(is_select) if is_select else goods[2]
        request.session['goods'] = session_goods
        return JsonResponse({'code': 200, 'msg': '请求成功'})


def del_cart(request, id):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        if user_id:
            # 登录情况，删除数据库中的数据
            ShoppingCart.objects.filter(user_id=user_id,
                                       goods_id=id).delete()
        # 不管登录与否, 删除session中的数据
        session_goods = request.session.get('goods')
        # [[goods_id, nums, is_select], [goods_id, nums, is_select]...]
        # 以下实现删除session中商品数据，如session_goods为 [[7,1,1],[5,1,0], [9,3,1]]
        # 删除goods_id为7的商品信息，最后结果为[[5,1,0], [9,3,1]]
        for goods in session_goods:
            if goods[0] == int(id):
                session_goods.remove(goods)
        request.session['goods'] = session_goods

        return HttpResponseRedirect(reverse('carts:cart'))

