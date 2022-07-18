from django.shortcuts import render
from utils.emails import SendingEmail
from utils.Cart_Dict import GetDict
from orders.models import Order, Status


def send_email(request):
    # print("Send email")
    return_dict = dict()
    if request.method == 'GET':
        data = request.GET
        # print(data)
        current_user = request.user
        try:
            order = Order.objects.get(customer=current_user, status_id=1)
            order_id = order.id
            return_dict = GetDict(order_id)
            return_dict['products_conf'] = return_dict['products']
            del return_dict['products']
            del return_dict['order_total_price']
            del return_dict['products_total_nmb']
            return_dict['order'] = order_id
            if order.status.id == 1:
                status = Status.objects.get(pk=2)
                order.status = status
                order.save(force_update=True)
            email = SendingEmail()
            email.sending_email(type_id=1, order=order)
            email.sending_email(type_id=2, email=order.customer.email, order=order)
        except Order.DoesNotExist:
            print('Error update')

    title = {'title': 'Заказ принят'}
    context = {**title, **return_dict}

    return render(request, 'emails_templates/thanks-for-order.html', context)
