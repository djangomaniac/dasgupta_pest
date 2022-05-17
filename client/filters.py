import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class ClientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')
    # start_date = DateFilter(field_name='timestamp', lookup_expr='gte')
    # end_date = DateFilter(field_name='timestamp', lookup_expr='lte')
    # note = CharFilter(field_name='remark', lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['name', 'phone']
        # exclude = ['client', 'company', 'status', 'total', 'service']


class SubClientFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    phone = CharFilter(field_name='phone', lookup_expr='icontains')

    class Meta:
        model = Sub_Client
        fields = ['name', 'phone']
