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
    service_1 = models.ForeignKey(Service, null=True, on_delete=models.CASCADE, related_name='service_1')
    price_1 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_1 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_1 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_2 = models.ForeignKey(Service, null=True, on_delete=models.CASCADE, related_name='service_2')
    price_2 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_2 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_2 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_3 = models.ForeignKey(Service, null=True, on_delete=models.CASCADE, related_name='service_3')
    price_3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_3 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_4 = models.ForeignKey(Service, null=True, on_delete=models.CASCADE, related_name='service_4')
    price_4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_4 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    upload_document = models.FileField(upload_to="document_uploaded/", blank=True)
    work_order_period = models.CharField(max_length=100, null=True)
    frequency = models.CharField(max_length=100, null=True)
    CSR = models.IntegerField(default=0)
    challan_text = models.TextField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


