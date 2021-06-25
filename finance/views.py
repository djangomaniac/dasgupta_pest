from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def DE_finance_page(request):
    qs = Cashbox.objects.filter(company__name='Dasgupta Enterprise')
    cashbox = qs[0]
    qs = Bank.objects.filter(company__name='Dasgupta Enterprise')
    bank = qs[0]

    if request.method == 'POST':
        amount = request.POST.get('amount', '')
        section = request.POST.get('hidden_type', '')
        typeof = request.POST.get('action', '')
        if section == 'cash':
            if typeof == 'DEBIT':
                cashbox.amount = cashbox.amount - float(amount)
                cashbox.save()
                cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), type=typeof, balance=cashbox.amount)
                cashtransaction.save()
            elif typeof == 'CREDIT':
                cashbox.amount = cashbox.amount + float(amount)
                cashbox.save()
                cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), type=typeof, balance=cashbox.amount)
                cashtransaction.save()
        elif section == 'bank':
            if typeof == 'DEBIT':
                bank.amount = bank.amount - float(amount)
                bank.save()
                banktransaction = BankTransaction(company=bank.company, amount=float(amount), type=typeof, balance=bank.amount)
                banktransaction.save()
            elif typeof == 'CREDIT':
                bank.amount = bank.amount + float(amount)
                bank.save()
                banktransaction = BankTransaction(company=bank.company, amount=float(amount), type=typeof, balance=bank.amount)
                banktransaction.save()
        return redirect("/finance/de_finance")

    cashtransactions = CashboxTransaction.objects.filter(company__name='Dasgupta Enterprise')
    banktransactions = BankTransaction.objects.filter(company__name='Dasgupta Enterprise')
    context = {
        'title': "Dasgupta Enterprise",
        'cashbox': cashbox,
        'bank': bank,
        'cashtransactions': cashtransactions,
        'banktransactions': banktransactions,
    }
    return render(request, 'finance.html', context)


@login_required(login_url='login')
def AC_finance_page(request):
    qs = Cashbox.objects.filter(company__name='Asian Chemicals')
    cashbox = qs[0]
    qs = Bank.objects.filter(company__name='Asian Chemicals')
    bank = qs[0]

    if request.method == 'POST':
        amount = request.POST.get('amount', '')
        section = request.POST.get('hidden_type', '')
        typeof = request.POST.get('action', '')
        if section == 'cash':
            if typeof == 'DEBIT':
                cashbox.amount = cashbox.amount - float(amount)
                cashbox.save()
                cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), type=typeof, balance=cashbox.amount)
                cashtransaction.save()
            elif typeof == 'CREDIT':
                cashbox.amount = cashbox.amount + float(amount)
                cashbox.save()
                cashtransaction = CashboxTransaction(company=cashbox.company, amount=float(amount), type=typeof, balance=cashbox.amount)
                cashtransaction.save()
        elif section == 'bank':
            if typeof == 'DEBIT':
                bank.amount = bank.amount - float(amount)
                bank.save()
                banktransaction = BankTransaction(company=bank.company, amount=float(amount), type=typeof, balance=bank.amount)
                banktransaction.save()
            elif typeof == 'CREDIT':
                bank.amount = bank.amount + float(amount)
                bank.save()
                banktransaction = BankTransaction(company=bank.company, amount=float(amount), type=typeof, balance=bank.amount)
                banktransaction.save()
        return redirect("/finance/ac_finance")

    cashtransactions = CashboxTransaction.objects.filter(company__name='Asian Chemicals')
    banktransactions = BankTransaction.objects.filter(company__name='Asian Chemicals')
    context = {
        'title': "Asian Chemicals",
        'cashbox': cashbox,
        'bank': bank,
        'cashtransactions': cashtransactions,
        'banktransactions': banktransactions,
    }
    return render(request, 'finance.html', context)
