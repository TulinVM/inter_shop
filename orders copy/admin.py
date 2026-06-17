from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'status', 'created')
    list_filter = ('status',)

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


admin.site.register(OrderItem)

from django import forms
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.ModelForm):
    phone = PhoneNumberField(region='RU')

    class Meta:
        model = Contact
        fields = '__all__'