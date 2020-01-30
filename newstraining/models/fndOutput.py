from django.db import models
from .fndModel import FNDModel


class FNDOutput(models.Model):
    variableName = models.CharField(null=False, max_length=100)
    variableSymbol = models.CharField(null=False, max_length=100)
    fndModel = models.ForeignKey(FNDModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.variableName}, Type: {self.variableSymbol}"
