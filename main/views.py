from django.shortcuts import render
from products.models import ProductImage
from .models import Slider


def index(request):
    # print('Main page')
    product_image = ProductImage.objects.filter(product__is_active=True, product__is_new=True, is_main=True)
    slider_image = Slider.objects.filter(is_show=True)

    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'product': product_image, 'slider': slider_image})
