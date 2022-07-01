from django.db import models
from products.models import Product, ProductImage
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

def default_user():
    return User.objects.get(username='alex').pk

class Order(models.Model):
    customer = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, db_constraint=False)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    address = models.CharField('Адрес доставки', max_length=128, blank=True, null=True, default='')
    total_price = models.DecimalField('Окончательная цена', max_digits=8, decimal_places=2, default=0)
    product_price = models.DecimalField('Начальная цена', max_digits=8, decimal_places=2, default=0)
    comment = models.TextField('Коментарий', blank=True, null=True, default=None)
    cupon = models.CharField('Купон', max_length=12, blank=True, null=True, default='')
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
    img = models.CharField('Сcылка на картинку', max_length=128, default=None)
    nmb = models.IntegerField('Количество', default=1)
    product_price = models.DecimalField('Цена за штуку', max_digits=8, decimal_places=2, default=0)
    price_per_item = models.DecimalField('Цена со скидкой', max_digits=8, decimal_places=2, default=0)
    total_price = models.DecimalField('Цена обшая', max_digits=8, decimal_places=2, default=0)
    review = models.TextField('Отзыв', blank=True, null=True, default=None)
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
        product_price = self.product.price
        price_per_item = product_price * (100 - self.product.discount) / 100
        self.product_price = product_price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item
        product_image = ProductImage.objects.get(product_id=self.product.id, is_main=True)
        self.img = product_image.picture_small.url

        super(ProductInOrder, self).save(*args, **kwargs)


@receiver(post_save, sender=ProductInOrder)
def product_in_order_post_save(sender, instance, created, **kwargs):
    calc_order_total_price(instance)


@receiver(post_delete, sender=ProductInOrder)
def calc_price_in_order(sender, instance, **kwargs):
    calc_order_total_price(instance)


def calc_order_total_price(order_instance):
    order = order_instance.order
    print('Calculate order price')
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0   # Окончательная цена со скидкой
    order_product_price = 0 # Цена заказа без скидки
    for item in all_products_in_order:
        order_total_price += item.total_price
        order_product_price += item.product_price * item.nmb
    order_instance.order.total_price = order_total_price
    order_instance.order.product_price = order_product_price
    order_instance.order.save(force_update=True)
