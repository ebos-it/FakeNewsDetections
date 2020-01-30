from newsPortal.newsPortal.newstraining.datasource.inputDataGenerator import (
    InputDataGenerator,
)
from newsPortal.newsPortal.newstraining.algorithm.algorithmAdapter import AlgorithmAdapter


class FNDExecutor:
    def execute(self, fndContext):
        inputDataGenerator = InputDataGenerator(fndContext)
        trainingInput = inputDataGenerator.generateInput("training")

        algorithmAdapter = AlgorithmAdapter()
        algorithmAdapter.initiateDetection(trainingInput)