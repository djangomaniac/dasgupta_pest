import django_filters
from django_filters import DateFilter, CharFilter
from .models import *
# from client.models import *


class OrderFilter(django_filters.FilterSet):
    order_id = CharFilter(field_name='order_id', lookup_expr='icontains')
    client_name = CharFilter(field_name='client__name', lookup_expr='icontains')
    # start_date = DateFilter(field_name='timestamp', lookup_expr='gte')
    # end_date = DateFilter(field_name='timestamp', lookup_expr='lte')
    # note = CharFilter(field_name='remark', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = ['order_id', 'client_name']
        # exclude = ['company', 'status', 'total', 'service']
