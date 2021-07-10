from django.db import models
from company.models import Company
from service.models import Service
from client.models import Client
from django.db.models.signals import pre_save, post_save
from .utils import unique_order_id_generator


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Paid(NEFT)', 'Paid(NEFT)'),
        ('Paid(CHEQUE)', 'Paid(CHEQUE)'),
    )
    MONTH = (
        ('JANUARY', 'JANUARY'),
        ('FEBRUARY', 'FEBRUARY'),
        ('MARCH', 'MARCH'),
        ('APRIL', 'APRIL'),
        ('MAY', 'MAY'),
        ('JUNE', 'JUNE'),
        ('JULY', 'JULY'),
        ('AUGUST', 'AUGUST'),
        ('SEPTEMBER', 'SEPTEMBER'),
        ('OCTOBER', 'OCTOBER'),
        ('NOVEMBER', 'NOVEMBER'),
        ('DECEMBER', 'DECEMBER'),
    )
    order_id = models.CharField(max_length=120, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    sub_client = models.CharField(max_length=120, null=True, blank=True)
    service = models.ForeignKey(Service, null=True, on_delete=models.CASCADE)
    upload_document = models.FileField(upload_to="document_uploaded/", blank=True)
    work_order_period = models.CharField(max_length=100, null=True)
    invoice_for_month = models.CharField(max_length=100, default='JAN', choices=MONTH)
    frequency = models.CharField(max_length=100, null=True)
    area = models.IntegerField(default=0)
    rate = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    payment = models.CharField(max_length=100, default='Pending', choices=STATUS)
    TDS = models.IntegerField(default=0)
    CSR = models.IntegerField(default=0)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    remark = models.TextField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)
    instance.total = float(instance.area) * float(instance.rate)


pre_save.connect(pre_save_create_order_id, sender=Order)
