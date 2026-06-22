#orders/forms.py
from django import forms
from .models import Order
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'customer_name',
            'address',
            'phone',
        )

        widgets = {
            # 'phone': PhoneNumberPrefixWidget(initial='US'),
            'customer_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Введите имя клиента'
                }
            ),

            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 1, 'placeholder': 'Введите адрес доставки'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Номер телефона = +79991234567'
                }
            ),
            }
