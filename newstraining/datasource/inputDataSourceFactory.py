from newsPortal.newsPortal.newstraining.datasource.impl.contentDS import ContentDS
from newsPortal.newsPortal.newstraining.datasource.impl.authorDS import AuthorDS
from newsPortal.newsPortal.newstraining.datasource.impl.titleDS import TitleDS


class InputDataSourceFactory:
    class __InputDataSourceFactory:
        def __init__(self):
            pass

    instance = None

    def __init__(self):
        if not InputDataSourceFactory.instance:
            InputDataSourceFactory.instance = (
                InputDataSourceFactory.__InputDataGenerator()
            )

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def getInputDataSource(self, fndInput):
        dataSource = None
        if (
            fndInput.variableName.lower() == "content"
            and fndInput.trainingIndicator == "Y"
        ):
            dataSource = ContentDS()
        elif (
            fndInput.variableName.lower() == "author"
            and fndInput.trainingIndicator == "Y"
        ):
            dataSource = AuthorDS()
        if (
            fndInput.variableName.lower() == "content"
            and fndInput.trainingIndicator == "Y"
        ):
            dataSource = TitleDS()

        return dataSource
