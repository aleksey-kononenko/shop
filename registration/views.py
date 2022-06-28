from django.shortcuts import render, redirect
from utils.Cart_Dict import GetDict
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from orders.models import Order


def registration(request):
    error = ''
    print('Make user')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print('yes')
            data = request.POST
            log = data['username']
            pswd = data['password']
            pswd2 = data['password2']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            if pswd == pswd2:
                # form.save()
                print('Пароли верны')
                user = User.objects.filter(username=log)
                if user:
                    print('пользователь существует')
                    user = authenticate(request, username=log, password=pswd)
                else:
                    print('регистрируем пользователя')
                    user = User.objects.create_user(username=log, email=email, first_name=first_name,
                                                    last_name=last_name, password=pswd)
                    user.save()
                print(user.username)
                login(request, user)
                return redirect('home')
            else:
                error = 'Ошибка подтверждения пароля'
                print('Ошибка пароля')
        else:
            print('no')
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
    print('User login form')
    if request.method == 'POST':
        data = request.POST
        log = data.get("log")
        password = data.get("Password")
        remember = data.get("rememberme")
        user = authenticate(request, username=log, password=password)
        if user is not None:
            login(request, user)
            new_order, created = Order.objects.get_or_create(customer=user, status_id=1)
            if not created:
                return_dict = GetDict(new_order.id)
    return redirect('home')


def user_logout(request):
    logout(request)

    return redirect('home')
