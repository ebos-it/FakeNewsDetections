from newsPortal.newsPortal.newstraining.preprocessor.contentPreprocessor import ContentPreprocessor
from newsPortal.newsPortal.newstraining.algorithm.impl.neuralNetwork import NeuralNetwork


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

    def initiateDetection(self, trainingInput):
        preprocessor = ContentPreprocessor()
        preprocessedTrainingInput = preprocessor.preprocess(trainingInput)
        fndAlgo = self.getFNDAlgo()
        fndAlgo.train()

    # get the configuration for trainingAlgo to use
    def getFNDAlgo(self):
        return NeuralNetwork()
