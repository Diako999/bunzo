from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'register'),
    path('create_user/', views.create_user, name = 'create_user'),

]
