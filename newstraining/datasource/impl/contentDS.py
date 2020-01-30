import numpy as np
from newsPortal.newsPortal.newsextractor.models import NewsArticle
from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.datasource.abstractDS import AbstractDS


class ContentDS(AbstractDS):
    def __init__(self):
        super().__init__()

    def getData(self, dataset, columnName):
        return dataset[columnName]

    def getLabels(self, dataset, columnName):
        labels = dataset[columnName]
        labels = np.array(list(map(lambda x: 1 if x == False else 0, labels)))
        return labels

    def getDataFromDB(self, startDate=None, endDate=None):
        if startDate == None or endDate == None:
            newsArticles = NewsArticle.objects.all()
        else:
            if startDate > endDate:
                log.debug(
                    f"Unable to fetch news articles as start date is after end date"
                )
                return
            newsArticles = NewsArticle.objects.filter(
                date_posted__range=[startDate, endDate]
            )
        return newsArticles

    def getDataset(self, fndInput, fndOutput, startDate=None, endDate=None):
        news_articles = self.getDataFromDB(startDate, endDate)
        sentences = self.getData(news_articles, fndInput)
        labels = self.getLabels(news_articles, columnName="fact_check")
        return [sentences, labels]
