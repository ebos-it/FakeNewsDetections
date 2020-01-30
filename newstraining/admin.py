from django.contrib import admin
from .models import fndConfig, fndInput, fndModelAttribute, fndModel, fndOutput

fndModels = [
    fndConfig.FNDConfig,
    fndOutput.FNDOutput,
    fndModel.FNDModel,
    fndModelAttribute.FNDModelAttribute,
    fndInput.FNDInput,
]
admin.site.register(fndModels)
