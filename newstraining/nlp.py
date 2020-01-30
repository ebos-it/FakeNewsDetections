from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
from nltk.corpus import gutenberg, wordnet

nltk.download("state_union")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")
nltk.download("wordnet")
nltk.download("movie_reviews")

example_sentences = (
    "Hello Mr. Girija, how are you doing? "
    "The weathered is great and pythonly is awesome. "
    "The skyed is blue and you should not be eating "
    "cardboard."
)

print(sent_tokenize(example_sentences))
print(word_tokenize(example_sentences))

stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentences)
filtered_sentences = [w for w in words if not w in stop_words]

print(filtered_sentences)

new_text = (
    "It is very important to be pythonly while you are "
    "pythoninh with python. All pythoners have pythoned "
    "before pythoning has even started happening."
)

ps = PorterStemmer()
for w in filtered_sentences:
    print(ps.stem(w))

words = word_tokenize(new_text)
for w in words:
    print(ps.stem(w))

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(new_text)


def process_content():
    try:
        for i in tokenized:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)

            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?} """
            chinkgram = r"""Chunk: {<.*>+}
                                    }<VB.?|IN|DT>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chinkParser = nltk.RegexpParser(chinkgram)
            chunked = chunkParser.parse(tagged)
            chinked = chinkParser.parse(tagged)
            print(chunked)
            print(chinked)
            chunked.draw()
            chinked.draw()
    except Exception as e:
        print(str(e))


line = (
    "Hello Mr. President Obama, are you going to your house in America? "
    "The weathered is great and python is awesome. "
    "The sky is blue and you should not be eating "
    "cardboard. White house is burning. "
    "There is an earthquake happened near Russia."
    "Robert managed escape from jail."
)


def getNamedEnt(line):
    line_tokenized = custom_sent_tokenizer.tokenize(line)
    ps = PorterStemmer()
    for line in line_tokenized:
        words = word_tokenize(line)
        words = [w for w in words if not w in stop_words]
        stemmed_words = []
        # for word in words:
        #     stemmed_words.append(ps.stem(word))
        tagged = nltk.pos_tag(words)
        namedEnt = nltk.ne_chunk(tagged, binary=True)
        namedEnt.draw()
        print("hello")


lemmatizer = WordNetLemmatizer()
# print(lemmatizer.lemmatize("better"))
# print(lemmatizer.lemmatize("better",pos="a"))
# print(lemmatizer.lemmatize("best",pos="a"))
# print(lemmatizer.lemmatize("surprising",pos="a"))
# print(lemmatizer.lemmatize("surprising",pos="v"))
# print(lemmatizer.lemmatize("surprising",pos="n"))
#
# sample_text = gutenberg.raw('bible-kjv.txt')
# sample_text_tokens = sent_tokenize(sample_text)
# print(sample_text_tokens)
#
# syns = wordnet.synsets("program")
# print(syns)
# print(syns[0])
# print(syns[0].lemmas()[0].name())
# print(syns[0].definition())
# print(syns[0].examples())
#
# synonyms = []
# antonyms = []
#
# for syn in wordnet.synsets("good"):
#     for l in syn.lemmas():
#         synonyms.append(l.name())
#         if l.antonyms():
#             antonyms.append(l.antonyms()[0].name())
#
# print(set(synonyms))
# print(set(antonyms))
#
# word1 = wordnet.synset("ship.n.01")
# word2 = wordnet.synset("boat.n.01")
#
# print(word1.wup_similarity(word2))
#
# word1 = wordnet.synset("ship.n.01")
# word2 = wordnet.synset("car.n.01")
#
# print(word1.wup_similarity(word2))
#
# word1 = wordnet.synset("ship.n.01")
# word2 = wordnet.synset("love.n.01")
#
# print(word1.wup_similarity(word2))
#
# word1 = wordnet.synset("ship.n.01")
# word2 = wordnet.synset("rain.n.01")
#
# print(word1.wup_similarity(word2))

# process_content()
# getNamedEnt(line)


class NewsTrainerUtil:
    def __init__(self):
        pass

    def cleanRecords(self):
        self.removeStopWords()
        self.changeCase()

    def removeStopWords(self):
        pass

    def changeCase(self):
        pass

    def tokenizeSentence(self):
        pass
