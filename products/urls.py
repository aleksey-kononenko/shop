from django.urls import path
from . import views


urlpatterns = [
    path('item/<int:product_id>', views.item, name='item'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    path('get_url', views.get_url, name='get_url'),
]