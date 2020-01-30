import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from newsPortal.newsPortal.newstraining.preprocessor.preprocessor import Preprocessor


class ContentPreprocessor(Preprocessor):
    def __init__(self):
        super().__init__()

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

    def preprocess(self, sentences):
        filtered_sentences = []
        for sentence in sentences[0]:
            sentence = self.removeSymbols(sentence)
            words = self.tokenizeSentence(sentence)
            filtered_words = self.removeStopWords(words)
            filtered_words = self.stemText(filtered_words)
            filtered_sentence = " ".join(word for word in filtered_words)
            filtered_sentences.append(filtered_sentence)
        return filtered_sentences
