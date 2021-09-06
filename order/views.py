from django.shortcuts import render, redirect
from .models import *
from .forms import *
from finance.models import *
from django.contrib.auth.decorators import login_required
import datetime


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
def amount_pay(request, pk):
    order_obj = Order.objects.get(id=pk)
    order_obj.payment = 'Paid'
    order_obj.payment_date = datetime.date.today()
    order_obj.save()
    return redirect('client:invoice_detail_view', order_obj.client.id)


@login_required(login_url='login')
def bank_transfer(request, pk):
    order_obj = Order.objects.get(id=pk)
    amount = order_obj.total
    if order_obj.company.name == 'Dasgupta Enterprise':
        qs = Bank.objects.filter(company__name='Dasgupta Enterprise')
        bank = qs[0]
        bank.amount = bank.amount + float(amount)
        bank.save()
        banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Dasgupta Enterprise Payment Credit, order: '+str(order_obj.order_id),
                                          type='CREDIT', balance=bank.amount)
        banktransaction.save()
    elif order_obj.company.name == 'Asian Chemicals':
        qs = Bank.objects.filter(company__name='Asian Chemicals')
        bank = qs[0]
        bank.amount = bank.amount + float(amount)
        bank.save()
        banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Asian Chemicals Payment Credit, order: '+str(order_obj.order_id),
                                          type='CREDIT', balance=bank.amount)
        banktransaction.save()
    order_obj.bank_transfer = True
    order_obj.save()
    return redirect('client:invoice_detail_view', order_obj.client.id)


@login_required(login_url='login')
def csr_pay(request, pk):
    order_obj = Order.objects.get(id=pk)
    order_obj.csr_status = True
    order_obj.save()
    order_id = order_obj.order_id
    amount = order_obj.CSR
    if order_obj.company.name == 'Dasgupta Enterprise':
        qs = Bank.objects.filter(company__name='Dasgupta Enterprise')
        bank = qs[0]
        bank.amount = bank.amount - float(amount)
        bank.save()
        banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Dasgupta Enterprise CSR Debit, order: '+str(order_id),
                                          type='DEBIT', balance=bank.amount)
        banktransaction.save()
    elif order_obj.company.name == 'Asian Chemicals':
        qs = Bank.objects.filter(company__name='Asian Chemicals')
        bank = qs[0]
        bank.amount = bank.amount - float(amount)
        bank.save()
        banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Asian Chemicals CSR Debit, order: '+str(order_id),
                                          type='DEBIT', balance=bank.amount)
        banktransaction.save()
    return redirect('client:client_detail_view', order_obj.client.id)


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
        'bill_raised': order_obj.bill_raised,
        'area': order_obj.area,
        'rate': order_obj.rate,
        'total': order_obj.total,
        'challan_text': order_obj.challan_text,
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
