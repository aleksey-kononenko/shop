from django.template.loader import get_template
# from django.core.mail import EmailMessage
from django.core.mail import send_mail
from bestShop.settings import FROM_EMAIL, EMAIL_ADMIN
# from emails.models import EmailSendingFact
from django.forms.models import model_to_dict
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os



class SendingEmail(object):
    from_email = "БАГЕТНЫЙ ДВОР <%s>" % FROM_EMAIL
    reply_to_emails = [from_email]
    target_emails = []
    bcc_emails = []

    def sending_email(self, type_id, email=None, order=None):
        if not email:
            email = EMAIL_ADMIN
        target_emails = [email]
        vars = {}

        if type_id == 1:
            subject = "Новый заказ"
            vars["order_fields"] = model_to_dict(order)
            vars["order"] = order
            vars["products_in_order"] = order.productinorder_set.filter(is_active=True)
            message = get_template('emails_templates/order_notification_admin.html').render(vars)
        elif type_id == 2:
            subject = "Ваш заказ в магазине 'БАГЕТНЫЙ ДВОР' получен!"
            message = get_template('emails_templates/order_notification_customer.html').render(vars)

        response = send_mail(subject, message=message, html_message=message, from_email=self.from_email, recipient_list=target_emails, fail_silently=False)


