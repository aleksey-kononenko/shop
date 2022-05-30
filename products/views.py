from django.shortcuts import render
from .models import Product


def item(request, product_id):
    itemByid = Product.objects.get(id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    # print(request.session.session_key)

    return render(request, 'products/item.html', {'title': 'Страница продукта', 'item': itemByid})