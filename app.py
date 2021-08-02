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

@app.route("/predict/", methods = ["POST"])
def respond():
    input["area"] = float(get_parameters.area())
    input["postalCode"] = int(get_parameters.postal_code())
    input["subtypeProperty"] = get_parameters.subtype_property()
    input["buildingCondition"] = get_parameters.building_condition()
    input["BedroomsCount"] = get_parameters.bedrooms_count()
    input["fireplaceExists"] = get_parameters.fireplace_exists()
    input["hasGarden"] = get_parameters.has_garden()
    input["hasSwimmingPool"] = get_parameters.has_swimming_pool()
    input["hasTerrace"] = get_parameters.has_swimming_pool()
    input["facadeCount"] = get_parameters.facade_count()
    input["outsideSpace"] = float(get_parameters.outside_space())
    input["landSurface"] = float(get_parameters.land_surface())
    input["hasFullyEquippedKitchen"] = get_parameters.has_fully_equiped_kitchen()

    y = predictor.predict(input)
    return jsonify({"prediction" : f"{y}"})

if __name__ == "__main__":
    predictor = Predictor()
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)