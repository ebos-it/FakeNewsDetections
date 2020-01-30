import configparser
import os

import numpy as np
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer

from newsPortal.newsPortal.newstraining.preprocessor import contentPreprocessor
from newsPortal.newsPortal.newstraining.algorithm.impl.trainingUtil import TrainingUtil

cParser = configparser.ConfigParser()
cParser.read("..\\..\\configurations.ini")


class TrainingAlgorithm:
    gloveDirectory = "D:\\ml and dl\\keras\\dataset\\glove\\glove.6B"
    gloveFilename = "glove.6B.100d.txt"
    absoluteGloveFilePath = os.path.join(gloveDirectory, gloveFilename)

    def __init__(self):
        pass

    def train(self):
        sentences, labels = DataAccess.getDataset()
        filtered_sentences = contentPreprocessor.DataPreprocessor.preprocess_text(
            sentences
        )

        X_train, X_test, Y_train, Y_test = TrainingUtil.splitTrainTest(
            filtered_sentences, labels, splitRatio=0.05
        )

        tokenizer = Tokenizer(num_words=5000)
        tokenizer.fit_on_texts(X_train)

        X_train = tokenizer.texts_to_sequences(X_train)
        X_test = tokenizer.texts_to_sequences(X_test)

        vocab_size = len(tokenizer.word_index) + 1
        maxlen = 600
        X_train = pad_sequences(X_train, padding="post", maxlen=maxlen)
        X_test = pad_sequences(X_test, padding="post", maxlen=maxlen)

        embeddings_dictionary = dict()
        glove_file = open(self.absoluteGloveFilePath, encoding="utf8")
        for line in glove_file:
            records = line.split()
            word = records[0]
            vector_dimensions = np.asarray(records[1:], dtype="float32")
            embeddings_dictionary[word] = vector_dimensions
        glove_file.close()

        embedding_matrix = np.zeros((vocab_size, 100))
        for word, index in tokenizer.word_index.items():
            embedding_vector = embeddings_dictionary.get(word)
            if embedding_vector is not None:
                embedding_matrix[index] = embedding_vector

        return X_train, X_test, Y_train, Y_test, embedding_matrix

    def predict(self):
        pass
