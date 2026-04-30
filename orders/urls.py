from django.urls import path
from . import views
#from orders.models import OrderView

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('success/', views.success, name='success'),
    path('confirmed/', views.confirmed_orders, name='confirmed_orders')
    #path('confirm/<int:order_id>/', views.confirm_order, name='confirm_order'),
    #path('orders', OrdersView, name='confirmed_orders'),
]
