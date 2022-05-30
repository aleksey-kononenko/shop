# from .models import Customer
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput
from django.contrib.auth.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'last_name', 'first_name', 'username']
        widgets = {
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Фамилию*'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Имя*'
            }),
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер телефона*'
            }),
            "password": PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите пароль*'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Ваш email'
            }),

        }