from sklearn.model_selection import train_test_split

class TrainingUtil():

    @staticmethod
    def splitTrainTest(dataset,labels,splitRatio):
        X_train, X_test, Y_train, Y_test = train_test_split(dataset, labels, test_size=splitRatio, random_state=42)
        return X_train,X_test,Y_train,Y_test