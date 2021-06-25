from django.db import models
from company.models import Company


class Cashbox(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True, null=True)


class Bank(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True, null=True)


class CashboxTransaction(models.Model):
    TYPE_CHOICES = (
        ("DEBIT", "DR"),
        ("CREDIT", "CR"),
    )
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    balance = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)


class BankTransaction(models.Model):
    TYPE_CHOICES = (
        ("DEBIT", "DR"),
        ("CREDIT", "CR"),
    )
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    amount = models.FloatField()
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    balance = models.FloatField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

