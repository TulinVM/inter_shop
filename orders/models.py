#orders/models.py
from django.db import models
from users.models import User
from products.models import Product
from phonenumber_field.modelfields import PhoneNumberField

from .managers import OrderQuerySet

class Contact(models.Model):
    # phone = PhoneNumberField()
    name = models.CharField(max_length=100)
    # phone = PhoneNumberField(region='RU', null=False, blank=False)  
    # По умолчанию для России


class Order(models.Model):
     
    STATUS_NEW = 'new'
    STATUS_CONFIRMED = 'confirmed'
    STATUS_SHIPPED = 'shipped'

    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('confirmed', 'Подтвержден'),
        ('shipped', 'Отправлен'),
        
    )
     
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=25, verbose_name='Имя клиента')
    address = models.TextField(verbose_name='Адрес доставки')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_NEW)
    phone = PhoneNumberField(region='RU', null=False, blank=False, verbose_name='Номер телефона') 

    objects = OrderQuerySet.as_manager()

    @property
    def total_sum(self):
        return sum(item.sum for item in self.items.all()) 
    
    @property
    def total_quantity(self):
        return sum(item.quantity for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def sum(self):
        return self.quantity * self.price