from django.shortcuts import render


# Create your views here.


def index(request):
    """
    获取网站首页
    :param request:
    :return:
    """
    return render(request, 'web/index.html')


def winery(request):
    """
    获取酒庄页面
    :param request:
    :return:
    """
    return render(request, 'web/winery.html')


def advisory(request):
    """
    获取资讯页面
    :param request:
    :return:
    """
    pass


def products(request):
    """
    获取产品页面
    :param request:
    :return:
    """
    return render(request, 'web/product.html')


def grape(request):
    """
    获取葡园页面
    :param request:
    :return:
    """
    return render(request, 'web/grape.html')


def college(request):
    """
    获取学院页面
    :param request:
    :return:
    """
    pass
