from newsPortal.newsPortal.newsPortal.settings import log
from newsPortal.newsPortal.newstraining.dao.fndetectordao import FNDetectorDao
from newsPortal.newsPortal.newstraining.executor.fndExecutor import FNDExecutor
from newsPortal.newsPortal.newstraining.fndContext import FNDContext
from newsPortal.newsPortal.newstraining.trainingUtil import TrainingUtil


class FNDDriver:
    def __init__(self):
        pass

    def run(self):
        log.debug(f"Inside ntDriver run")
        dao = FNDetectorDao()
        configuration = dao.getConfiguration()
        fndContext = self.getFNDContext(configuration)
        self.process(fndContext)

    def process(self, fndContext):
        FNDExecutor.execute(fndContext)

    def getFNDContext(self, configuration):
        section = "trainingConfigurations"
        keys = ["trainingStartDate", "trainingEndDate"]
        log.debug(f"Getting the FND context")
        startDate = TrainingUtil.getConfigAttribute(
            configSection=section, configKey=keys[0]
        )
        endDate = TrainingUtil.getConfigAttribute(
            configSection=section, configKey=keys[1]
        )
        if startDate is None or endDate is None:
            fndContext = FNDContext(fndConfig=configuration)
        else:
            fndContext = FNDContext(
                trainStartDate=startDate, trainEndDate=endDate, fndConfig=configuration
            )
        return fndContext
