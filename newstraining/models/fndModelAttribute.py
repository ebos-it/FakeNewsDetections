from django.db import models
from .fndModel import FNDModel


class FNDModelAttribute(models.Model):
    name = models.CharField(null=False, max_length=100)
    value = models.CharField(null=False, max_length=100)
    fndModel = models.ForeignKey(FNDModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}, Value: {self.value}"
