# orders/urls.py
from django.urls import path
from .views import (OrderCreateView, OrderDetailView, UserOrdersView)
from . import views

app_name = 'orders'   # <-- ОБЯЗАТЕЛЬНО

urlpatterns = [

    path('create/',OrderCreateView.as_view(),name='create'),
    path('',UserOrdersView.as_view(),name='user_orders'),
    path('order_detail/<int:order_id>', OrderDetailView.as_view(), name='order_detail'),
    path('order-status/', views.order_status, name='order_status'),
]