# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Customer(models.Model):
#     user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     email = models.EmailField('Email', blank=True, null=True, default=None)
#     password = models.CharField('Пароль', max_length=16)
#     last_name = models.CharField('Фамилия', max_length=42)
#     first_name = models.CharField('Имя', max_length=24)
#     phone_number = models.CharField('Номер телефона', max_length=13, blank=True, null=True, default=None)
#
#     def __str__(self):
#         return "%s %s %s" % (self.last_name, self.first_name, self.id)
#
#     class Meta:
#         verbose_name = 'Заказчик'
#         verbose_name_plural = 'Заказчики'
