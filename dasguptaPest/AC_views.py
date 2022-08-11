from django.shortcuts import render, redirect
from client.models import Client
from finance.models import Bank, Cashbox
from order.models import Order
from order.filters import *
from client.filters import ClientFilter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='login')
def company_dashboard(request):
    qs = Cashbox.objects.filter(company__name='Asian Chemicals')
    cashbox = qs[0]
    qs = Bank.objects.filter(company__name='Asian Chemicals')
    bank = qs[0]
    orders = Order.objects.filter(company__name='Asian Chemicals')
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    clients = Client.objects.filter(company__name='Asian Chemicals')
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
        "title": "Asian Chemicals",
        "content": "Asian Chemicals Dashboard",
        "clients": clients,
        "cashbox": cashbox,
        "bank": bank,
        "orders": orders,
        "order_filter": order_filter,
        "client_filter": client_filter,
        "time": datetime.datetime.now().time(),
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def superview_page(request):
    orders = Order.objects.filter(company__name='Asian Chemicals')
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    p = Paginator(orders, 2)
    page = request.GET.get('page')
    page_order = p.get_page(page)
    context = {
        "title": "Asian Chemicals",
        "orders": page_order,
        "page_order": page_order,
        "order_filter": order_filter,
        "time": datetime.datetime.now().time(),
    }
    return render(request, 'superview_test.html', context)

