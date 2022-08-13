from django.shortcuts import render, redirect
from .models import Product, Baguette, BaguetteColor, BaguetteMaterial
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect


def item(request, product_id):
    itemByid = Product.objects.get(id=product_id)
    # print('Item page')
    price_discount = itemByid.price * (100 - itemByid.discount) / 100

    return render(request, 'products/item.html', {'title': 'Страница продукта', 'item': itemByid, 'price_discount': price_discount})


def upload_csv(request):
    if request.method == "POST":
        pass
    form = CsvImportForm()
    data = {"form": form}
    return render(request, "admin/csv_upload.html", data)


def get_url(request):
    if request.method == "POST":
        csv_file = request.FILES["csv_upload"]
        print(csv_file)
        file_data = csv_file.read().decode("utf-8")
        csv_data = file_data.split("\r\n")
        headers = csv_data[0].split(';')
        del headers[0]
        fields = [f.name for f in Baguette._meta.get_fields()]
        is_correct = True
        for header in headers:
            if header in fields:
                continue
            is_correct = False
            break
        if is_correct:
            #Make data dictionary
            for i in range(1, len(csv_data) - 1):
                product = csv_data[i].split(';')
                del product[0]
                data_item = dict(zip(headers, product))
                # color = BaguetteColor.objects.get(color=data_item['color'])
                # material = BaguetteMaterial.objects.get(material=data_item['material'])
                # baguette = Baguette.objects.get(name=data_item['name'])
                # baguette.color = color
                # baguette.material = material
                # baguette.save(force_update=True)
                baguette = Baguette.objects.update_or_create(**data_item)
                print(baguette)
        else:
            messages.warning(request, 'Ошибочный набор данных')
            print('Ошибка данных')
            return HttpResponseRedirect(request.path_info)


    return redirect("admin:index")
