from django.contrib import admin
from django.urls import path
from Shop import views
urlpatterns = [
    path('pz/',views.index),
    path('', views.welcome),
    path('shop/', views.shop)
]
