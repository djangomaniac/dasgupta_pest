from django.shortcuts import render, redirect
from client.models import Client
from finance.models import Bank, Cashbox
from order.models import Order
from order.filters import OrderFilter
from client.filters import ClientFilter
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def company_dashboard(request):
    qs = Cashbox.objects.filter(company__name='Dasgupta Enterprise')
    cashbox = qs[0]
    qs = Bank.objects.filter(company__name='Dasgupta Enterprise')
    bank = qs[0]
    orders = Order.objects.filter(company__name='Dasgupta Enterprise')
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    clients = Client.objects.filter(company__name='Dasgupta Enterprise')
    client_filter = ClientFilter(request.GET, queryset=clients)
    clients = client_filter.qs
    # customer_filter = CustomerFilter(request.GET, queryset=customers)
    # customers = customer_filter.qs
    # order_filter = OrderFilter(request.GET, queryset=orders)
    # orders = order_filter.qs
    # total_orders = orders.count()
    # pending_orders = orders.filter(status='Pending').count()
    # delivered_orders = orders.filter(status='Delivered').count()
    # ordered_orders = orders.filter(status='Ordered').count()

    context = {
        "title": "Dasgupta Enterprise",
        "content": "Dasgupta Enterprise Dashboard",
        "clients": clients,
        "cashbox": cashbox,
        "bank": bank,
        "orders": orders,
        "order_filter": order_filter,
        "client_filter": client_filter,
    }
    return render(request, 'dashboard.html', context)
