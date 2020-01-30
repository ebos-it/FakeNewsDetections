from newsPortal.newsPortal.newstraining.preprocessor.contentPreprocessor import ContentPreprocessor
from newsPortal.newsPortal.newstraining.algorithm.impl.neuralNetwork import NeuralNetwork
from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil


class AlgorithmAdapter:
    class __AlgorithmAdapter:
        def __init__(self):
            pass

    instance = None

    def __init__(self):
        if not AlgorithmAdapter.instance:
            AlgorithmAdapter.instance = (
                AlgorithmAdapter.__AlgorithmAdapter()
            )

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def initiateDetection(self, trainingInput, fndContext):
        fndInputs = fndContext.fndConfig.fndModel.fndinput_set.filter(trainingIndicator="Y").all()
        preprocessor = None
        for fndInput in fndInputs:
            if fndInput.variableName == "content":
                preprocessor = ContentPreprocessor()
        preprocessedTrainingInput = preprocessor.preprocess(trainingInput, fndContext)
        fndAlgo = self.getFNDAlgo()
        if not fndAlgo:
            log.debug("training algo not configured. Cannot train further")
            return
        fndAlgo.train(preprocessedTrainingInput,fndContext)

    def getFNDAlgo(self):
        return TrainingUtil.getAlgo()
