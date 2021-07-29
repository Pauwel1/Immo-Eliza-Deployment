### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

import os
from flask import Flask, jsonify
from preprocessing.schemas import get_parameters


app = Flask(__name__)

df = {}

@app.route("/", methods = ["GET"])
def check():
    return "Alive!"

@app.route("/predict/", methods = ["GET", "POST"])
def respond():
    # obliques = ["area", "postalCode", "subtypeProperty", "buildingCondition"]
    # try InvalidUsage(Exception):

    df["area"] = get_parameters.area()
    df["postalCode"] = get_parameters.postal_code()
    df["subtypProperty"] = get_parameters.subtype_property()
    df["buildingCondition"] = get_parameters.building_condition()

    features = ["fireplaceExists", "hasSwimmingPool", "hasGarden", "hasTerrace", "hasFullyEquippedKitchen"]
    for f in features:
        df[f] = get_parameters.non_oblique(f)

    if df.values() == None:
        return jsonify[{"ERROR"} : {"Not all values were entered correctly"}]
    else:
        return jsonify(df)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host = "0.0.0.0", threaded = True, port = port)