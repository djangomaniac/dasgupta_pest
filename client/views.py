from django.shortcuts import render, redirect
from .models import *
from .forms import *
from order.filters import OrderFilter
from order.models import Order
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def client_page(request, pk):
    client = Client.objects.get(id=pk)
    orders = Order.objects.filter(client__name=client.name)
    total_order = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
        "title": "Clients",
        "content": "Clients Page",
        "client": client,
        "orders": orders,
        "total_order": total_order,
        "order_filter": order_filter,
    }
    return render(request, 'client.html', context)


@login_required(login_url='login')
def client_detail_page(request, pk):
    client = Client.objects.get(id=pk)
    orders = Order.objects.filter(client__name=client.name)
    total_order = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
        "title": "Clients",
        "content": "Clients Page",
        "client": client,
        "orders": orders,
        "total_order": total_order,
        "order_filter": order_filter,
    }
    return render(request, 'client_detail.html', context)


@login_required(login_url='login')
def invoice_detail_page(request, pk):
    client = Client.objects.get(id=pk)
    orders = Order.objects.filter(client__name=client.name)
    total_order = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    context = {
        "title": "Clients",
        "content": "Clients Page",
        "client": client,
        "orders": orders,
        "total_order": total_order,
        "order_filter": order_filter,
    }
    return render(request, 'invoice_detail.html', context)


@login_required(login_url='login')
def create_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            client = Client.objects.latest('id')
            return redirect('client:client_view', client.id)
    context = {
        'form': form,
    }
    return render(request, 'client_form.html', context)


@login_required(login_url='login')
def update_client(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client:client_view', client.id)
    context = {
        'form': form,
    }
    return render(request, 'client_form.html', context)
