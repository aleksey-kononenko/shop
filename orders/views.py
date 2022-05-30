from django.http import JsonResponse
from .models import ProductInOrder, Order
from django.shortcuts import render


def add_item2cart(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    print(data)
    product_id = data.get("product_id")
    nmb = int(data.get("nmb"))

    new_product, created = ProductInOrder.objects.get_or_create(order_id=3, session_key=session_key, product_id=product_id, defaults={"nmb": nmb})
    if not created:
        new_product.nmb += int(nmb)
        new_product.save(force_update=True)

    products_in_cart = ProductInOrder.objects.filter(order_id=3, session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()
    return_dict["products_total_nmb"] = products_total_nmb
    order = Order.objects.filter(id=3)
    return_dict["order_total_price"] = order[0].total_price
    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["id"] = item.product.id
        product_dict["price"] = item.price_per_item
        product_dict["total"] = item.total_price
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def cart(request):
    session_key = request.session.session_key
    print('CART test')
    if request.POST:
        print(request.POST)

    return render(request, 'orders/cart.html', {'title': 'Корзина'})


def update_cart(request):
    return_dict = dict()
    print('UPDATE test')
    session_key = request.session.session_key

    if request.POST:
        data = request.POST
        print(data)
        for name, value in data.items():
            if name.startswith('quanitySniper'):
                product_id = int(name.split("_")[1])
                product_nmb = int(value)
                try:
                    product = ProductInOrder.objects.get(order_id=3, session_key=session_key, id=product_id)
                    if product.nmb != product_nmb :
                        product.nmb = product_nmb
                        print('Saved')
                        product.save(force_update=True)
                except ProductInOrder.DoesNotExist:
                    print('Error update')

                print(product.nmb)

    # return_dict["products_total_nmb"] = 1
    #
    # data = request.POST.dict()
    # qty = list()
    #
    # qty.append(1)
    # qty.append(2)
    # print(data)
    # print(qty)

    return render(request, 'orders/cart.html', {'title': 'Корзина'})
