import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import seaborn as sns
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.core import Activation, Dropout, Dense
from keras.layers import Flatten
import matplotlib.pyplot as plt
from keras.layers import GlobalMaxPooling1D, Conv1D, LSTM

imdb_dataset = pd.read_csv("D:\\ml and dl\\keras\\nlp_3.7\\dataset\\imdb-dataset\\IMDB Dataset.csv")

print(imdb_dataset.columns)
print(imdb_dataset.shape)

imdb_dataset.isnull().values.any()
print(imdb_dataset.head())
print(imdb_dataset.shape)

sns.countplot(x='sentiment',data=imdb_dataset)

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(sen):
    return TAG_RE.sub('',sen)

def preprocess_text(sen):
    sentence = remove_tags(sen)
    sentence = re.sub('[^a-zA-Z]',' ',sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+",' ',sentence)
    sentence = re.sub(r'\s+',' ',sentence)
    return sentence

X = []
sentences = list(imdb_dataset['review'])
for sen in sentences:
    X.append(preprocess_text(sen))

print(X[3])

y = imdb_dataset['sentiment']
y = np.array(list(map(lambda x: 1 if x == "positive" else 0, y)))

X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.20,random_state=42)

tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)

vocab_size = len(tokenizer.word_index)+1
maxlen = 100
X_train = pad_sequences(X_train,padding="post",maxlen=maxlen)
X_test = pad_sequences(X_test,padding="post",maxlen=maxlen)

embeddings_dictionary = dict()
glove_file = open("D:\\ml and dl\\keras\\nlp_3.7\\glove.6B\\glove.6B.100d.txt",encoding="utf8")
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

print('hello')

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

instance = X[57]
print(instance)

instance = tokenizer.texts_to_sequences(instance)

flat_list = []
for sublist in instance:
    for item in sublist:
        flat_list.append(item)

flat_list = [flat_list]
instance = pad_sequences(flat_list,padding="post",maxlen=maxlen)
model.predict(instance)