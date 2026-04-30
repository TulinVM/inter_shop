from django.db import models
from users.models import User
from products.models import Product
#from phonenumbers import PhoneNumberField

#from phonenumber_field.modelfields import PhoneNumberField

#class Contact(models.Model):
    #phone = PhoneNumberField()


class Order(models.Model):
     STATUS_CHOICES = (
        ('new', 'Новый'),
        ('confirmed', 'Подтвержден'),
        ('shipped', 'Отправлен'),
        
    )
     
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     customer_name = models.CharField(max_length=255)
     address = models.TextField()
     created = models.DateTimeField(auto_now_add=True)
     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    #phone_number = models.PhoneNumberField(blank=True, null=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
