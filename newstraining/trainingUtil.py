from newsPortal.newsPortal.newsPortal.settings import configParser
from sklearn.model_selection import train_test_split


class TrainingUtil:
    @staticmethod
    def getConfigAttribute(configSection, configKey):
        if configParser.has_section(configSection) and configParser.has_option(
            configKey
        ):
            return configParser.get(configSection, configKey)
        return None

    @staticmethod
    def splitTrainTest(dataset, labels, splitRatio):
        X_train, X_test, Y_train, Y_test = train_test_split(
            dataset, labels, test_size=splitRatio, random_state=42
        )
        return X_train, X_test, Y_train, Y_test

    @staticmethod
    def getAlgo():
        return TrainingUtil.getConfigAttribute("trainingConfigurations","trainingAlgo")

    @staticmethod
    def getWordEmbeddingsFileName():
        embeddingLocation = TrainingUtil.getConfigAttribute("wordembeddingConfigurations","embeddingDirectory")
        embeddingFileName = TrainingUtil.getConfigAttribute("wordembeddingConfigurations", "embeddingFileName")
        return embeddingLocation + embeddingFileName

    @staticmethod
    def getMaxLength():
        return TrainingUtil.getConfigAttribute("wordembeddingConfigurations", "maxLengthForPadding")