import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

documents = [(list(movie_reviews.words(fileid)),category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
stop_words = set(stopwords.words("English"))
symbols = {',','.','/','!','@','#','$','%','^','&','*',
           '(',')','`','-','=','+','_','<','>','?',
           '"',':',';'}

all_words = []
for w in movie_reviews.words():
    if not w in stop_words and not w in symbols:
        all_words.append(w.lower())

all_words_freq = nltk.FreqDist(all_words)
print(all_words_freq.most_common(15))
print(all_words_freq["stupid"])

word_features = list(all_words_freq.keys())[:3000]

print('hello')

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

# print(find_features(movie_reviews.words('neg/cv000_29416.txt')))

featuresets = [(find_features(rev),category) for (rev,category) in documents]

training_set = featuresets[:1900]
testing_set = featuresets[100:]

# classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naiverbayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Ordinal Naive Bayes Algo accuracy:", nltk.classify.accuracy(classifier,testing_set)*100)
classifier.show_most_informative_features(15)

# save_classifier = open("naiverbayes.pickle","wb")
# pickle.dump(classifier,save_classifier)
# save_classifier.close()

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB classifier accuracy:", nltk.classify.accuracy(MNB_classifier,testing_set)*100)

# GaussianNB_classifier = SklearnClassifier(GaussianNB())
# GaussianNB_classifier.train(training_set)
# print("GaussianNB classifier accuracy:", nltk.classify.accuracy(GaussianNB_classifier,testing_set)*100)

BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("Bernoulli classifier accuracy:", nltk.classify.accuracy(BernoulliNB_classifier,testing_set)*100)

LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("Logistic classifier accuracy:", nltk.classify.accuracy(LogisticRegression_classifier,testing_set)*100)

SGD_classifier = SklearnClassifier(SGDClassifier())
SGD_classifier.train(training_set)
print("SGD classifier accuracy:", nltk.classify.accuracy(SGD_classifier,testing_set)*100)

SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("Bernoulli classifier accuracy:", nltk.classify.accuracy(SVC_classifier,testing_set)*100)

LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("Linear SVC classifier accuracy:", nltk.classify.accuracy(LinearSVC_classifier,testing_set)*100)

NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC classifier accuracy:", nltk.classify.accuracy(NuSVC_classifier,testing_set)*100)

voted_classifier = VoteClassifier(classifier,
                                  MNB_classifier,
                                  SVC_classifier,
                                  LinearSVC_classifier,
                                  NuSVC_classifier)
print("voted classifier accuracy percent:",
      (nltk.classify.accuracy(voted_classifier,testing_set)*100))

print("classificnation: ",
      voted_classifier.classify(testing_set[0][0]),"confidence: ", voted_classifier.confidence(testing_set[0][0]))
print("classificnation: ",
      voted_classifier.classify(testing_set[1][0]),"confidence: ", voted_classifier.confidence(testing_set[1][0]))
print("classificnation: ",
      voted_classifier.classify(testing_set[2][0]),"confidence: ", voted_classifier.confidence(testing_set[2][0]))
print("classificnation: ",
      voted_classifier.classify(testing_set[3][0]),"confidence: ", voted_classifier.confidence(testing_set[3][0]))
print("classificnation: ",
      voted_classifier.classify(testing_set[4][0]),"confidence: ", voted_classifier.confidence(testing_set[4][0]))