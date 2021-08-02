import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from preprocessing.cleaner import Preprocessor
import joblib

class Model:
    def __init__(self):
        """
        It creates a DataRegressor object containing the dataFrame we are going
        to train it with. Also contains a regressor which will be trained for
        futures predictions
        :param df: cleaned dataframe to train our model
        """
        self.columns = []
        self.regressor = LinearRegression()
        self.newDf = pd.DataFrame()
        self.fitModel()

    def fitModel(self):
        """
        This method will train our model with the data passed to the
        constructor for further predictions
        :return: None
        """
        # We first rescale our price and surfaces to get a better
        # observation of the linear relationship between them and help
        # our model to do better predictions

        df = pd.read_csv("/Users/pauwel/Documents/GitHub/Immo-Eliza-Deployment/preprocessing/housing-data.csv", index_col=0)
        preprocessor = Preprocessor()
        df = preprocessor.clean(df, isTrainingSet = True)

        self.columns = df.columns.to_list()

        # We split our target and our features in numpy arrays
        y = df["price"].to_numpy()
        X = df.drop(["price"], axis=1).to_numpy()

        # We split our data into a train and test datasets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.10, random_state=42
        )

        # We fit our regression model to the train data
        self.regressor.fit(X_train, y_train)

        # print scores
        print("############# LINEAR REGRESSOR #############")
        print("Train score", self.regressor.score(X_train, y_train))
        print("Test score", self.regressor.score(X_test, y_test))

        joblib.dump(self, '/Users/pauwel/Documents/GitHub/Immo-Eliza-Deployment/model/model.pkl')

    def adjustToTrainingset(self, df : pd.DataFrame):
        """
        This method fit the new data into the format of the X dataset from
         the model to be able to predict using the model of the regressor
        :param df: new dataframe to fit into the X format.
        :return: None
        """
        # We create a new data frame with the columns of the dataframe used to
        # train the model
        self.newDf = pd.DataFrame(columns = self.columns)

        print(self.columns)

        # We append our new data to this dataframe
        finalData = self.newDf.append(df)

        # Fill all the nan values with zeros
        finalData.fillna(0, inplace=True)

        finalData = finalData.apply(lambda x: pd.to_numeric(x, errors='coerce')).dropna()

        return finalData