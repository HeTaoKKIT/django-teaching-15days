from django.shortcuts import render
from django.http import JsonResponse


def add_cart(request):
    if request.method == 'POST':
        # 添加到session中的数据格式为:
        # key==>goods,
        # value==>[[id1, num], [id2, num], [id3, num]....]

        # 1.1 添加到购物车的数据，其实就是添加到session中
        # 1.2 如果商品已经加入到session中，则修改session中商品的个数
        # 1.3 如果商品没有添加到session中，则添加

        # 获取从ajax中传递的商品的id和商品的个数
        goods_id = request.POST.get('goods_id')
        goods_num = request.POST.get('goods_num')
        # 组装存储的数据结构
        goods_list = [goods_id, goods_num]
        # 判断在session中是否存储了商品信息
        if request.session.get('goods'):
            # 标识符: 用于判断当前加入到购物车的商品
            # 如果购物车中已经存在了该商品，则修改flag为1，否则flag还是为0
            flag = 0
            # 说明购物车中已经存储了商品信息
            session_goods = request.session['goods']
            for goods in session_goods:
                # 循环判断，判断加入到session中的商品是否已经存在于session中
                if goods_id == goods[0]:
                    goods[1] = int(goods[1]) + int(goods_num)
                    # 标识符，修改session中的商品后，标识符修改为1
                    flag = 1
            # flag为0，表示添加到session中的商品之前并没有添加
            if not flag:
                session_goods.append(goods_list)
            # 修改成功session中商品的信息
            request.session['goods'] = session_goods
            cart_count = len(session_goods)
        else:
            # 说明购物车中还没有存储商品信息
            data = []
            data.append(goods_list)
            request.session['goods'] = data
            cart_count = 1

        return JsonResponse({'code': 200, 'cart_count': cart_count})


def cart(request):
    if request.method == 'GET':
        # 需要判断用户是否登录， session['user_id']
        # 1. 如果登录，则购物车中展示当前登录用户的购物车表中的数据
        # 2. 如果没有登录，则购物车页面中展示session中的数据
        return render(request, 'cart.html')
