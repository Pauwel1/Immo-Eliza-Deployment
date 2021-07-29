### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

# schemas to get the parameters seperately
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

@app.route("/predict/", methods = ["GET"])
class get_parameters():
    def area():
        area = request.args.get("area", None)
        if (area == None):
            abort(400, description = "Area not given (only numbers separated by a '.' are allowed)")
        else:
            return area
        
    def postal_code():
        postalCode = request.args.get("postalCode", None)
        if len(postalCode) == 4:
            return postalCode
        else:
            abort(400, description = "Postal code should exist of 4 intigers, without space")
    
    def subtype_property():
        subtypeProperty = request.args.get("subtypeProperty", None)
        # There should be a limited list to select from, that will be transformed to dummies with values 1 - 22
        lst = [
            "APARTMENT", "HOUSE", "MANSION", 
            "VILLA", "STUDIO", "HOUSE_GROUP", 
            "EXCEPTIONAL_PROPERTY", "MIXED_USE_BUILDING", "APARTMENT_BLOCK",
            "BUNGALOW", "CASTLE", "COUNTRY_HOUSE", 
            "TOWN_HOUSE", "MANOR_HOUSE", "GROUND_FLOOR",
            "PENTHOUSE", "KOT", "CHALET",
            "FARMHOUSE", "PAVILION", "DUPLEX",
            "LOFT", "SERVICE_FLAT", "TRIPLEX"
            ]
        if subtypeProperty in lst:
            return subtypeProperty
        else:
            abort(400, description = "Choose one of the property type options")

    def building_condition():
        buildingCondition = request.args.get("buildingCondition", None)
        # There should be a limited list to select from, that will be transformed to dummies with values 1 - 6
        lst2 = ["GOOD", "TO_RESTORE", "TO_BE_DONE_UP", "AS_NEW", "JUST_RENOVATED", "TO_RENOVATE"]
        if buildingCondition in lst2:
            return buildingCondition
        else:
            abort(400, description = "Choose one of the building condition options")
    
    # the non-oblique features
    def non_oblique(feature):
        spec = request.args.get(feature, None)
        if spec:
            return spec
        else:
            return 0