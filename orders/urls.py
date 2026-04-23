from django.urls import path
from . import views
#from orders.models import OrderView

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('success/', views.success, name='success'),
    path('confirmed/', views.confirmed_orders, name='confirmed')
    #path('orders', OrdersView, name='confirmed_orders'),
]
