from newsPortal.newsPortal.newstraining.datasource.inputDataSourceFactory import (
    InputDataSourceFactory,
)


class InputDataGenerator:
    class __InputDataGenerator:
        def __init__(self, fndContext):
            self.context = fndContext

    instance = None

    def __init__(self, fndContext):
        if not InputDataGenerator.instance:
            InputDataGenerator.instance = InputDataGenerator.__InputDataGenerator(
                fndContext
            )
        else:
            InputDataGenerator.instance.context = fndContext

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def generateInput(self, generateType):
        if generateType == "training":
            dataset = None
            context = InputDataGenerator.instance.context
            trainStartDate = context.get_trainStartDate()
            trainEndDate = context.get_trainEndDate()
            fndConfig = context.get_fndConfig()
            fndInputs = fndConfig.fndModel.fndinput_set.all()
            fndOutput = fndConfig.fndModel.fndoutput_set.first()
            # will be a loop as multiple inputs will participate in training
            # for fndInput in fndInputs:
            #     inputDataSourceFactory = InputDataSourceFactory()
            #     dataSource = inputDataSourceFactory.getInputDataSource(fndInput)
            #     if dataSource is not None:
            #         dataset = dataSource.getDataset(
            #             fndInput=fndInput,
            #             fndOutput=fndOutput,
            #             startDate=trainStartDate,
            #             endDate=trainEndDate,
            #         )
            inputDataSourceFactory = InputDataSourceFactory()
            dataSource = inputDataSourceFactory.getInputDataSource(fndInputs.first())
            if dataSource is not None:
                dataset = dataSource.getDataset(
                    fndInput=fndInputs.first(),
                    fndOutput=fndOutput,
                    startDate=trainStartDate,
                    endDate=trainEndDate,
                )
            return dataset