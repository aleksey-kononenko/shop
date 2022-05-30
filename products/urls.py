from django.urls import path
from . import views


urlpatterns = [
    path('item/<int:product_id>', views.item, name='item'),
]