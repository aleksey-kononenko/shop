from django.db import models
from products.models import Product
from django.contrib.auth.models import User
# from registration.models import Customer
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Status(models.Model):
    name = models.CharField('Тип статуса', max_length=24, blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    address = models.CharField('Адрес доставки', max_length=128, blank=True, null=True, default='')
    total_price = models.DecimalField('Цена заказа', max_digits=8, decimal_places=2, default=0)
    comment = models.TextField('Коментарий', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s" % (self.customer.last_name, self.customer.first_name, self.customer.username)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    nmb = models.IntegerField('Количество', default=1)
    price_per_item = models.DecimalField('Цена за штуку', max_digits=8, decimal_places=2, default=0)
    total_price = models.DecimalField('Цена обшая', max_digits=8, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    session_key = models.CharField('Ключ сессии', max_length=32, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.product.name

    class Meta:
        verbose_name = 'Продукт в заказе'
        verbose_name_plural = 'Продукты в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


@receiver(post_save, sender=ProductInOrder)
def product_in_order_post_save(sender, instance, created, **kwargs):
    calc_order_total_price(instance)


@receiver(post_delete, sender=ProductInOrder)
def calc_price_in_order(sender, instance, **kwargs):
    calc_order_total_price(instance)


def calc_order_total_price(order_instance):
    order = order_instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    order_instance.order.total_price = order_total_price
    order_instance.order.save(force_update=True)
    # return order_total_price
