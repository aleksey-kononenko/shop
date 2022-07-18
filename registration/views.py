from django.shortcuts import render, redirect
from utils.Cart_Dict import GetDict
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from orders.models import Order


def registration(request):
    error = ''
    # print('Make user')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = request.POST
            log = data['username']
            pswd = data['password']
            pswd2 = data['password2']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            if pswd == pswd2:
                user = User.objects.filter(username=log)
                if user:
                    user = authenticate(request, username=log, password=pswd)
                else:
                    user = User.objects.create_user(username=log, email=email, first_name=first_name,
                                                    last_name=last_name, password=pswd)
                    user.save()
                login(request, user)
                return redirect('home')
            else:
                error = 'Ошибка подтверждения пароля'
        else:
            error = 'Данные неверные'
    form = UserForm()
    context = {
        'form': form,
        'error': error,
        'title': 'Регистрация пользователя'
    }

    return render(request, 'registration/index.html', context)

def user_login_form(request):
    error = ''
    # print('User login form')
    if request.method == 'POST':
        data = request.POST
        log = data.get("log")
        password = data.get("Password")
        remember = data.get("rememberme")
        user = authenticate(request, username=log, password=password)
        if user is not None:
            login(request, user)
            # order = Order.objects.filter(customer=user, status_id=1)
    return redirect('home')


def user_logout(request):
    logout(request)

    return redirect('home')
