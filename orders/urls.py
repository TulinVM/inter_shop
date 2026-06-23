# orders/urls.py
from django.urls import path
from .views import OrderCreateView, OrderDetailView, UserOrdersView, order_create
from . import views

app_name = 'orders'   # <-- ОБЯЗАТЕЛЬНО

urlpatterns = [

    path('create/', views.order_create, name='create'),
    # path('create/',OrderCreateView.as_view(),name='create'),
    path('',UserOrdersView.as_view(),name='user_orders'),
    path('order_detail/<int:order_id>', OrderDetailView.as_view(), name='order_detail'),
    path('order-status/', views.order_status, name='order_status'),
    path('success/', views.success, name='success'),
    path('confirmed/', views.user_orders, name='orders'),
    # path('confirm/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('order-status/', views.order_status, name='order_status'),
    # path('orders/', views.confirmed_orders, name='confirmed_orders'),

    ###
   # path('profile/', views.profile, name='profile'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]