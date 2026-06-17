from django.urls import path
from . import views
from orders.models import OrderItem

app_name = 'orders'

urlpatterns = [
    path('create/', views.order_create, name='create'),
    path('success/', views.success, name='success'),
    path('confirmed/', views.user_orders, name='orders'),
    path('confirm/<int:order_id>/', views.confirm_order, name='confirm_order'),
    path('order-status/', views.order_status, name='order_status'),
    # path('orders/', views.confirmed_orders, name='confirmed_orders'),

    ###
   # path('profile/', views.profile, name='profile'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),

    # AJAX
    #path('confirm-ajax/', views.confirm_order_ajax, name='confirm_order_ajax'),
    #path('cancel-ajax/', views.cancel_order_ajax, name='cancel_order_ajax'),
    

]
