from django import views
from django.contrib import admin
from django.urls import URLPattern, path, include
from api import views



urlpatterns = [
    path('product-pagination',views.productPagination, name='productPagination')
]