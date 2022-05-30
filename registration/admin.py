from django.contrib import admin
# from .models import Customer
# from django.contrib.auth.models import User
#
#
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Customer._meta.fields]
#     list_filter = ['last_name']
#     search_fields = ['last_name', 'phone_number']
#     exclude = ['password'] #исключить поле
#     # fields = ['title'] #включить поле
#
#
#     class Meta:
#         model = User
#
#
# admin.site.register(Customer, CustomerAdmin)