from django.shortcuts import render
from products.models import ProductImage


def index(request):

    product_image = ProductImage.objects.filter(product__is_active=True, is_main=True)
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'product': product_image})
