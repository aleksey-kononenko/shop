from django.shortcuts import render
from .models import Product


def item(request, product_id):
    itemByid = Product.objects.get(id=product_id)
    # print('Item page')
    price_discount = itemByid.price * (100 - itemByid.discount) / 100

    return render(request, 'products/item.html', {'title': 'Страница продукта', 'item': itemByid, 'price_discount': price_discount})
