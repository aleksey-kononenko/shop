from django.urls import path
from . import views


urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_login_form', views.user_login_form, name='user_login_form'),
]