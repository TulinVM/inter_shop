#products/urls.py
from django.urls import path

from products.views import ProductsListView, ProductsListView1, ProductsListView2,IndexView, basket_add, basket_remove 
#, IndexView1, basket_add, basket_remove
from . import views
# from contacts.views import ContactView

app_name = 'products'

urlpatterns = [
       path('', ProductsListView.as_view(), name='index'),
       # path('tel/', IndexView1.as_view(), name='tel'),
       path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
       # path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
      # path('orders/<int:page>/', ProductsListView.as_view(), name='orders'),
       path("basket/add/<int:product_id>/", basket_add, name="basket_add"),
       path("basket/remove/<int:basket_id>/", basket_remove, name="basket_remove"),
       path('products1/<int:category_id>/', ProductsListView1.as_view(), name='products1'),
       path('products2/<int:pk>/', ProductsListView2.as_view(), name='products2'),
       path('products/', ProductsListView.as_view(), name='products'),
]
