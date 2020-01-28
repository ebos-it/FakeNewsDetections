import os
import pandas as pd
import numpy as np

class DataAccess():

    dataFilepath = "D:\\ml and dl\\keras\\dataset\\csv files"
    dataFilename = "dataset_2.csv"
    absoluteDataFilePath = os.path.join(dataFilepath, dataFilename)

    def __init__(self):
        pass

    def getData(self,dataset, columnNames):
        textData = []
        for columnName in columnNames:
            textData.append(dataset[columnName])
        return textData

    def getLabels(self,dataset, columnName):
        labels = dataset[columnName]
        labels = np.array(list(map(lambda x: 1 if x == False else 0, labels)))
        return labels

    def readFile(self):
        news_articles = pd.read_csv(self.absoluteDataFilePath)
        return news_articles

    def getDataset(self):
        news_articles = self.readFile()
        sentences = self.getData(news_articles,['content'])
        labels = self.getLabels(news_articles, columnName="fact_check")
        return sentences, labels