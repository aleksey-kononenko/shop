from django.db import models
from orders.models import Order

class EmailType(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип email'
        verbose_name_plural = 'Типы emails'


class EmailSendingFact(models.Model):
    type = models.ForeignKey(EmailType, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.type.name

    class Meta:
        verbose_name = 'Отправленный email'
        verbose_name_plural = 'Отправленные emails'
