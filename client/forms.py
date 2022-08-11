from django.forms import ModelForm, HiddenInput, Select, EmailInput, Textarea, TextInput, FileInput, NumberInput
from .models import *


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'address': Textarea(attrs={'class': 'form-control'}),
        }


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
            'work_order_number': TextInput(attrs={'class': 'form-control'}),
            'work_order_period': TextInput(attrs={'class': 'form-control'}),
            'frequency': TextInput(attrs={'class': 'form-control'}),
            'CSR': NumberInput(attrs={'class': 'form-control'}),
        }


