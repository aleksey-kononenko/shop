from django.urls import path
from . import views


urlpatterns = [
    path('constructor', views.constructor, name='constructor'),
    path('constructor_filter', views.constructor_filter, name='constructor_filter'),
]