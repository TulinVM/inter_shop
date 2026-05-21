from django import forms
from .models import Order
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class OrderlForm(forms.ModelForm):
    class Meta:
        model = Order
        fields =  [  #'__all__'
            'id',
            'user',
            # 'address',
            'status',
            # 'phone',
            'created',
                           
        ]      

        # widgets = {
        #     'phone': PhoneNumberPrefixWidget(initial='US'),
           
        }

