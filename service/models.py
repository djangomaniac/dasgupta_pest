from django.db import models
from company.models import Company


class Service(models.Model):
    name = models.CharField(max_length=100, null=True)
    company = models.ForeignKey(Company, null=True, on_delete=models.CASCADE)
    description = models.TextField(max_length=200, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
