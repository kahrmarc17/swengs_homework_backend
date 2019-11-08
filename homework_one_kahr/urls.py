from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('animal/', views.animal_list),
    path('animal/<int:pk>/', views.animal_detail),
]
