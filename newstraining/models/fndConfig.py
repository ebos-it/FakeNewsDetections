from django.db import models
from .fndModel import FNDModel


class FNDConfig(models.Model):
    name = models.CharField(null=False, max_length=100)
    fndType = models.CharField(null=False, max_length=100)
    fndModel = models.ForeignKey(FNDModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"Name: {self.name}, Type: {self.fndType}"

    # def setModel(self, fndModel):
    #     self.fndModel = fndModel
