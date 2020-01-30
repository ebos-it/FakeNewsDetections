import matplotlib.pyplot as plt
from keras.layers import Flatten
from keras.layers.core import Dense
from keras.layers.embeddings import Embedding
from keras.models import Sequential
from newsPortal.newsPortal.newstraining.algorithm.abstractAlgorithm import AbstractAlgorithm


class NeuralNetwork(AbstractAlgorithm):
    def __init__(self):
        super().__init__()

    def train(self):
        X_train, X_test, Y_train, Y_test, embedding_matrix = super().train()
        model = Sequential()
        embedding_layer = Embedding(
            vocab_size,
            100,
            weights=[embedding_matrix],
            input_length=maxlen,
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
        print("Test score using baseline NN:", score[0] * 100)
        print("Test accuracy using baseline NN:", score[1] * 100)

        plt.plot(history.history["acc"])
        plt.plot(history.history["val_acc"])

        plt.title("model accuracy")
        plt.ylabel("accuracy")
        plt.xlabel("epoch")
        plt.legend(["train", "test"], loc="upper left")
        plt.show()

        plt.plot(history.history["loss"])
        plt.plot(history.history["val_loss"])

        plt.title("model loss")
        plt.xlabel("epoch")
        plt.ylabel("loss")
        plt.legend(["train", "test"], loc="upper left")
        plt.show()

    def predict(self):
        print(f'nisniibni')
        pass
