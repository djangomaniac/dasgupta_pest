from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .filters import *
from order.filters import OrderFilter
from order.models import Order
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def client_page(request, pk):
    client = Client.objects.get(id=pk)
    sub_clients = Sub_Client.objects.filter(client__name=client.name)
    orders = Order.objects.filter(client__name=client.name)
    total_order = orders.count()
    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs
    sub_client_filter = SubClientFilter(request.GET, queryset=sub_clients)
    sub_clients = sub_client_filter.qs
    context = {
        "title": "Clients",
        "content": "Clients Page",
        "sub_clients": sub_clients,
        "client": client,
        "orders": orders,
        "total_order": total_order,
        "order_filter": order_filter,
        "sub_client_filter": sub_client_filter,
    }
    return render(request, 'client.html', context)


@login_required(login_url='login')
def sub_client_page(request, pk):
    sub_client = Sub_Client.objects.get(id=pk)
    orders = Order.objects.filter(sub_client__name=sub_client.name)
    last_paid = orders.filter(payment='Paid').last()
    total_order = orders.count()
    total_paid = orders.filter(payment='Paid').count()
    context = {
        "title": "Clients",
        "content": "Clients Page",
        "client": sub_client,
        "orders": orders,
        "total_order": total_order,
        "last_paid": last_paid,
        "total_paid": total_paid,
    }
    return render(request, 'sub_client.html', context)


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


@login_required(login_url='login')
def create_sub_client(request):
    if request.method == 'POST':
        form = Sub_ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sub_client = Sub_Client.objects.latest('id')
            client = sub_client.client
            return redirect('client:client_view', client.id)
    else:
        form = Sub_ClientForm()
    context = {
        'form': form,
    }
    return render(request, 'client_form.html', context)


@login_required(login_url='login')
def update_sub_client(request, pk):
    sub_client = Sub_Client.objects.get(id=pk)
    form = Sub_ClientForm(instance=sub_client)
    if request.method == 'POST':
        form = Sub_ClientForm(request.POST, request.FILES, instance=sub_client)
        if form.is_valid():
            form.save()
            client = sub_client.client
            return redirect('client:client_view', client.id)
    context = {
        'form': form,
    }
    return render(request, 'client_form.html', context)
