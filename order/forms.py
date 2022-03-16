from django.forms import ModelForm, HiddenInput
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'order_id': HiddenInput(),
            'uid': HiddenInput(),
            'company': HiddenInput(),
            'payment_date': HiddenInput(),
            'bank_transfer': HiddenInput(),
            'total': HiddenInput(),
            'rate_1': HiddenInput(),
            'rate_2': HiddenInput(),
            'rate_3': HiddenInput(),
            'rate_4': HiddenInput(),
        }
