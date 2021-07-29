import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib
from cleaner import DataCleaner

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
        self.fitModel()

    def rescale(self, df):
        """This static method will standardize some of the features,
        all the areas (square meter) will be rescaled into their square root
        and the price into its logarithm
        :param df: cleaned data frame to resale
        :return: rescaleded dataframe
        """

        df["price"] = np.log(df["price"])
        df["area"] = np.sqrt(df["area"])
        df["outsideSpace"] = np.sqrt(df["outsideSpace"])
        df["landSurface"] = np.sqrt(df["landSurface"])

        return df

    def trainModel(self):
        # We first rescale our price and surfaces to get a better
        # observation of the linear relationship between them and help
        # our model to do better predictions
        self.df = self.rescale(self.df)

        # We split our target and our features in numpy arrays
        y = self.df["price"].to_numpy()
        X = self.df.drop(["price"], axis=1).to_numpy()

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

        # Make predictions on test datasets
        predictions = self.regressor.predict(X_test)
        print("Predictions on test datasets: ", predictions)

    def predict(self, df):
        """
        This method receives a new dataframe to make predictions with the
        regressor already trained
        :param df: cleaned dataframe ready to create predictions:
        :return: predictions for price
        """
        self.fitModel(df)
        self.newData = self.rescale(self.newData)

        y = self.newData["price"].to_numpy()
        X = self.newData.drop(["price"], axis=1).to_numpy()

        print("############# LINEAR REGRESSOR FOR NEW DATA #############")
        print("score", self.regressor.score(X, y))
        predictions = self.regressor.predict(X)
        print("Prediciton with new dataframe: ", predictions)

        return np.exp(self.regressor.predict(X))

    def fitModel(self):
        """
        This method will train our model with the data passed to the
        constructor for further predictions
        :return: None
        """
        # We first rescale our price and surfaces to get a better
        # observation of the linear relationship between them and help
        # our model to do better predictions

        df = pd.read_csv("/Users/pauwel/Documents/GitHub/Immo-Eliza-Deployment/preprocessing/utils/housing-data.csv", index_col=0)
        df = DataCleaner(df, isTrainingSet=True)

        self.columns = df.columns.to_list()

        # We split our target and our features in numpy arrays
        y = df["price"].to_numpy()
        X = df.drop(["price"], axis=1).to_numpy()

        # We split our data into a train and test datasets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.10, random_state=42
        )

        # Se fit our regression model to the train data
        self.regressor.fit(X_train, y_train)

        # print scores
        print("############# LINEAR REGRESSOR #############")
        print("Train score", self.regressor.score(X_train, y_train))
        print("Test score", self.regressor.score(X_test, y_test))

        joblib.dump(self, 'model/model.pkl')