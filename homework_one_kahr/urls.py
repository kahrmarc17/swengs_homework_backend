from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('animal/', views.animal_list),
    path('animal/<int:pk>/', views.animal_detail),
    path('zoo/', views.zoo_list),
    path('zoo/<int:pk>/', views.zoo_detail),
    path('zookeeper/', views.zookeeper_list),
    path('zookeeper/<int:pk>/', views.zookeeper_detail),
]
