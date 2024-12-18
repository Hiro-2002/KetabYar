from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('allbooks/', views.book_list),
    path('book/', views.book_create)
]
