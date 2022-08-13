from django.shortcuts import render
from products.models import Baguette, BaguetteColor, BaguetteMaterial
from django.http import JsonResponse
from django.db.models import Q
from math import ceil


def constructor(request):
    print('Constructor page')
    return_dict = dict()
    return_dict['colors'] = BaguetteColor.objects.all()
    return_dict['materials'] = BaguetteMaterial.objects.all()
    n = 9       # Количество изделий на странице
    c_page = 1  # Текущая страница
    baguette = Baguette.objects.filter(is_active=True)
    baguette_total_nmb = baguette.count()
    return_dict["baguette_total_nmb"] = baguette_total_nmb
    page = ceil(baguette_total_nmb/n)
    return_dict["baguette_range"] = str((c_page-1)*n+1)+'-'+str(c_page*n)
    return_dict["page_total_nmb"] = list()
    if page <= 6:
        return_dict["page_total_nmb"] = range(1, page)
    else:
        return_dict["page_total_nmb"].append('1')
        return_dict["page_total_nmb"].append('2')
        return_dict["page_total_nmb"].append('3')
        return_dict["page_total_nmb"].append('...')
        return_dict["page_total_nmb"].append(str(page-1))
        return_dict["page_total_nmb"].append(str(page))
    return_dict["current_page"] = str(c_page)
    return_dict["baguette"] = list()
    for i in range((c_page-1)*n, c_page*n):
        baguette_dict = dict()
        baguette_dict["name"] = baguette[i].name
        baguette_dict["id"] = baguette[i].id
        baguette_dict["width"] = baguette[i].width
        baguette_dict["price"] = baguette[i].price
        return_dict["baguette"].append(baguette_dict)
    title = {'title': 'Конструктор рам'}
    context = {**title, **return_dict}

    return render(request, 'constructor/constructor.html', context)


def constructor_filter(request):
    print("Constructor filter")
    n = 9
    return_dict = dict()
    if request.method == 'GET':
        data = request.GET
        if data:
            material_sel = data.getlist('materials[]')
            color_sel = data.getlist('colors[]')
            width = data.get('range_width')
            c_page = int(data.get('current_page'))
            min_width = 10
            max_width = 90
            if width == '1':
                max_width = 39
            elif width == '2':
                min_width = 40
                max_width = 69
            elif width == '3':
                min_width = 70
                max_width = 90
            is_select = len(material_sel) | len(color_sel)
            if is_select:
                baguette = Baguette.objects.filter(Q(color__in=color_sel) | Q(material__in=material_sel), (Q(width__lte=max_width) & Q(width__gte=min_width)), is_active=True)
            else:
                baguette = Baguette.objects.filter((Q(width__lte=max_width) & Q(width__gte=min_width)), is_active=True)
            baguette_total_nmb = baguette.count()
            print(baguette_total_nmb)
            return_dict["baguette_total_nmb"] = baguette_total_nmb
            page = ceil(baguette_total_nmb / n)
            if c_page > page:
                c_page = 1
            return_dict["baguette_range"] = str((c_page - 1) * n + 1) + '-' + str(c_page * n)
            return_dict["page_total_nmb"] = list()
            return_dict["baguette"] = list()
            if page == 1:
                return_dict["page_total_nmb"].append('1')
            elif page <= 6:
                return_dict["page_total_nmb"] = list(range(1, page))
            elif c_page == 1:
                return_dict["page_total_nmb"].append('1')
                return_dict["page_total_nmb"].append('2')
                return_dict["page_total_nmb"].append('3')
                return_dict["page_total_nmb"].append('...')
                return_dict["page_total_nmb"].append(str(page - 1))
                return_dict["page_total_nmb"].append(str(page))
            elif (c_page > 1) & (c_page < (page-4)):
                return_dict["page_total_nmb"].append(str(c_page-1))
                return_dict["page_total_nmb"].append(str(c_page))
                return_dict["page_total_nmb"].append(str(c_page+1))
                return_dict["page_total_nmb"].append('...')
                return_dict["page_total_nmb"].append(str(page - 1))
                return_dict["page_total_nmb"].append(str(page))
            else:
                return_dict["page_total_nmb"].append(str(page - 5))
                return_dict["page_total_nmb"].append(str(page - 4))
                return_dict["page_total_nmb"].append(str(page - 3))
                return_dict["page_total_nmb"].append(str(page - 2))
                return_dict["page_total_nmb"].append(str(page - 1))
                return_dict["page_total_nmb"].append(str(page))
            print(return_dict["page_total_nmb"])
            if page == 1:
                end_range = baguette_total_nmb
            else:
                end_range = c_page*n
            for i in range((c_page-1)*n, end_range):
                baguette_dict = dict()
                baguette_dict["name"] = baguette[i].name
                baguette_dict["id"] = baguette[i].id
                baguette_dict["width"] = baguette[i].width
                baguette_dict["price"] = baguette[i].price
                return_dict["baguette"].append(baguette_dict)
            return_dict["current_page"] = str(c_page)
            return_dict["baguette_total_nmb"] = baguette_total_nmb
    return JsonResponse(return_dict, safe=False)