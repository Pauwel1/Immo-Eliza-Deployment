### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from preprocessing.schemas import Get_parameters
from predict.prediction import Predictor

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict/", methods = ["POST"])
def respond():
    input = {}

    get_params = Get_parameters(request)

    input["area"] = float(get_params.area())
    input["postalCode"] = int(get_params.postal_code())
    input["subtypeProperty"] = get_params.subtype_property()
    input["buildingCondition"] = get_params.building_condition()
    input["BedroomsCount"] = get_params.bedrooms_count()
    input["fireplaceExists"] = get_params.fireplace_exists()
    input["hasGarden"] = get_params.has_garden()
    input["hasSwimmingPool"] = get_params.has_swimming_pool()
    input["hasTerrace"] = get_params.has_terrace()
    input["facadeCount"] = get_params.facade_count()
    input["outsideSpace"] = float(get_params.outside_space())
    input["landSurface"] = float(get_params.land_surface())
    input["hasFullyEquippedKitchen"] = get_params.has_fully_equipped_kitchen()

    y = predictor.predict(input)
    return jsonify({"prediction" : f"{y}"})

if __name__ == "__main__":
    predictor = Predictor()
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)