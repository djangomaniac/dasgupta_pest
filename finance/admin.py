from django.contrib import admin
from . import models


admin.site.register(models.Cashbox)
admin.site.register(models.Bank)
admin.site.register(models.CashboxTransaction)
admin.site.register(models.BankTransaction)
