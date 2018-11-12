from django.shortcuts import render

from django.http import JsonResponse

from goods.models import Goods
from cart.models import ShoppingCart


def add_cart(request):
    if request.method == 'POST':
        # 加入到购物车，需判断用户是否登录
        # 如果登录，加入到购物车中的数据，其实就是加入到数据库中购物车表中(设计不好的办法)

        # 如果登录，加入到购物车中的数据，存储到session中（设计相对比较好的）
        # 如果没有登录，则加入到购物车中的数据，是加入到session中
        # session中存储数据: 商品id，商品数量，商品的选择状态
        # 如果登录，则把session中数据同步到数据库中（中间件同步数据）

        # 1. 获取商品id和商品数量
        goods_id = int(request.POST.get('goods_id'))
        goods_num = int(request.POST.get('goods_num'))
        # 2. 组装存到session中的数据格式
        goods_list = [goods_id, goods_num, 1]
        # {'goods':[[1,2,1],[2,5,1],[5,1,1]....]}
        if request.session.get('goods'):
            # 说明session中存储了加入到购物车的商品信息
            # 判断当前加入到购物车中的数据，是否已经存在于session中
            # 如果存在，则修改session中该商品的数量
            # 如果不存在，则新增
            flag = 0
            session_goods = request.session['goods']
            for goods in session_goods:
                # 判断如果加入到购物中数据，已经存在于session中，则修改
                if goods[0] == goods_id:
                    goods[1] = int(goods[1]) + int(goods_num)
                    flag = 1
            if not flag:
                # 如果不存在，则添加
                session_goods.append(goods_list)
            request.session['goods'] = session_goods
            goods_count = len(session_goods)
        else:
            data = []
            data.append(goods_list)
            request.session['goods'] = data
            goods_count = 1
        return JsonResponse({'code': 200, 'msg': '请求成功', 'goods_count': goods_count})


def cart(request):
    if request.method == 'GET':
        # 如果没有登录，则从session中取商品的信息
        # 如果登录，还是从session中取数据(保证数据库中的商品和session中商品一致)
        session_goods = request.session.get('goods')
        if session_goods:
            # 获取session中所有的商品id值
            goods_all = []
            for goods in session_goods:
                cart_goods = Goods.objects.filter(pk=goods[0]).first()
                goods_number = goods[1]
                total_price = goods[1] * cart_goods.shop_price
                goods_all.append([cart_goods, goods_number, total_price])
            # 获取商品对象
            # 前台需要商品信息，商品的个数，商品的总价
            # 后台返回结构[[goods objects, number, total_price],[goods objects, number, total_price]]
        else:
            goods_all = ''
        return render(request, 'cart.html', {'goods_all': goods_all})


def place_order(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id')
        carts = ShoppingCart.objects.filter(user_id=user_id,
                                            is_select=1).all()
        for cart in carts:
            # 给每一个购物车商品对象添加一个total_price属性，用于存储总价
            cart.total_price = int(cart.nums) * int(cart.goods.shop_price)
        return render(request, 'place_order.html', {'carts': carts})


