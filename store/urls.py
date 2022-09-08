from django.urls import path, include
from store import views

urlpatterns = [
    path('', views.home.as_view(), name='homepage'),
    path('product/<int:pk>', views.product_detail.as_view(), name='product_detail'),
    path('register/', views.signUp, name='register'),
    path('postsignUp/', views.postsignUp),
    path('login/', views.signIn, name='login'),
    path('postsignIn/', views.postsignIn),
    path('fav/<int:id>/', views.favourite_add, name='favourite_add'),
    path('cart/', views.cart_details.as_view(), name='cart_details'),
]
