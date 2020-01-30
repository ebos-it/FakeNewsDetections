class FNDContext:
    def __init__(self, fndConfig, trainStartDate=None, trainEndDate=None):
        self.trainStartDate = trainStartDate
        self.trainEndDate = trainEndDate
        self.fndConfig = fndConfig

    def get_trainStartDate(self):
        return self.trainStartDate

    def get_trainEndDate(self):
        return self.trainEndDate

    def get_fndConfig(self):
        return self.fndConfig
