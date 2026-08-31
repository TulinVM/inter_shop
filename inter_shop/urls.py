# inter_shop/urls.py
from django.contrib import admin
from django.urls import path, include
from products.views import IndexView
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'inter_shop'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('contacts/', include('contacts.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
