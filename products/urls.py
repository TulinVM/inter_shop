#products/urls.py
from django.urls import path

from products.views import ProductsListView, ProductsListView1, basket_add, basket_remove
from orders.views import order_status

app_name = 'products'
app_name = 'orders'

urlpatterns = [
       path('', ProductsListView.as_view(), name='index'),
       path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
       path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
      # path('orders/<int:page>/', ProductsListView.as_view(), name='orders'),
       path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
       path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
       path('products1/<int:category_id>/', ProductsListView1.as_view(), name='products1'),
       path('order-status/', order_status, name='order_status')
]
