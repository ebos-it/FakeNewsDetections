from django.contrib import admin
from .models.fndConfig import FNDConfig
from .models import fndInput, fndModelAttribute, fndModel, fndOutput

fndModels = [
    FNDConfig,
    fndOutput.FNDOutput,
    fndModel.FNDModel,
    fndModelAttribute.FNDModelAttribute,
    fndInput.FNDInput,
]
admin.site.register(fndModels)
