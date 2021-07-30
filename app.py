### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

import os
from flask import Flask, jsonify
from preprocessing.schemas import get_parameters
from predict.prediction import Predictor

app = Flask(__name__)

input = {}

@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict/", methods = ["GET", "POST"])
def respond():
    input["area"] = float(get_parameters.area())
    input["postalCode"] = int(get_parameters.postal_code())
    input["subtypeProperty"] = get_parameters.subtype_property()
    input["buildingCondition"] = get_parameters.building_condition()
    input["facadeCount"] = int(get_parameters.facade_count())
    input["outsideSpace"] = float(get_parameters.outside_space())
    input["landSurface"] = float(get_parameters.land_surface())

    features = ["fireplaceExists", "hasSwimmingPool", "hasGarden", "hasTerrace", "hasFullyEquippedKitchen"]
    for f in features:
        input[f] = get_parameters.non_oblique(f)

    if input.values() == None:
        return jsonify[{"ERROR"} : {"Not all values were entered correctly"}]
    else:
        y = predictor.predict(input)
        return jsonify[{"Predicted price"} : {y}]

if __name__ == "__main__":
    predictor = Predictor()
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)