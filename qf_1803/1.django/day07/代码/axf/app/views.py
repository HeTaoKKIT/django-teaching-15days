from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse

from app.models import MainWheel, MainNav, MainMustBuy, \
    MainShop, MainShow, FoodType, Goods


def Home(request):

    if request.method == 'GET':
        mainwheels = MainWheel.objects.all()
        mainnavs = MainNav.objects.all()
        mainmustbuys = MainMustBuy.objects.all()
        mainshops = MainShop.objects.all()
        mainshows = MainShow.objects.all()

        data = {
            'mainwheels': mainwheels,
            'mainnavs': mainnavs,
            'mainmustbuys': mainmustbuys,
            'mainshops': mainshops,
            'mainshows': mainshows
        }
        return render(request, 'home/home.html', data)


def Market(request):
    if request.method == 'GET':

        return HttpResponseRedirect(reverse('axf:marketparams',
                                            kwargs={'typeid': 104749,
                                                    'cid': 0,
                                                    'sid': 0}))


def MarketParams(request, typeid, cid, sid):
    if request.method == 'GET':
        foodtypes = FoodType.objects.all()
        if cid == '0':
            goods = Goods.objects.filter(categoryid=typeid)
        else:
            goods = Goods.objects.filter(categoryid=typeid,
                                         childcid=cid)

        if sid == '0':
            pass
        elif sid == '1':
            goods = goods.order_by('-productnum')
        elif sid == '2':
            goods = goods.order_by('-price')
        elif sid == '3':
            goods = goods.order_by('price')


        childtypenames = FoodType.objects.filter(typeid=typeid).first().childtypenames
        # [['国产水果',14111], ['进口水果'：13321]]
        childtypenames_list = [i.split(':') for i in childtypenames.split('#')]
        data = {
            'foodtypes': foodtypes,
            'goods': goods,
            'typeid': typeid,
            'cid': cid,
            'sid': sid,
            'childtypenames_list': childtypenames_list
        }
        return render(request, 'market/market.html', data)
