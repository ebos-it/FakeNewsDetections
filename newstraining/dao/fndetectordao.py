from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.models.fndConfig import FNDConfig
from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil


class FNDetectorDao:

    configSection = "trainingConfigurations"
    configKey = "trainingName"

    def __init__(self):
        self.trainingName = ""
        self.validate()

    def validate(self):
        self.trainingName = TrainingUtil.getConfigAttribute(
            configSection=self.configSection, configKey=self.configKey
        )
        if self.trainingName:
            log.error(
                f"Configuration loaded - section: {self.configSection}"
                f" and key: {self.configKey}"
            )
        else:
            log.error(
                f"Invalid configuration provided - section: {self.configSection}"
                f" and key: {self.configKey}"
            )
            raise KeyError

    def getModelConfig(self):
        if not self.trainingName:
            log.debug(f"No training name")
            return

        return FNDConfig.objects.filter(name=self.trainingName)

    def getConfiguration(self):
        modelConfig = self.getModelConfig()
        if not modelConfig:
            log.debug(f"No model configuration found")
            return

        return modelConfig
