from django.forms import ModelForm, HiddenInput, Select, EmailInput, Textarea, TextInput, FileInput, NumberInput
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class Sub_ClientForm(ModelForm):
    class Meta:
        model = Sub_Client
        fields = '__all__'
        widgets ={
            'client': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'address': Textarea(attrs={'class': 'form-control'}),
            'service_1': Select(attrs={'class': 'form-control'}),
            'service_2': Select(attrs={'class': 'form-control'}),
            'service_3': Select(attrs={'class': 'form-control'}),
            'service_4': Select(attrs={'class': 'form-control'}),
            'rate_1': NumberInput(attrs={'class': 'form-control'}),
            'rate_2': NumberInput(attrs={'class': 'form-control'}),
            'rate_3': NumberInput(attrs={'class': 'form-control'}),
            'rate_4': NumberInput(attrs={'class': 'form-control'}),
            'area_1': NumberInput(attrs={'class': 'form-control'}),
            'area_2': NumberInput(attrs={'class': 'form-control'}),
            'area_3': NumberInput(attrs={'class': 'form-control'}),
            'area_4': NumberInput(attrs={'class': 'form-control'}),
            'price_1': NumberInput(attrs={'class': 'form-control'}),
            'price_2': NumberInput(attrs={'class': 'form-control'}),
            'price_3': NumberInput(attrs={'class': 'form-control'}),
            'price_4': NumberInput(attrs={'class': 'form-control'}),
            'work_order_period': TextInput(attrs={'class': 'form-control'}),
            'frequency': TextInput(attrs={'class': 'form-control'}),
            'CSR': NumberInput(attrs={'class': 'form-control'}),
            'challan_text': Textarea(attrs={'class': 'form-control'}),
        }


