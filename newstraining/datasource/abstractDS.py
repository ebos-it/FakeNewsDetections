class AbstractDS:
    def __init__(self):
        pass

    def getData(self, dataset, columnNames):
        pass

    def getLabels(self, dataset, columnName):
        pass

    def getDataset(self, fndInput, fndOutput, startDate=None, endDate=None):
        pass
