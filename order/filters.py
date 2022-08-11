import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, ChoiceFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    order_id = CharFilter(field_name='order_id', lookup_expr='icontains')
    sub_client = CharFilter(field_name='sub_client__name', lookup_expr='icontains')
    payment = ChoiceFilter(choices=Order.STATUS)
    csr_status = ChoiceFilter(choices=Order.CSR_value)

    # start_date = DateFilter(field_name='timestamp', lookup_expr='gte')
    # end_date = DateFilter(field_name='timestamp', lookup_expr='lte')
    # note = CharFilter(field_name='remark', lookup_expr='icontains')

    # class Meta:
    #     model = Order
    #     fields = []
    #     widgets = {
    #         'order_id': forms.TextInput(attrs={'class': 'form-control'}),
    #         'sub_client': forms.TextInput(attrs={'class': 'form-control'}),
    #         'payment': forms.Select(attrs={'class': 'form-control'}),
    #         'Start_date': forms.DateInput(attrs={'class': 'form-control'}),
    #     }
    #     # exclude = ['company', 'status', 'total', 'service']


class ColourFilter(django_filters.FilterSet):
    colour_code = ChoiceFilter(field_name='colour_code')

    class Meta:
        model = Order
        fields = ['colour_code']
        widgets = {
            'colour_code': forms.Select(attrs={'class': 'form-control'}),
        }
