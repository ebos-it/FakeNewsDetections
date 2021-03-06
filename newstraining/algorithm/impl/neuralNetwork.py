import matplotlib.pyplot as plt
from keras.layers import Flatten
from keras.layers.core import Dense
from keras.layers.embeddings import Embedding
from keras.models import Sequential
from newsPortal.newsPortal.newstraining.algorithm.abstractAlgorithm import AbstractAlgorithm
from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil
from newsPortal.newsPortal.newstraining.preprocessor.contentPreprocessor import ContentPreprocessor


class NeuralNetwork(AbstractAlgorithm):
    def __init__(self):
        super().__init__()

    def train(self,trainingInput,fndContext,embeddingMatrix=None):
        trainTestSplitRatio = super().getTrainingProperties("TRAIN_TEST_SPLIT_RATIO",fndContext)
        if not trainTestSplitRatio:
            log.debug(f'Unable to train, as trainTestSplitRatio is not provided')
            return
        X_train, X_test, Y_train, Y_test = TrainingUtil.splitTrainTest(
            trainingInput[0], trainingInput[1], trainTestSplitRatio
        )
        fndInputs = fndContext.fndConfig.fndModel.fndinput_set.filter(trainingIndicator="Y").all()
        preprocessor = None
        for fndInput in fndInputs:
            if fndInput.variableName == "content":
                preprocessor = ContentPreprocessor()
        X_train, X_test, embedding_matrix = preprocessor.getEmbeddingMatrix(trainingInput, fndContext)


        model = Sequential()
        embedding_layer = Embedding(
            preprocessor.getVocabularySize(),
            100,
            weights=[embedding_matrix],
            input_length=TrainingUtil.getMaxLength(),
            trainable=False,
        )
        model.add(embedding_layer)
        model.add(Flatten())
        model.add(Dense(1, activation="sigmoid"))

        model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["acc"])
        print(model.summary())

        history = model.fit(
            X_train, Y_train, batch_size=128, epochs=6, verbose=1, validation_split=0.2
        )

        score = model.evaluate(X_test, Y_test, verbose=1)
        log.debug("Test score using baseline NN:", score[0] * 100)
        log.debug("Test accuracy using baseline NN:", score[1] * 100)

        # plt.plot(history.history["acc"])
        # plt.plot(history.history["val_acc"])
        #
        # plt.title("model accuracy")
        # plt.ylabel("accuracy")
        # plt.xlabel("epoch")
        # plt.legend(["train", "test"], loc="upper left")
        # plt.show()
        #
        # plt.plot(history.history["loss"])
        # plt.plot(history.history["val_loss"])
        #
        # plt.title("model loss")
        # plt.xlabel("epoch")
        # plt.ylabel("loss")
        # plt.legend(["train", "test"], loc="upper left")
        # plt.show()
        log.debug("Training over")

    def predict(self,predictionInput,fndContext):
        print(f'nisniibnisk kk')
        pass
