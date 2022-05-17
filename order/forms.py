from django.forms import ModelForm, HiddenInput, TextInput, Select, Textarea
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'sub_client': Select(attrs={'class': 'form-control'}),
            'invoice_for_month': Select(attrs={'class': 'form-control'}),
            'date': TextInput(attrs={'class': 'form-control'}),
            'bill_raised': TextInput(attrs={'class': 'form-control'}),
            'payment': Select(attrs={'class': 'form-control'}),
            'payment_details': TextInput(attrs={'class': 'form-control'}),
            'csr_status': Select(attrs={'class': 'form-control'}),
            'remark': Textarea(attrs={'class': 'form-control'}),
            'client': HiddenInput(),
            'order_id': HiddenInput(),
            'uid': HiddenInput(),
            'company': HiddenInput(),
            'payment_date': HiddenInput(),
            'bank_transfer': HiddenInput(),
            'total': HiddenInput(),
            'service_1': HiddenInput(),
            'service_2': HiddenInput(),
            'service_3': HiddenInput(),
            'service_4': HiddenInput(),
            'price_1': HiddenInput(),
            'price_2': HiddenInput(),
            'price_3': HiddenInput(),
            'price_4': HiddenInput(),
            'area_1': HiddenInput(),
            'area_2': HiddenInput(),
            'area_3': HiddenInput(),
            'area_4': HiddenInput(),
            'rate_1': HiddenInput(),
            'rate_2': HiddenInput(),
            'rate_3': HiddenInput(),
            'rate_4': HiddenInput(),
            'work_order_period': HiddenInput(),
            'frequency': HiddenInput(),
            'challan_text': HiddenInput(),
            'CSR': HiddenInput(),
            'serial_no': HiddenInput(),
        }
