from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def DE_create_order(request):
    company = Company.objects.get(name='Dasgupta Enterprise')
    form = OrderForm(initial={'company': company})
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            order = Order.objects.latest('pk')
            return redirect('order:view_order', order.id)
    else:
        form.fields["client"].queryset = Client.objects.filter(company=company)
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def AC_create_order(request):
    company = Company.objects.get(name='Asian Chemicals')
    form = OrderForm(initial={'company': company})
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            order = Order.objects.latest('pk')
            return redirect('order:view_order', order.id)
    else:
        form.fields["client"].queryset = Client.objects.filter(company=company)
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def update_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    form = OrderForm(instance=order_obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order_obj)
        if form.is_valid():
            form.save()
            return redirect('client:client_view', order_obj.client.id)
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def next_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    # form = OrderForm(instance=order_obj)
    form = OrderForm(initial={
        'client': order_obj.client,
        'sub_client': order_obj.sub_client,
        'company': order_obj.company,
        'service': order_obj.service,
        'upload_document': order_obj.upload_document,
        'work_order_period': order_obj.work_order_period,
        'frequency': order_obj.frequency,
        'area': order_obj.area,
        'rate': order_obj.rate,
    })
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            order = Order.objects.latest('pk')
            return redirect('order:view_order', order.id)
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def view_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    context = {
        "order_obj": order_obj,
    }
    return render(request, 'view_order.html', context)


@login_required(login_url='login')
def invoice(request, pk):
    order_obj = Order.objects.get(id=pk)
    context = {
        "order_obj": order_obj,
    }
    return render(request, 'invoice.html', context)
