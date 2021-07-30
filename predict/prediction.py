import pandas as pd
import numpy as np
import joblib

from preprocessing.cleaner import Preprocessor
from model.model import Model


class Predictor:
    def __init__(self):
        self.newData = pd.DataFrame()
        self.model = Model()
        self.columns = []

    def predict(self, newData : dict):
        newData = pd.DataFrame(newData, index = [0])
        preprocessor = Preprocessor()
        newData = preprocessor.clean(newData, isTrainingSet = False)
        newData = self.model.adjustToTrainingset(newData)

        X = newData.drop(["price"], axis = 1).to_numpy()
        y = self.model.regressor.predict(newData)

        return np.exp(y)