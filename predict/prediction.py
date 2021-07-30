import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

from preprocessing.cleaner import Preprocess


class Prediction:
    def __init__(self, newData = pd.DataFrame):
        self.newData = newData
        self.model = joblib.load("model/model.pkl")
        self.prediction()

    def prediction(self, newData = pd.Dataframe):
        newData = Preprocess(newData, isTrainingSet = False)
        model = self.model.drop(["price"], axis=1)
        regressor = LinearRegression(self.model)
        
        y = model.regressor.predict(newData)
        
        return y