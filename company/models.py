from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
