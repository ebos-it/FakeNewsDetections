from newsPortal.newsPortal.newstraining.DataAccessModule import DataAccess
from newsPortal.newsPortal.newstraining.preprocessor import datapreprocessor
from .trainingUtil import TrainingUtil
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import os

class TrainingAlgorithm():
    gloveDirectory = "D:\\ml and dl\\keras\\dataset\\glove\\glove.6B"
    gloveFilename = "glove.6B.100d.txt"
    absoluteGloveFilePath = os.path.join(gloveDirectory, gloveFilename)

    def __init__(self):
        pass

    def train(self):
        sentences, labels = DataAccess.DataAccess.getDataset()
        filtered_sentences = datapreprocessor.DataPreprocessor.preprocess_text(sentences)

        X_train, X_test, Y_train, Y_test = TrainingUtil.splitTrainTest(filtered_sentences, labels, splitRatio=0.05)

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
            vector_dimensions = np.asarray(records[1:], dtype='float32')
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