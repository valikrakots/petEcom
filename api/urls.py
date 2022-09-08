from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.AllProducts.as_view(), name='api_products'),
    path('products/<int:id>/images/', views.ProductImages.as_view(), name='api_images'),
    path('page/', views.PageImages.as_view(), name='api_page'),
    path('register/', views.RegisterUser, name='api_registration'),
    path('login/', views.LoginUser, name='api_login')
]