from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:id>/', views.customers, name='customer'),
    path('create_order/<str:id>/', views.create_order, name='create_order'),
    path('update_order/<str:id>/', views.update_order, name='update_order'),
    path('delete_order/<str:id>/', views.delete_order, name='delete_order'),
]
