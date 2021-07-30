### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

import os
from flask import Flask, jsonify
from preprocessing.schemas import get_parameters
from predict.prediction import Prediction

app = Flask(__name__)

input = {}

@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict/", methods = ["GET", "POST"])
def respond():
    input["area"] = get_parameters.area()
    input["postalCode"] = get_parameters.postal_code()
    input["subtypProperty"] = get_parameters.subtype_property()
    input["buildingCondition"] = get_parameters.building_condition()

    features = ["fireplaceExists", "hasSwimmingPool", "hasGarden", "hasTerrace", "hasFullyEquippedKitchen"]
    for f in features:
        input[f] = get_parameters.non_oblique(f)

    if input.values() == None:
        return jsonify[{"ERROR"} : {"Not all values were entered correctly"}]
    else:
        return jsonify(input)

def predict(input):
    prediction = Prediction(input)
    return jsonify(prediction)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)