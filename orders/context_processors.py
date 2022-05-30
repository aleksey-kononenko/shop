from .models import ProductInOrder, Order


def get_card_info (request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key

    products_in_cart = ProductInOrder.objects.filter(order_id=3, session_key=session_key, is_active=True)
    products_total_nmb = products_in_cart.count()
    order = Order.objects.filter(id=3)
    if order:
        order_total_price = order[0].total_price
    # try:
    #     print("enetered to mdw")
    #     user = request.user
    #     print(user)
    #     if not user.is_anonymous():
    #         print("not anon")
    #         profile = Profile.objacts.get(user=user)
    #         return  {"profile":profile}
    #     else:
    #         print("anonymous")
    #         pass
    # except:
    #     pass
    # is_act = "Ture"
    return locals()