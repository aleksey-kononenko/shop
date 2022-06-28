# from .models import Customer
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, CheckboxInput
# from django.contrib.auth.models import User
from django import forms


class UserForm(forms.Form):

    # model = User
    # fields = ['email', 'password', 'last_name', 'first_name', 'username']
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    username = forms.TextInput()
    email = forms.EmailInput()
    password = forms.PasswordInput()
    password2 = forms.PasswordInput()
    # first_name.widget.attrs.update({
    #     'title': 'Пожалуйста введите вашу фамилию (не менее 3х символов)',
    #     'class': 'form-control',
    #     'placeholder': 'Введите фамилию*',
    #     'required minlength': '3',
    #     'value': '{{ request.POST.last_name }}'
    # })
    # widgets = {
    #     "last_name": TextInput(attrs={
    #
    #     }),
    #     "first_name": TextInput(attrs={
    #         'title': 'Пожалуйста введите ваше имя (не менее 3х символов)',
    #         'class': 'form-control',
    #         'placeholder': 'Введите имя*',
    #         'required minlength': '3',
    #     }),
    #     "username": TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Введите номер телефона*'
    #     }),
    #     "password": PasswordInput(attrs={
    #         'title': 'Пожалуйста введите пароль (5-12 символов)',
    #         'class': 'form-control',
    #         'placeholder': 'Введите пароль*',
    #         'required minlength': '5',
    #     }),
    #     "email": EmailInput(attrs={
    #         'title': 'Пожалуйста введите действительный email',
    #         'class': 'form-control',
    #         'placeholder': 'Введите Ваш email'
    #     }),
    # }