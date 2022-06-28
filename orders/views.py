from django.http import JsonResponse
from .models import ProductInOrder, Order
from django.shortcuts import render
from utils.Cart_Dict import GetDict
from .services import get_cities, get_warehouses


def add_item2cart(request):
    print('Add to cart')
    session_key = request.session.session_key
    data = request.POST
    current_user = request.user
    new_order, created = Order.objects.get_or_create(customer=current_user, status_id=1)
    if not created:
        print('Заказ существует')
    else:
        print('Заказ создан')
    order_id = new_order.id
    product_id = data.get("product_id")
    nmb = int(data.get("nmb"))
    new_product, created = ProductInOrder.objects.get_or_create(order_id=order_id, product_id=product_id, defaults={"nmb": nmb, "session_key": session_key})
    if not created:
        if new_product.is_active:
            new_product.nmb += int(nmb)
        else:
            new_product.nmb = int(nmb)
            new_product.is_active = True
        new_product.save(force_update=True)

    return_dict = GetDict(order_id)

    return JsonResponse(return_dict)


def cart(request):
    print('CART test')
    return render(request, 'orders/cart.html', {'title': 'Корзина'})


def update_cart(request):
    return_dict = dict()
    print('UPDATE test')
    if request.POST:
        data = request.POST
        current_user = request.user
        order = Order.objects.get(customer=current_user, status_id=1)
        order_id = order.id
        # products = ProductInOrder.objects.filter(order_id=order.id)
        for name, value in data.items():
            if name.startswith('quanitySniper'):
                key = int(name.split("_")[1])
                nmb = int(value)
                try:
                    product = ProductInOrder.objects.get(order_id=order_id, product_id=key)
                    if nmb:
                        if product.nmb != nmb:
                            product.nmb = nmb
                    else:
                        product.is_active = False
                    product.save(force_update=True)
                except ProductInOrder.DoesNotExist:
                    print('Error update')
        return_dict = GetDict(order_id)
        title = {'title': 'Корзина'}
        context = {**title, **return_dict}
    return render(request, 'orders/cart.html', context)


def checkout(request):
    print('CHECKOUT test')
    current_user = request.user
    order = Order.objects.get(customer=current_user, status_id=1)

    return render(request, 'orders/checkout.html', {'title': 'Оформление заказа', 'order': order})


def search(request):
    print("Search city")
    if request.method == 'GET':
        q = request.GET.get('term', '')
        results = []
        len_reg = len(q)
        if len_reg > 2:
            cities = get_cities(q)
            print(results)
            for city in cities:
                new_dict = dict()
                descr = city['DescriptionRu']
                new_res = descr[:len_reg]
                ref = city['Ref']
                if new_res == q:
                    new_dict['DescriptionRu'] = descr
                    new_dict['Ref'] = ref
                results.append(new_dict)
        print(results)
        return JsonResponse(results, safe=False)


def search_wh(request):
    print("Search warehouse")
    return_dict = dict()
    if request.method == 'GET':
        # if request.is_ajax():
        data = request.GET
        ref = data['ref']
        print(ref)
        whs = get_warehouses(ref)
        print(whs)
        return_dict['DescriptionRu'] = data['city']
        return_dict['warehouse'] = list()
        for wh in whs:
            new_dict = dict()
            descr = wh['DescriptionRu']
            ref = wh['Ref']
            new_dict['DescriptionRu_wh'] = descr
            new_dict['Ref_wh'] = ref
            return_dict['warehouse'].append(new_dict)
        # print(return_dict)
        title = {'title': 'Корзина'}
        context = {**title, **return_dict}
        return render(request, 'orders/checkout.html', context)