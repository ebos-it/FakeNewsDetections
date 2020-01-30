from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil


class AbstractAlgorithm:
    def __init__(self):
        pass

    def train(self,trainingInput,fndContext,embeddingMatrix=None):
        trainTestSplitRatio = self.getTrainingProperties("TRAIN_TEST_SPLIT_RATIO", fndContext)
        if not trainTestSplitRatio:
            log.debug(f'Unable to train, as trainTestSplitRatio is not provided')
            return
        X_train, X_test, Y_train, Y_test = TrainingUtil.splitTrainTest(
            trainingInput[0], trainingInput[1], trainTestSplitRatio
        )

    def predict(self,predictionInput,fndContext):
        pass

    def getTrainTestSplitRatio(self):
        self.getTrainTestSplitRatio()

    def getTrainingProperties(self,propertyName,fndContext):
        fndModelAttribute = fndContext.fndConfig.fndModel.fndmodelattribute_set.filter(name=propertyName)
        return fndModelAttribute
