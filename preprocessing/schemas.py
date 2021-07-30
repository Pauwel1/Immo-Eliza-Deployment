### Immmo Eliza Deployment ###
### BeCode BXL - Bouman 3.31 ###
### Pauwel De Wilde ###

# schemas to get the parameters seperately
from flask import Flask, request, abort
from flask.scaffold import F

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
    
    def facade_count():
        facadeCount = request.args.get("facadeCount", None)
        if facadeCount:
            return facadeCount
        else:
            return 2

    def outside_space():
        outsideSpace = request.args.get("outsideSpace", None)
        if outsideSpace:
            return outsideSpace
        else:
            abort(400, description = "Please enter the available space outside the house (terrace + garden)")

    def land_surface():
        landSurface = request.args.get("landSurface", None)
        if landSurface:
            return landSurface
        else:
            abort(400, description = "Please give the surface of the lot")

    def fireplace_exists():
        fireplaceExists = request.args.get("fireplaceExists")
        if fireplaceExists == 1:
            return 1
        else:
            return 0
    
    def has_swimming_pool():
        hasSwimmingPool = request.args.get("hasSwimmingPool")
        if hasSwimmingPool == 1:
            return 1
        else:
            return 0
    
    def has_garden():
        hasGarden = request.args.get("hasGarden")
        if hasGarden == 1:
            return 1
        else:
            return 0
    
    def has_terrace():
        hasTerrace = request.args.get("hasTerrace")
        if hasTerrace == 1:
            return 1
        else:
            return 0
    
    def has_fully_equiped_kitchen():
        hasFullyEquippedKitchen = request.args.get("hasFullyEquippedKitchen")
        if hasFullyEquippedKitchen == 1:
            return 1
        else:
            return 0

    # the non-oblique features, expressed in 1 or 0
    def non_oblique(feature):
        for f in feature:
            spec = request.args.get(f, None)
            if spec == 1:
                return 1
            else:
                return 0