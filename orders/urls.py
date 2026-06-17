from django.urls import path
from . import views
from orders.models import OrderItem
from .views import OrderCreateView, OrderDetailView, UserOrdersView
from .views import (
    order_create,
    success,
    user_orders,
    order_detail,
    order_status,
)

urlpatterns = [

    path('create/',
        OrderCreateView.as_view(),
        name='create'
    ),

    path(
        '<int:order_id>/',
        OrderDetailView.as_view(),
        name='detail'
    ),

    path(
        '',
        UserOrdersView.as_view(),
        name='user_orders'
    ),
]