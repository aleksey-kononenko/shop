from .models import ProductInOrder, Order
from utils.Cart_Dict import GetDict

def get_card_info (request):
    return_dict = dict()
    session_key = request.session.session_key
    print('Get cart info')
    if not session_key:
        request.session.cycle_key
    current_user = request.user
    if current_user.id is not None:
        order, created = Order.objects.get_or_create(customer=current_user, status_id=1)
        if not created:
            return_dict = GetDict(order.id)

    return return_dict
