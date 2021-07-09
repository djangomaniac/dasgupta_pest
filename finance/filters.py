import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class CashFilter(django_filters.FilterSet):
    remark = CharFilter(field_name='remark', lookup_expr='icontains')
    start_date = DateFilter(field_name='timestamp', lookup_expr='gt')
    end_date = DateFilter(field_name='timestamp', lookup_expr='lt')

    class Meta:
        model = CashboxTransaction
        fields = ['remark']


class BankFilter(django_filters.FilterSet):
    remark = CharFilter(field_name='remark', lookup_expr='icontains')
    start_date = DateFilter(field_name='timestamp', lookup_expr='gt')
    end_date = DateFilter(field_name='timestamp', lookup_expr='lt')

    class Meta:
        model = BankTransaction
        fields = ['remark']
