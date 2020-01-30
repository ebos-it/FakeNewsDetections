from newsPortal.newsPortal.newstraining.datasource.abstractDS import AbstractDS

# yet not figured out how title is going to behave while FND
class TitleDS(AbstractDS):
    def __init__(self):
        super().__init__()

    def getData(self, dataset, columnNames):
        pass

    def getLabels(self, dataset, columnName):
        pass

    def getDataset(self, fndInput, fndOutput, startDate=None, endDate=None):
        pass
