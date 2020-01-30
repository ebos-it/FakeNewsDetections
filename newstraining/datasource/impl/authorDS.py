from newsPortal.newsPortal.newstraining.datasource.abstractDS import AbstractDS

# need to get details of author, his profile and other information
class AuthorDS(AbstractDS):
    def __init__(self):
        super().__init__()

    def getData(self, dataset, columnNames):
        pass

    def getLabels(self, dataset, columnName):
        pass

    def getDataset(self, fndInput, fndOutput, startDate=None, endDate=None):
        pass
