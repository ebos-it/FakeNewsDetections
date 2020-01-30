from newsPortal.newsPortal.newsPortal.settings import configParser


class TrainingUtil:
    @staticmethod
    def getConfigAttribute(configSection, configKey):
        if configParser.has_section(configSection) and configParser.has_option(
            configKey
        ):
            return configParser.get(configSection, configKey)
        return None
