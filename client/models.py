from django.db import models
from service.models import Service
from company.models import Company


class Client(models.Model):
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    address = models.TextField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Sub_Client(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    address = models.TextField(max_length=200, null=True)
    work_order_number = models.CharField(max_length=120, null=True, blank=True)
    upload_document = models.FileField(upload_to="document_uploaded/", blank=True)
    work_order_period = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)
    CSR = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


