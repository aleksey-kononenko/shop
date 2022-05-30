from django.shortcuts import render, redirect
# from .models import Customer
from .forms import UserForm
from django.contrib.auth.models import User


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('home')
        else:
            error = 'Данные неверные'
    form = UserForm()
    context = {
        'form': form,
        'error': error,
        'title': 'Регистрация пользователя'
    }
    return render(request, 'registration/index.html', context)