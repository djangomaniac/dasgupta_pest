from django.db import models
from company.models import Company
from service.models import Service
from client.models import *
from django.db.models.signals import pre_save, post_save
from .utils import unique_order_id_generator
import datetime


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
    )
    CSR_value = (
        (True, 'Paid'),
        (False, 'Not Paid'),
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
    COLOUR_CODE = (
        ('#ffffff', 'None'),
        ('#ffc7c7', 'RED'),
        ('#99ffcc', 'GREEN'),
        ('#ffff99', 'YELLOW'),
    )
    order_id = models.CharField(max_length=120, null=True, blank=True)
    uid = models.CharField(max_length=4, null=True, blank=True)
    client = models.ForeignKey(Client, null=True, on_delete=models.CASCADE)
    colour_code = models.CharField(max_length=20, default='None', choices=COLOUR_CODE)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    sub_client = models.ForeignKey(Sub_Client, null=True, on_delete=models.CASCADE)
    work_order_number = models.CharField(max_length=120, null=True, blank=True)
    service_1 = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE, related_name='service_1')
    price_1 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_1 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_1 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_2 = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE, related_name='service_2')
    price_2 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_2 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_2 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_3 = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE, related_name='service_3')
    price_3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_3 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_3 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    service_4 = models.ForeignKey(Service, null=True, blank=True, on_delete=models.CASCADE, related_name='service_4')
    price_4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    area_4 = models.DecimalField(default=1.00, max_digits=10, decimal_places=2)
    rate_4 = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    upload_document = models.FileField(upload_to="document_uploaded/", blank=True)
    work_order_period = models.CharField(max_length=100, null=True, blank=True)
    invoice_for_month = models.CharField(max_length=100, default='JAN', choices=MONTH)
    date = models.CharField(max_length=20, default=datetime.datetime.now().strftime('%d/%m/%y'), null=True)
    frequency = models.CharField(max_length=100, null=True, blank=True)
    # bill_raised = models.CharField(max_length=100, null=True)
    payment = models.CharField(max_length=100, default='Pending', choices=STATUS)
    payment_details = models.CharField(max_length=100, null=True, blank=True)
    payment_date = models.DateField(blank=True, null=True)
    bank_transfer = models.BooleanField(default=False)
    CSR = models.IntegerField(default=0)
    csr_status = models.BooleanField(default=False, choices=CSR_value)
    total = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    challan_text = models.TextField(max_length=200, null=True, blank=True)
    remark = models.TextField(max_length=200, null=True, blank=True)
    serial_no = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    dt = datetime.datetime.now()
    order = Order.objects.all().last()
    if order:
        print(order.serial_no)
        serial_no = order.serial_no + 1
    else:
        serial_no = 1
    if not instance.order_id:

        # instance.uid = unique_order_id_generator(instance)
        if instance.company.name == "Dasgupta Enterprises":
            instance.order_id = "DE/" + str(serial_no) + "/" + dt.strftime("%b") + "/" + dt.strftime("%Y")  # for order_id formatting
        else:
            instance.order_id = "AC/" + str(serial_no) + "/" + dt.strftime("%b") + "/" + dt.strftime("%Y")  # for order_id formatting
            # instance.order_id = unique_order_id_generator(instance)
    if not instance.serial_no:
        instance.serial_no = serial_no

    try:
        instance.rate_1 = float(instance.price_1) / float(instance.area_1)
        instance.rate_2 = float(instance.price_2) / float(instance.area_2)
        instance.rate_3 = float(instance.price_3) / float(instance.area_3)
        instance.rate_4 = float(instance.price_4) / float(instance.area_4)
    except ZeroDivisionError:  # ignore division by zero
        if instance.area_1 == 0:
            instance.rate_1 = 0
        if instance.area_2 == 0:
            instance.rate_2 = 0
        if instance.area_3 == 0:
            instance.rate_3 = 0
        if instance.area_4 == 0:
            instance.rate_4 = 0

        # print("division by zero")

    instance.total = float(instance.price_1) + float(instance.price_2) + float(instance.price_3) + float(instance.price_4)


pre_save.connect(pre_save_create_order_id, sender=Order)

# post_save.connect(post_save_uid_serialize, sender=Order)
