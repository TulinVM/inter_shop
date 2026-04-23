from django.contrib import admin

from products.models import Basket, Product, ProductCategory
from orders.models import Order

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'stripe_product_price_id', 'category')
    #readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('-name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
""""""    
class OrderAdmin(admin.TabularInline):
     model = Order
     list_display = ('user', 'prcustomer_name', 'address', 'created', 'status')
     fields = ('user', 'customer_name', 'address', 'created', 'status',)
     #readonly_fields = ('created_timestamp',)
     extra = 0

class OrderItemAdmin(admin.TabularInline):
     model = Order
     list_display = ('user', 'prcustomer_name', 'address', 'created', 'status', 'order', 'product', 'quantity', 'price')
     fields = ('user', 'customer_name', 'address', 'created', 'status', 'order', 'product', 'quantity', 'price')
     #readonly_fields = ('created_timestamp',)
     extra = 0


     """     


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
"""
