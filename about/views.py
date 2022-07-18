from django.shortcuts import render


def about(request):
    title = {'title': 'О магазине'}
    context = {**title}

    return render(request, 'about/about.html', context)