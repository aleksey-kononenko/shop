from django.urls import path
from . import views


urlpatterns = [
    path('add_item2cart', views.add_item2cart, name='add_item2cart'),
    path('update_cart', views.update_cart, name='update_cart'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('search', views.search, name='search'),
    path('search_wh', views.search_wh, name='search_wh'),
]