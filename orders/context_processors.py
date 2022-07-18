from .models import ProductInOrder, Order
from utils.Cart_Dict import GetDict

def get_card_info (request):
    return_dict = dict()
    session_key = request.session.session_key
    # print('Get cart info')
    if not session_key:
        request.session.cycle_key
    current_user = request.user
    if (current_user.id is not None) & (not current_user.is_superuser):
        try:
            order = Order.objects.get(customer=current_user, status_id=1)
            order_id = order.id
            if order:
                return_dict = GetDict(order_id)
        except Order.DoesNotExist:
            print('Error update cart')

    return return_dict
