import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.core import Dense
from keras.layers import Flatten
import matplotlib.pyplot as plt
from keras.layers import GlobalMaxPooling1D, Conv1D, LSTM
from nltk.stem import WordNetLemmatizer
import os

dataFilepath = "D:\\ml and dl\\keras\\dataset\\csv files"
dataFilename = "dataset_2.csv"
gloveDirectory = "D:\\ml and dl\\keras\\dataset\\glove\\glove.6B"
gloveFilename = "glove.6B.100d.txt"

absoluteDataFilePath = os.path.join(dataFilepath,dataFilename)
absoluteGloveFilePath = os.path.join(gloveDirectory,gloveFilename)

def printDatasetDetails(dataset):
    print(f'Column Names: {dataset.columns}')
    print(f'\n\nDataset Shape: {dataset.shape}')
    print(f'\n\nFirst 5 rows: {dataset.head()}')

def removeSymbols(sen):
    sentence = re.sub('[^a-zA-Z0-9]', ' ', sen)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence

def stemText(words):
    # ps = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    # filtered_words = [ps.stem(w.lower()) for w in words if not w in stop_words]
    filtered_words = [lemmatizer.lemmatize(w.lower()) for w in words]
    return filtered_words

def removeStopWords(words):
    stop_words = set(stopwords.words("english"))
    filtered_words = []
    for w in words:
        if not w in stop_words:
            filtered_words.append(w)
    return filtered_words

def tokenizeSentence(sentence):
    return word_tokenize(sentence)

def preprocess_text(sentences):
    filtered_sentences = []
    for sentence in sentences[0]:
        sentence = removeSymbols(sentence)
        words = tokenizeSentence(sentence)
        filtered_words = removeStopWords(words)
        filtered_words = stemText(filtered_words)
        filtered_sentence = ' '.join(word for word in filtered_words)
        filtered_sentences.append(filtered_sentence)
    return filtered_sentences

def getData(dataset,columnNames):
    textData = []
    for columnName in columnNames:
        textData.append(dataset[columnName])
    return textData

def getLabels(dataset, columnName):
    labels = news_articles[columnName]
    labels = np.array(list(map(lambda x: 1 if x == False else 0, labels)))
    return labels

def readFile(absoluteFilePath):
    news_articles = pd.read_csv(absoluteFilePath)
    return news_articles

def splitTrainTest(dataset,labels,splitRatio):
    X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=splitRatio, random_state=42)
    return X_train,X_test,Y_train,Y_test

news_articles = readFile(absoluteDataFilePath)
sentences = getData(news_articles,['content'])
filtered_sentences = preprocess_text(sentences)
labels = getLabels(news_articles,columnName="fact_check")

X_train,X_test,Y_train,Y_test = splitTrainTest(filtered_sentences,labels,splitRatio=0.05)

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

vocab_size = len(tokenizer.word_index)+1
maxlen = 600
X_train = pad_sequences(X_train,padding="post",maxlen=maxlen)
X_test = pad_sequences(X_test,padding="post",maxlen=maxlen)

embeddings_dictionary = dict()
glove_file = open(absoluteGloveFilePath,encoding="utf8")
for line in glove_file:
    records = line.split()
    word = records[0]
    vector_dimensions = np.asarray(records[1:],dtype='float32')
    embeddings_dictionary[word] = vector_dimensions
glove_file.close()

embedding_matrix = np.zeros((vocab_size,100))
for word, index in tokenizer.word_index.items():
    embedding_vector = embeddings_dictionary.get(word)
    if embedding_vector is not None:
        embedding_matrix[index] = embedding_vector

model = Sequential()
embedding_layer = Embedding(vocab_size,100,weights=[embedding_matrix],input_length=maxlen,trainable=False)
model.add(embedding_layer)
model.add(Flatten())
model.add(Dense(1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
print(model.summary())

history = model.fit(X_train, Y_train, batch_size=128, epochs=6, verbose=1, validation_split=0.2)
score = model.evaluate(X_test,Y_test,verbose=1)
print("Test score using baseline NN:", score[0]*100)
print("Test accuracy using baseline NN:", score[1]*100)

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','test'],loc='upper left')
plt.show()

model = Sequential()
model.add(embedding_layer)
model.add(Conv1D(128,5,activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])

print(model.summary())

history = model.fit(X_train,Y_train,batch_size=128,epochs=6,verbose=1,validation_split=0.2)
score = model.evaluate(X_test, Y_test,verbose=1)

print("Test score using CNV:", score[0]*100)
print("Test accuracy using CNV:", score[1]*100)

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','test'],loc='upper left')
plt.show()

model = Sequential()
model.add(embedding_layer)
model.add(LSTM(128))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['acc'])
print(model.summary())

history = model.fit(X_train,Y_train,batch_size=128,epochs=6,verbose=1,validation_split=0.2)
score = model.evaluate(X_test,Y_test,verbose=1)

print("Test score using LSTM:", score[0]*100)
print("Test accuracy using LSTM:", score[1]*100)

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])

plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train','test'],loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])

plt.title('model loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['train','test'],loc='upper left')
plt.show()

instance = filtered_sentences[57]
print(instance)

instance = tokenizer.texts_to_sequences(instance)

flat_list = []
for sublist in instance:
    for item in sublist:
        flat_list.append(item)

flat_list = [flat_list]
instance = pad_sequences(flat_list,padding="post",maxlen=maxlen)
print(model.predict(instance))