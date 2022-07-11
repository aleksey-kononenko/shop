from django.shortcuts import render
from django.http import JsonResponse
from products.models import *
from django.db.models import Q
import json


def shop(request):
    print('Shop page')
    return_dict = dict()
    return_dict['types'] = Type.objects.all()
    return_dict['categories'] = Category.objects.all()
    n = 6
    page = 1
    catalog = ProductImage.objects.filter(product__is_active=True, is_main=True)[:n]
    catalog_total_nmb = catalog.count()
    return_dict["catalog_total_nmb"] = catalog_total_nmb
    return_dict["catalog"] = list()
    min_price = max_price = catalog[0].product.price
    for item in catalog:
        product_dict = dict()
        if item.product.price > max_price: max_price = item.product.price
        if item.product.price < min_price: min_price = item.product.price
        product_dict["name"] = item.product.name
        product_dict["id"] = item.product.id
        product_dict["img"] = item.picture_small.url
        product_dict["price"] = item.product.price
        product_dict["discount"] = item.product.discount
        product_dict["description"] = item.product.description
        return_dict["catalog"].append(product_dict)
    # print(return_dict)
    return_dict['min_price'] = int(min_price)
    return_dict['max_price'] = int(max_price)
    title = {'title': 'Каталог'}
    context = {**title, **return_dict}

    return render(request, 'shop/catalog.html', context)


def shop_filter(request):
    print("Shop filter")
    n = 6
    page = 1
    return_dict = dict()
    if request.method == 'GET':
        data = request.GET
        if data:
            print(data)
            type_sel = data.getlist('types[]')
            category_sel = data.getlist('categories[]')
            is_discount = int(data.get('is_discount'))
            is_new = int(data.get('is_new'))
            min_price = int(data.get('min_price'))
            max_price = int(data.get('max_price'))
            is_select = len(type_sel) | len(category_sel)
            if is_select:
                # catalog = ProductImage.objects.filter(Q(product__type__in=type_sel) | Q(product__category__in=category_sel),
                #                                       product__is_active=True, is_main=True, (Q(product__price__lt=max_price) AND Q(product__price__gt=min_price)))[:n]
                catalog = ProductImage.objects.filter(Q(product__type__in=type_sel) | Q(product__category__in=category_sel), (Q(product__price__lte=max_price) & Q(product__price__gte=min_price)), product__is_active=True, is_main=True)[:n]
            else:
                # catalog = ProductImage.objects.filter(product__is_active=True, is_main=True).exlude(product__price__gt=max_price).exlude(product__price__lt=min_price)[:n]
                catalog = ProductImage.objects.filter((Q(product__price__lte=max_price) & Q(product__price__gte=min_price)), product__is_active=True, is_main=True)[:n]
            catalog_total_nmb = 0
            return_dict["catalog"] = list()
            for item in catalog:
                if (((item.product.discount > 0) & is_discount) | (not is_discount)) & ((is_new & item.product.is_new) | (not is_new)):
                    catalog_total_nmb += 1
                    product_dict = dict()
                    product_dict["name"] = item.product.name
                    product_dict["id"] = item.product.id
                    product_dict["img"] = item.picture_small.url
                    product_dict["price"] = item.product.price
                    product_dict["discount"] = item.product.discount
                    product_dict["description"] = item.product.description
                    return_dict["catalog"].append(product_dict)
            # | (is_discount == (item.product.discount > 0)) | (not is_new) | (not is_discount)  |  |  |
            return_dict["catalog_total_nmb"] = catalog_total_nmb
            print(return_dict)
    return JsonResponse(return_dict, safe=False)