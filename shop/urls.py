from django.urls import path
from . import views


urlpatterns = [
    path('shop', views.shop, name='shop'),
    path('shop_filter', views.shop_filter, name='shop_filter'),
]