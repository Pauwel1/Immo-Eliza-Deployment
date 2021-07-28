import os
from flask import Flask, request, jsonify
import numpy as np
from model.schemas import get_parameters


app = Flask(__name__)

df = {}

@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict/", methods = ["GET", "POST"])
def respond():
    df["area"] = get_parameters.area()
    df["postalCode"] = get_parameters.postal_code()
    df["subtypProperty"] = get_parameters.subtype_property()
    df["buildingCondition"] = get_parameters.building_condition()

    features = ["fireplaceExists", "hasSwimmingPool", "hasGarden", "hasTerrace", "hasFullyEquippedKitchen"]
    for f in features:
        df[f] = get_parameters.non_oblique(f)
    
    return jsonify(df)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)