from newsPortal.newsPortal.newstraining.datasource.inputDataGenerator import (
    InputDataGenerator,
)
from newsPortal.newsPortal.newstraining.algorithm.algorithmAdapter import AlgorithmAdapter
from newsPortal.newsPortal.newsPortal.settings import log


class FNDExecutor:
    def execute(self, fndContext):
        inputDataGenerator = InputDataGenerator(fndContext)
        trainingInput = inputDataGenerator.generateInput("training")

        algorithmAdapter = AlgorithmAdapter()
        algorithmAdapter.initiateDetection(trainingInput)