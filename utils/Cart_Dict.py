from orders.models import ProductInOrder, Order


def GetDict(id):
    return_dict = dict()
    products_in_cart = ProductInOrder.objects.filter(order_id=id, order__status=1, is_active=True)
    products_total_nmb = products_in_cart.count()
    return_dict["products_total_nmb"] = products_total_nmb
    order = Order.objects.filter(id=id)
    return_dict["order_total_price"] = order[0].total_price
    return_dict["order_product_price"] = order[0].product_price
    return_dict["order_discount"] = order[0].product_price - order[0].total_price
    return_dict["products"] = list()
    for item in products_in_cart:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["id"] = item.product.id
        product_dict["img"] = item.img
        product_dict["price"] = item.price_per_item
        product_dict["product_price"] = item.product_price
        product_dict["total"] = item.total_price
        product_dict["nmb"] = item.nmb
        product_dict["discount"] = item.product.discount
        return_dict["products"].append(product_dict)

    return return_dict