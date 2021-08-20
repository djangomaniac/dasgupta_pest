from django.forms import ModelForm, HiddenInput
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'order_id': HiddenInput(),
            'company': HiddenInput(),
            # 'total': HiddenInput(),
        }
