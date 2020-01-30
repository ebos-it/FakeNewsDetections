import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from newsPortal.newsPortal.newstraining.preprocessor.preprocessor import Preprocessor
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np

from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil


class ContentPreprocessor(Preprocessor):
    class __ContentPreprocessor:
        tokenizer = None

        def __init__(self):
            pass

    instance = None

    def __init__(self):
        super().__init__()
        if not ContentPreprocessor.instance:
            ContentPreprocessor.instance = (
                ContentPreprocessor.__ContentPreprocessor()
            )

    def setTokenizer(self, tokenizer):
        self.tokenizer = tokenizer

    def getTokenizer(self):
        return self.tokenizer

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def removeSymbols(self, sen):
        sentence = re.sub("[^a-zA-Z0-9]", " ", sen)
        sentence = re.sub(r"\s+[a-zA-Z]\s+", " ", sentence)
        sentence = re.sub(r"\s+", " ", sentence)
        return sentence

    def stemText(self, words):
        # ps = PorterStemmer()
        lemmatizer = WordNetLemmatizer()
        # filtered_words = [ps.stem(w.lower()) for w in words if not w in stop_words]
        filtered_words = [lemmatizer.lemmatize(w.lower()) for w in words]
        return filtered_words

    def removeStopWords(self, words):
        stop_words = set(stopwords.words("english"))
        filtered_words = []
        for w in words:
            if not w in stop_words:
                filtered_words.append(w)
        return filtered_words

    def tokenizeSentence(self, sentence):
        return word_tokenize(sentence)

    def createTokenizer(self, X_train):
        print('hello')
        tokenizer = Tokenizer(num_words=5000)
        tokenizer.fit_on_texts(X_train)
        self.setTokenizer(tokenizer)
        return tokenizer

    def createWordEmbeddingDictionary(self):
        embeddings_dictionary = dict()
        glove_file = open(TrainingUtil.getWordEmbeddingsFileName(), encoding="utf8")
        for line in glove_file:
            records = line.split()
            word = records[0]
            vector_dimensions = np.asarray(records[1:], dtype="float32")
            embeddings_dictionary[word] = vector_dimensions
        glove_file.close()
        return embeddings_dictionary

    def getVocabularySize(self):
        return len(self.getTokenizer().word_index) + 1

    def createEmbeddingMatrix(self, embeddings_dictionary, tokenizer):
        embedding_matrix = np.zeros((self.getVocabularySize(), 100))
        for word, index in tokenizer.word_index.items():
            embedding_vector = embeddings_dictionary.get(word)
            if embedding_vector is not None:
                embedding_matrix[index] = embedding_vector

        return embedding_matrix

    def getEmbeddingMatrix(self, X_train, X_test):
        tokenizer = self.createTokenizer(X_train)

        maxlen = TrainingUtil.getMaxLength()
        X_train = pad_sequences(X_train, padding="post", maxlen=maxlen)
        X_test = pad_sequences(X_test, padding="post", maxlen=maxlen)

        embedding_dictionary = self.createWordEmbeddingDictionary()
        embedding_matrix = self.createEmbeddingMatrix(embeddings_dictionary=embedding_dictionary, tokenizer=tokenizer)

        return X_train, X_test, embedding_matrix

    def preprocess(self, sentences, fndContext):
        print(f'preprocessing start')
        filtered_sentences = []
        for sentence, label in sentences:
            sentence = self.removeSymbols(sentence)
            words = self.tokenizeSentence(sentence)
            filtered_words = self.removeStopWords(words)
            filtered_words = self.stemText(filtered_words)
            filtered_sentence = " ".join(word for word in filtered_words)
            filtered_sentences.append([filtered_sentence, label])
