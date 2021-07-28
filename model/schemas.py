### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

# schemas to get the parameters seperately
from flask import Flask, request, jsonify
from pandas.core.base import SpecificationError

app = Flask(__name__)

response = {}

@app.route("/predict/", methods = ["GET"])
class get_parameters():
    def area():
        area = request.args.get("area")
        if area:
            return area
        else:
            response["ERROR"] = "The area has to be given"
        
    def postal_code():
        postalCode = request.args.get("postalCode")
        if len(postalCode) == 4:
            return postalCode
        else:
            response["ERROR"] = "Postal code should exist of 4 characters"
    
    def subtype_property():
        subtypeProperty = request.args.get("subtypeProperty")
        if subtypeProperty:
            return subtypeProperty
        else:
            response["ERROR"] = "The type of building must be indicated"

    def building_condition():
        buildingCondition = request.args.get("buildingCondition")
        # The building condition is on a scale of 1 to 5
        if buildingCondition:
            return buildingCondition
        else:
            response["WARNING"] = "If no condition given, the default value of 0 will be set"
            return 0
    
    # the non-oblique features
    def non_oblique(feature):
        spec = request.args.get(feature)
        if spec:
            return spec
        else:
            return 0
        # return features
    
    
    # def fireplace():
    #     fireplace = request.args.get("fireplaceExists")
    #     if fireplace:
    #         return fireplace
    #     else:
    #         return 0

    # def swimming_pool():
    #     pool = request.args.get("hasSwimmingPool")
    #     if pool:
    #         return pool
    #     else:
    #         return 0

    # def garden():
    #     garden = request.args.get("hasGarden")
    #     if garden:
    #         return garden
    #     else:
    #         return 0

    # def terrace():
    #     terrace = request.args.get("hasTerrace")
    #     if terrace:
    #         return terrace
    #     else:
    #         return 0

    # def equipped_kitchen():
    #     kitchen = request.args.get("hasFullyEquippedKitchen")
    #     if kitchen:
    #         return kitchen
    #     else:
    #         return 0