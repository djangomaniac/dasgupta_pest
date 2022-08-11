from django.shortcuts import render, redirect
from .models import *
from service.models import *
from client.models import *
from .forms import *
from finance.models import *
from django.contrib.auth.decorators import login_required
import datetime


@login_required(login_url='login')
def DE_create_order(request, pk, mk):
    sub_client = Sub_Client.objects.get(id=mk)
    client = Client.objects.get(id=pk)
    company = Company.objects.get(name='Dasgupta Enterprises')
    form = OrderForm(initial={'company': company, 'client': client, 'sub_client': sub_client})
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            order = Order.objects.latest('pk')
            order.work_order_period = sub_client.work_order_period
            order.work_order_number = sub_client.work_order_number
            order.frequency = sub_client.frequency
            order.upload_document = sub_client.upload_document
            order.CSR = sub_client.CSR

            order.save()
            return redirect('client:client_view', order.client.id)

    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def AC_create_order(request, pk, mk):
    sub_client = Sub_Client.objects.get(id=mk)
    client = Client.objects.get(id=pk)
    company = Company.objects.get(name='Asian Chemicals')
    form = OrderForm(initial={'company': company, 'client': client, 'sub_client': sub_client})
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            order = Order.objects.latest('pk')
            order.work_order_period = sub_client.work_order_period
            work_order_number = sub_client.work_order_number
            order.frequency = sub_client.frequency
            order.upload_document = sub_client.upload_document
            order.CSR = sub_client.CSR

            order.save()
            return redirect('client:client_view', order.client.id)

    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def update_order(request, pk, mk):
    order_obj = Order.objects.get(id=pk)
    form = OrderForm(instance=order_obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=order_obj)
        if form.is_valid():
            form.save()
            if mk == 0:
                return redirect('client:client_view', order_obj.client.id)
            if mk == 1:
                if order_obj.company == 'Asian Chemicals':
                    return redirect('AC_superview')
                else:
                    return redirect('DE_superview')
            if mk == 3:
                return redirect('client:sub_client_page', order_obj.sub_client.id)

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
    return redirect(request.META['HTTP_REFERER'])

@login_required(login_url='login')
def bank_transfer(request, pk):
    order_obj = Order.objects.get(id=pk)
    amount = order_obj.total
    if order_obj.company.name == 'Dasgupta Enterprises':
        qs = Bank.objects.filter(company__name='Dasgupta Enterprises')
        bank = qs[0]
        bank.amount = bank.amount + float(amount)
        bank.save()
        banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Dasgupta Enterprises Payment Credit, order: '+str(order_obj.order_id),
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
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def csr_pay(request, pk):
    order_obj = Order.objects.get(id=pk)
    order_obj.csr_status = True
    order_obj.save()
    order_id = order_obj.order_id
    amount = order_obj.CSR
    if order_obj.company.name == 'Dasgupta Enterprises':
        qs = Cashbox.objects.filter(company__name='Dasgupta Enterprises')
        cashbox = qs[0]
        cashbox.amount = cashbox.amount - float(amount)
        cashbox.save()
        # banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Dasgupta Enterprises CSR Debit, order: '+str(order_id),
        #                                   type='DEBIT', balance=bank.amount)
        # banktransaction.save()
        cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), remark='Dasgupta Enterprises CSR Debit, order: '+str(order_id),
                                             type='DEBIT', balance=cashbox.amount)
        cashtransaction.save()
    elif order_obj.company.name == 'Asian Chemicals':
        qs = Cashbox.objects.filter(company__name='Asian Chemicals')
        cashbox = qs[0]
        cashbox.amount = cashbox.amount - float(amount)
        cashbox.save()
        # banktransaction = BankTransaction(company=bank.company, amount=float(amount), remark='Asian Chemicals CSR Debit, order: '+str(order_id),
        #                                   type='DEBIT', balance=bank.amount)
        # banktransaction.save()
        cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), remark='Asian Chemicals CSR Debit, order: '+str(order_id),
                                             type='DEBIT', balance=cashbox.amount)
        cashtransaction.save()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login')
def next_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    # form = OrderForm(instance=order_obj) 
    form = OrderForm(initial={
        'client': order_obj.client,
        'sub_client': order_obj.sub_client,
        'work_order_number': order_obj.work_order_number,
        'company': order_obj.company,
        'service_1': order_obj.service_1,
        'service_2': order_obj.service_2,
        'service_3': order_obj.service_3,
        'service_4': order_obj.service_4,
        'price_1': order_obj.price_1,
        'price_2': order_obj.price_2,
        'price_3': order_obj.price_3,
        'price_4': order_obj.price_4,
        'area_1': order_obj.area_1,
        'area_2': order_obj.area_2,
        'area_3': order_obj.area_3,
        'area_4': order_obj.area_4,
        'rate_1': order_obj.rate_1,
        'rate_2': order_obj.rate_2,
        'rate_3': order_obj.rate_3,
        'rate_4': order_obj.rate_4,
        'work_order_period': order_obj.work_order_period,
        'frequency': order_obj.frequency,
        'CSR': order_obj.CSR,
        'total': order_obj.total,
        'challan_text': order_obj.challan_text,
    })
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            order = Order.objects.latest('pk')
            order.upload_document = order_obj.upload_document
            order.save()
            return redirect('client:client_view', order.client.id)
    context = {
        'form': form,
    }
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
def view_order(request, pk):
    order_obj = Order.objects.get(id=pk)
    context = {
        'order_obj': order_obj,
    }
    return render(request, 'view_order.html', context)


@login_required(login_url='login')
def invoice(request, pk):
    order_obj = Order.objects.get(id=pk)
    context = {
        'order_obj': order_obj,
        'service_1': order_obj.service_1,
        'service_2': order_obj.service_2,
        'service_3': order_obj.service_3,
        'service_4': order_obj.service_4,
    }
    return render(request, 'invoice.html', context)
